---
cssclasses: daily-note, clean-ui
tags: [daily, journal, micro-tasks]
---

# ⟡ Daily Note — {{DATE}}
> **{{DAY}}** • Week **{{WEEK}}** • {{TIME_12H}}

---

> [!multi-column] **🌅 MORNING EXECUTION FLOW**
>> [!abstract]+ **9:00 AM — DAILY STARTUP**
>> ```mermaid
>> flowchart TD
>>     A[🌅 Wake 6:30] --> B[💧 Hydrate + ☕ Coffee]
>>     B --> C[📋 Open Daily Note<br/>Mod+Shift+d]
>>     C --> D[🎯 Set 3 Intentions]
>>     D --> E[🧠 DSA Triad<br/>LC + CF + CC]
>>     E --> F[🏗️ Build Lane #1<br/>90 min]
>>     F --> G[🏗️ Build Lane #2<br/>90 min]
>>     G --> H[📤 Push → TickTick<br/>python ticktick_sync.py push]
>> ```
>>
>> **Micro-Tasks (Priority Order):**
>> - [ ] **DSA Triad** — 1 LeetCode + 1 Codeforces + 1 CodeChef
>> - [ ] **Build Lane #1** — {{BUILD_TASK_1}}
>> - [ ] **Build Lane #2** — {{BUILD_TASK_2}}
>> - [ ] **20+ Job Applications** — Full-Stack / SDE / AI-ML
>> - [ ] **Content** — Reel + 3 Tweets + Poetry
>> - [ ] **Health** — Workout + Minoxidil + Skincare
>> - [ ] **Reading** — 3 bullets to Spine

---

> [!multi-column] **🧠 DSA TRIAD**
>> [!tip]+ **LeetCode**
>> - Problem: `{{LC_PROBLEM}}`
>> - Link: `{{LC_LINK}}`
>> - Status: `{{LC_STATUS}}`
>> - Time: `{{LC_TIME}}`
>> - Pattern: `{{LC_PATTERN}}`
>>
>> [!example]+ **Codeforces**
>> - Problem: `{{CF_PROBLEM}}`
>> - Link: `{{CF_LINK}}`
>> - Status: `{{CF_STATUS}}`
>> - Time: `{{CF_TIME}}`
>> - Rating: `{{CF_RATING}}`
>>
>> [!success]+ **CodeChef**
>> - Problem: `{{CC_PROBLEM}}`
>> - Link: `{{CC_LINK}}`
>> - Status: `{{CC_STATUS}}`
>> - Time: `{{CC_TIME}}`
>> - Division: `{{CC_DIV}}`

---

> [!multi-column] **🏗️ BUILD LANES — 90 MIN EACH**
>> [!abstract]+ **Lane 1: {{BUILD_TASK_1}}**
>> - **Goal:** `{{LANE1_GOAL}}`
>> - **Stack:** `{{LANE1_STACK}}`
>> - **Blocker:** `{{LANE1_BLOCKER}}`
>> - **Progress:**
>>   - [ ] Setup / Scaffold
>>   - [ ] Core Logic
>>   - [ ] Tests / Edge Cases
>>   - [ ] Polish / Docs
>> - **Commit:** `{{LANE1_COMMIT}}`
>>
>> [!tip]+ **Lane 2: {{BUILD_TASK_2}}**
>> - **Goal:** `{{LANE2_GOAL}}`
>> - **Stack:** `{{LANE2_STACK}}`
>> - **Blocker:** `{{LANE2_BLOCKER}}`
>> - **Progress:**
>>   - [ ] Setup / Scaffold
>>   - [ ] Core Logic
>>   - [ ] Tests / Edge Cases
>>   - [ ] Polish / Docs
>> - **Commit:** `{{LANE2_COMMIT}}`

---

> [!multi-column] **📚 READING LANE — ATOMIC NOTES**
>> [!example]+ **Input**
>> - **Source:** `{{READING_SOURCE}}`
>> - **Type:** `{{READING_TYPE}}` (Paper / Article / Video / Book)
>> - **Spine Connection:** `[[Spine#{{SPINE_TAG}}|{{SPINE_TAG}}]]`
>>
>> [!success]+ **3 Takeaways (Max)**
>> 1. `{{TAKEAWAY_1}}`
>> 2. `{{TAKEAWAY_2}}`
>> 3. `{{TAKEAWAY_3}}`
>>
>> [!abstract]+ **Quotes & Actions**
>> - > `{{QUOTE_1}}`
>> - [ ] `{{ACTION_1}}`
>> - [ ] `{{ACTION_2}}`

---

> [!multi-column] **☀️ MIDDAY TRIAGE (3:30 PM)**
>> [!tip]+ **Sync & Review**
>> - [ ] `python ticktick_sync.py pull` ✅
>> - [ ] Job Apps: `{{JOB_COUNT}}` / 20+
>> - [ ] DSA: `{{DSA_DONE}}` / 3
>> - [ ] Build #1: `{{BUILD1_STATUS}}`
>> - [ ] Build #2: `{{BUILD2_STATUS}}`
>> - [ ] Blocker: `{{MIDDAY_BLOCKER}}`
>> - [ ] Energy: Walk / Stretch / Nap

---

> [!multi-column] **🌙 EVENING WRAP-UP (9:00 PM)**
>> [!success]+ **Final Sync**
>> - [ ] `python ticktick_sync.py pull` ✅
>> - [ ] Content: Reel + 3 Tweets + Poetry
>> - [ ] Journal: 3 sentences
>> - [ ] Tomorrow's 3 Intentions
>> - [ ] Sleep by 23:30 🛌

---

> [!multi-column] **📊 SCORECARD — END OF DAY**
>> [!abstract]+ **Metrics**
>> | Category | Target | Actual | Status |
>> |----------|--------|--------|--------|
>> | DSA Triad | 3 | {{SCORE_DSA}} | {{SCORE_DSA_LABEL}} |
>> | Build Lane #1 | Done | {{SCORE_B1}} | {{SCORE_B1_LABEL}} |
>> | Build Lane #2 | Done | {{SCORE_B2}} | {{SCORE_B2_LABEL}} |
>> | Job Apps | 20+ | {{SCORE_JOBS}} | {{SCORE_JOBS_LABEL}} |
>> | Content Posts | 4 | {{SCORE_CONTENT}} | {{SCORE_CONTENT_LABEL}} |
>> | Reading Bullets | 3 | {{SCORE_READ}} | {{SCORE_READ_LABEL}} |
>> | Workout | 45 min | {{SCORE_WORKOUT}} | {{SCORE_WORKOUT_LABEL}} |
>> | Minoxidil | 2× | {{SCORE_MINOX}} | {{SCORE_MINOX_LABEL}} |
>> | Skincare | AM+PM | {{SCORE_SKIN}} | {{SCORE_SKIN_LABEL}} |
>> | Sleep by 23:30 | Yes | {{SCORE_SLEEP}} | {{SCORE_SLEEP_LABEL}} |
>>
>> **Daily Score: {{SCORE_TOTAL}} / 10** — `{{SCORE_LABEL}}`

---

> [!multi-column] **🪞 REFLECTION**
>> [!example]+ **Win of the Day**
>> `{{WIN}}`
>>
>> [!tip]+ **Friction / Blocker**
>> `{{FRICTION}}`
>>
>> [!abstract]+ **Emotional State**
>> `{{EMOTION}}`
>>
>> [!success]+ **Tomorrow's ONE Thing**
>> `{{TOMORROW_ONE_THING}}`
>>
>> [!abstract]+ **Gratitude (3)**
>> 1. `{{GRATITUDE_1}}`
>> 2. `{{GRATITUDE_2}}`
>> 3. `{{GRATITUDE_3}}`

---

> [!tip]+ **🔗 QUICK LINKS**
>> - [[Home|🏠 Command Center]]
>> - [[templates/daily-note.md|📋 This Template]]
>> - [[templates/project-note.md|🏗️ Project Template]]
>> - [[templates/reading-note.md|📚 Reading Template]]
>> - [[roadmap.md|🗺️ Roadmap]] | [[lanes.md|🛤️ Lanes]] | [[spine.md|🧬 Spine]]
>> - [[daily/|📂 All Daily Notes]]
>> - `Mod+Shift+d` → Today | `Mod+o` → Quick Switch | `Mod+g` → Graph

---

*Generated: {{DATE}} {{TIME}} • Template: `templates/daily-note.md`*