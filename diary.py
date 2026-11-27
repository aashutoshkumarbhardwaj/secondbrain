import argparse, json, subprocess
from datetime import date, datetime, timedelta
from pathlib import Path

diary_file = Path("/root/secondbrain/docs/diary.json")
today = date.today().isoformat()
now_time = datetime.now().strftime("%I:%M %p")

data = json.loads(diary_file.read_text()) if diary_file.exists() else {"days": {}}
day = data["days"].setdefault(today, {"tasks": [], "notes": []})

parser = argparse.ArgumentParser()
parser.add_argument("--action", required=True, choices=["add", "doing", "done", "read", "reclassify", "note"])
parser.add_argument("--title", default="", help="Task, article/book title, or diary note")
parser.add_argument("--category", default="General", help="Any dynamic type: Reading, DSA, Study, Jobs, Dev, Routine, etc.")
parser.add_argument("--priority", default="high", choices=["high", "low"], help="high=Important, low=Less Important")
parser.add_argument("--note", default="", help="Extra detail, takeaway, or status update")
args = parser.parse_args()

if args.action == "add":
    day["tasks"].append({
        "title": args.title,
        "category": args.category,
        "priority": args.priority,
        "note": args.note,
        "status": "todo",
        "updated_at": now_time
    })
    tag = "Important" if args.priority == "high" else "Less Important"
    day["notes"].append({"time": now_time, "text": f"Planned [{args.category} · {tag}]: {args.title}" + (f" — {args.note}" if args.note else "")})

elif args.action in ("doing", "done"):
    matched = False
    for t in day["tasks"]:
        if args.title.lower() in t["title"].lower() and t["status"] != "done":
            t["status"] = args.action
            t["updated_at"] = now_time
            if args.category != "General":
                t["category"] = args.category
            if args.note:
                t["note"] = args.note
            matched = True
            break
    if not matched:
        day["tasks"].append({
            "title": args.title,
            "category": args.category,
            "priority": args.priority,
            "note": args.note,
            "status": args.action,
            "updated_at": now_time
        })
    verb = "Working on" if args.action == "doing" else "Completed"
    day["notes"].append({"time": now_time, "text": f"{verb} [{args.category}]: {args.title}" + (f" — {args.note}" if args.note else "")})

elif args.action == "read":
    day["tasks"].append({
        "title": args.title,
        "category": "Reading",
        "priority": args.priority,
        "note": args.note,
        "status": "done",
        "updated_at": now_time
    })
    day["notes"].append({"time": now_time, "text": f"Read: {args.title}" + (f" — {args.note}" if args.note else "")})

elif args.action == "reclassify":
    for t in day["tasks"]:
        if args.title.lower() in t["title"].lower():
            if args.category != "General":
                t["category"] = args.category
            t["priority"] = args.priority
            t["updated_at"] = now_time
            if args.note:
                t["note"] = args.note
            break
    day["notes"].append({"time": now_time, "text": f"Updated category/priority for '{args.title}' → {args.category} ({args.priority})"})

elif args.action == "note":
    day["notes"].append({"time": now_time, "text": args.title})

# Compute real streak & best streak across logged dates with >=1 completed item
active_dates = sorted([
    d for d, info in data["days"].items()
    if any(t.get("status") == "done" for t in info.get("tasks", []))
])
best_streak, running, prev_d = 0, 0, None
for d_str in active_dates:
    cur_d = date.fromisoformat(d_str)
    if prev_d and (cur_d - prev_d).days == 1:
        running += 1
    else:
        running = 1
    best_streak = max(best_streak, running)
    prev_d = cur_d

streak = 0
check_d = date.today()
if check_d.isoformat() not in active_dates:
    check_d -= timedelta(days=1)
while check_d.isoformat() in active_dates:
    streak += 1
    check_d -= timedelta(days=1)

data["latest_date"] = today
data["updated_at"] = datetime.now().strftime("%b %d, %I:%M %p IST")
data["streak"] = streak
data["best_streak"] = best_streak
diary_file.write_text(json.dumps(data, indent=2))

subprocess.run(["git", "-C", "/root/secondbrain", "add", "docs/"], check=True)
subprocess.run(["git", "-C", "/root/secondbrain", "commit", "-m", f"Diary: {args.action} {args.title[:40]}"], check=False)
subprocess.run(["git", "-C", "/root/secondbrain", "push", "origin", "main"], check=True)
print("Digital diary updated & pushed!")
