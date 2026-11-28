#!/usr/bin/env python3
"""
TickTick <-> Obsidian <-> GitHub Two-Way Sync
Uses TickTick Open API v1: https://api.ticktick.com/open/v1
"""

import os
import sys
import re
import json
import subprocess
from datetime import datetime
from pathlib import Path

import requests
from dotenv import load_dotenv

# Load token from secure location
load_dotenv("/root/.hermes/.env", override=True)
TOKEN = os.getenv("TICKTICK_TOKEN")
if not TOKEN:
    print("ERROR: TICKTICK_TOKEN not found in /root/.hermes/.env")
    sys.exit(1)

API_BASE = "https://api.ticktick.com/open/v1"
HEADERS = {"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"}

OBSIDIAN_VAULT = Path("/root/secondbrain/obsidian-vault")
DAILY_DIR = OBSIDIAN_VAULT / "daily"
SYNC_SCRIPT = OBSIDIAN_VAULT / "sync-to-github.sh"
GIT_ROOT = Path("/root/secondbrain")

# Project name -> internal mapping
TARGET_LISTS = {
    "Inbox": "inbox",
    "Today": "today",
    "Parking Lot": "parking_lot",
    "Weekly Review": "weekly_review",
}

def api_get(endpoint, params=None):
    r = requests.get(f"{API_BASE}{endpoint}", headers=HEADERS, params=params, timeout=15)
    r.raise_for_status()
    return r.json()

def api_post(endpoint, data):
    r = requests.post(f"{API_BASE}{endpoint}", headers=HEADERS, json=data, timeout=15)
    r.raise_for_status()
    return r.json()

def api_post_raw(endpoint, data=None):
    r = requests.post(f"{API_BASE}{endpoint}", headers=HEADERS, json=data, timeout=15)
    r.raise_for_status()
    return r.json() if r.content else {}

def get_all_projects():
    """Fetch all projects/lists from TickTick"""
    return api_get("/project")

def find_project_id(name):
    """Find project ID by name (case-insensitive)"""
    projects = get_all_projects()
    for p in projects:
        if p.get("name", "").lower() == name.lower():
            return p["id"]
    return None

def get_project_data(project_id):
    """Get tasks + project info for a project"""
    return api_get(f"/project/{project_id}/data")

def create_task(project_id, title, content="", tags=None, due_date=None):
    """Create a task in a project"""
    data = {"projectId": project_id, "title": title}
    if content:
        data["content"] = content
    if tags:
        data["tags"] = tags
    if due_date:
        data["dueDate"] = due_date
    return api_post("/task", data)

def complete_task(project_id, task_id):
    """Mark task as complete"""
    return api_post_raw(f"/project/{project_id}/task/{task_id}/complete")

def get_today_daily_path():
    """Get today's daily note path"""
    today = datetime.now().strftime("%Y-%m-%d")
    return DAILY_DIR / f"{today}.md"

def parse_microtasks_from_daily(daily_path):
    """Extract [ ] micro-tasks from today's daily note - ONLY from the main Micro-Tasks section"""
    if not daily_path.exists():
        return []
    content = daily_path.read_text(encoding="utf-8")
    # Match lines with [ ] or [x] followed by task text
    # ONLY from the main "Micro-Tasks (Priority Order):" section, not nested callouts
    tasks = []
    in_microtasks_section = False
    for line in content.split("\n"):
        # Detect the start of the micro-tasks section
        if "Micro-Tasks (Priority Order)" in line:
            in_microtasks_section = True
            continue
        # Stop at next major section (starts with > [! or ## or ---)
        if in_microtasks_section and (line.startswith("> [") or line.startswith("##") or line.startswith("---")):
            in_microtasks_section = False
            continue
        if not in_microtasks_section:
            continue
        # Strip callout prefixes like ">> " or "> "
        clean_line = re.sub(r"^(\s*>+\s*)+", "", line)
        match = re.match(r"^\s*[-*]\s+\[([ x])\]\s+(.+)$", clean_line)
        if match:
            status, text = match.groups()
            # Clean up the text: remove markdown bold, em dash descriptions
            clean_text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)  # Remove **bold**
            clean_text = re.sub(r"\s*[—-]\s*.+$", "", clean_text)  # Remove — description
            clean_text = clean_text.strip()
            tasks.append({"text": clean_text, "done": status == "x", "raw_line": line.strip()})
    return tasks

def update_daily_checkbox(daily_path, task_text, done=True):
    """Update a specific checkbox in daily note"""
    if not daily_path.exists():
        return False
    content = daily_path.read_text(encoding="utf-8")
    lines = content.split("\n")
    updated = False
    for i, line in enumerate(lines):
        # Match the task text (allow partial match)
        if f"[ ] {task_text}" in line or f"[-] {task_text}" in line or f"[*] {task_text}" in line:
            lines[i] = line.replace("[ ]", "[x]").replace("[-]", "[x]").replace("[*]", "[x]")
            updated = True
        elif f"[x] {task_text}" in line and not done:
            lines[i] = line.replace("[x]", "[ ]")
            updated = True
    if updated:
        daily_path.write_text("\n".join(lines), encoding="utf-8")
    return updated

def push_microtasks():
    """Push today's micro-tasks from Obsidian to TickTick 'Today' list"""
    daily_path = get_today_daily_path()
    microtasks = parse_microtasks_from_daily(daily_path)
    if not microtasks:
        print("No micro-tasks found in today's daily note")
        return

    project_id = find_project_id("Today")
    if not project_id:
        print("ERROR: 'Today' list not found in TickTick")
        return

    # Get existing tasks to avoid duplicates
    existing = get_project_data(project_id)
    existing_titles = {t["title"].strip().lower() for t in existing.get("tasks", []) if t.get("status") != 2}

    created = 0
    for mt in microtasks:
        if mt["done"]:
            continue
        title_lower = mt["text"].strip().lower()
        if title_lower in existing_titles:
            print(f"  SKIP (exists): {mt['text']}")
            continue
        try:
            create_task(project_id, mt["text"], tags=["daily", "microtask"])
            print(f"  CREATED: {mt['text']}")
            created += 1
        except Exception as e:
            print(f"  ERROR creating '{mt['text']}': {e}")

    print(f"Push complete: {created} new tasks created")

def pull_completed():
    """Pull completed tasks from TickTick and update Obsidian daily note"""
    daily_path = get_today_daily_path()
    if not daily_path.exists():
        print("No daily note for today")
        return

    # Check all target lists for completed tasks
    for list_name, list_key in TARGET_LISTS.items():
        project_id = find_project_id(list_name)
        if not project_id:
            print(f"List '{list_name}' not found, skipping")
            continue

        data = get_project_data(project_id)
        tasks = data.get("tasks", [])
        for task in tasks:
            if task.get("status") == 2:  # Completed
                title = task.get("title", "").strip()
                if title:
                    updated = update_daily_checkbox(daily_path, title, done=True)
                    if updated:
                        print(f"  MARKED DONE in Obsidian: {title}")

    # Sync to GitHub
    print("Syncing Obsidian to GitHub...")
    result = subprocess.run(["bash", str(SYNC_SCRIPT)], capture_output=True, text=True, cwd=GIT_ROOT)
    if result.returncode == 0:
        print("  GitHub sync successful")
    else:
        print(f"  GitHub sync failed: {result.stderr}")

def add_task_cli(title, list_name="Inbox"):
    """CLI: Add a task to a list"""
    project_id = find_project_id(list_name)
    if not project_id:
        print(f"List '{list_name}' not found. Available: {list(TARGET_LISTS.keys())}")
        return
    try:
        result = create_task(project_id, title)
        print(f"Created task in '{list_name}': {result.get('id')}")
    except Exception as e:
        print(f"Error: {e}")

def done_task_cli(substring):
    """CLI: Mark task complete by substring match"""
    for list_name, list_key in TARGET_LISTS.items():
        project_id = find_project_id(list_name)
        if not project_id:
            continue
        data = get_project_data(project_id)
        for task in data.get("tasks", []):
            if substring.lower() in task.get("title", "").lower() and task.get("status") != 2:
                complete_task(project_id, task["id"])
                print(f"Completed: {task['title']} (in {list_name})")
                # Also update Obsidian
                daily_path = get_today_daily_path()
                if daily_path.exists():
                    update_daily_checkbox(daily_path, task["title"], done=True)
                    subprocess.run(["bash", str(SYNC_SCRIPT)], cwd=GIT_ROOT)
                return
    print(f"No matching incomplete task found for: {substring}")

def list_projects_cli():
    """CLI: List all projects"""
    projects = get_all_projects()
    print("Your TickTick Lists/Projects:")
    for p in projects:
        print(f"  - {p.get('name')} (id: {p.get('id')})")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 ticktick_sync.py <command> [args]")
        print("Commands:")
        print("  push              - Push today's micro-tasks from Obsidian to TickTick 'Today'")
        print("  pull              - Pull completed tasks from TickTick to Obsidian + GitHub sync")
        print("  add \"title\" [list] - Add task to list (default: Inbox)")
        print("  done \"substring\"    - Mark matching task complete")
        print("  lists             - List all TickTick projects")
        return

    cmd = sys.argv[1].lower()
    if cmd == "push":
        push_microtasks()
    elif cmd == "pull":
        pull_completed()
    elif cmd == "add":
        if len(sys.argv) < 3:
            print("Usage: add \"title\" [list_name]")
            return
        title = sys.argv[2]
        list_name = sys.argv[3] if len(sys.argv) > 3 else "Inbox"
        add_task_cli(title, list_name)
    elif cmd == "done":
        if len(sys.argv) < 3:
            print("Usage: done \"substring\"")
            return
        done_task_cli(sys.argv[2])
    elif cmd == "lists":
        list_projects_cli()
    else:
        print(f"Unknown command: {cmd}")

if __name__ == "__main__":
    main()