---
cssclasses: project-note, clean-ui
tags: [project, build-lane]
---

# ⟡ Project: {{PROJECT_NAME}}
> **Status:** `{{STATUS}}` • **Lane:** `{{LANE}}` • **Started:** {{DATE}} • **Target:** {{TARGET_DATE}}

---

## 🎯 North Star
> *One sentence: what does "done" look like?*

**Definition of Done:**

---

## 📐 Architecture & Decisions
> *Key technical choices, trade-offs, links to ADRs.*

| Decision | Context | Choice | Rationale |
|----------|---------|--------|-----------|
| | | | |

---

## 🧱 Task Breakdown
> *Atomic, ordered, checkable. Use `■` for current sprint.*

### Current Sprint ({{SPRINT_NAME}})
- [ ] `■` 
- [ ] `■` 
- [ ] `□` 

### Backlog
- [ ] 
- [ ] 

---

## 📝 Build Log — *Append only, reverse chronological*

### {{DATE}} — {{SESSION_FOCUS}}
**Learned:**
- 

**Built/Fixed:**
- 

**Blockers:**
- 

**Next Action:**
- 

---

## 🔬 Research & References
> *Links, snippets, docs that matter.*

| Topic | Link / Note | Key Insight |
|-------|-------------|-------------|
| | | |

---

## 📈 Progress Metrics
| Metric | Current | Target | Trend |
|--------|---------|--------|-------|
| | | | |

---

## 🔗 Related Notes
```dataview
LIST
FROM ""
WHERE contains(file.tags, "project") AND file.name != "{{PROJECT_NAME}}"
SORT file.mtime DESC
LIMIT 10
```

---

*Project template v1.0 • Keep it lean. Update the Build Log every session.*