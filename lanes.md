# Lanes Configuration (Rule 1: Lanes, Not Sequences)

**Purpose:** Every interest gets a permanent lane. Nothing gets dropped → no anxiety. Agent spreads lanes across the week.

---

## Lane Definitions

### 🟢 BUILD (Primary Focus — 70% Energy)
**Current Assignment:** ATS Resume Optimizer Extension + Job Application Pipeline
- **Deliverable:** Published Chrome Extension + 140 applications/week
- **Daily Time:** 4-6 hours (Morning project + Afternoon apps)
- **Success Signal:** Extension live on Chrome Web Store; 20+ apps/day sustained

**Next in Queue (Auto-promoted when Build completes):**
1. Second Brain v2: Multi-modal RAG + Agent memory
2. Full-Stack SaaS: AI-powered interview prep platform

---

### 📚 READING (Slow Burn — 15% Energy)
**Current Assignment:** 1 Chapter/Paper per Week
- **Week 1 (Nov 24-30):** CS224n Lecture 1-2 (Word Vectors, Word2Vec)
- **Week 2 (Dec 1-7):** CS224n Lecture 3-4 (GloVe, Subword) + Paper: "LangChain in Production"
- **Week 3 (Dec 8-14):** CS224n Lecture 5-6 (Transformers Intro) + Paper: "QLoRA"
- **Ongoing:** 1 paper from `resources.json → courses_papers.active_learning` per week

**Rules:**
- One chapter/paper = one Obsidian note in `/resources/reading-notes/`
- 3 bullet takeaways max per note
- Connect to Spine: "How does this help ship hiring AI products?"

---

### 🎯 OPEN (Side Quest — 10% Energy)
**Current Assignment (This Week):** Video Clipping Tool + Content Automation
- **Setup:** `ffmpeg` + Python wrapper on personal laptop
- **Workflow:** YouTube URL → Transcript → 10-20s timestamp → Clip → Caption → Post
- **Timebox:** 2 sessions (Wed + Sat, 1-2 hrs each)

**Next in Queue:**
1. Automated Tweet thread generator from blog posts
2. Instagram Reel template system (Canva API / FFmpeg overlay)

---

### 🅿️ PARKING LOT (Bookmarked — 5% Energy)
**Items:** (from `resources.json → courses_papers.parking_lot`)
| Item | Why Parked | Revisit Trigger |
|------|------------|-----------------|
| Rust for Systems Programming | Not on critical path for hiring | Build lane clears; need systems depth |
| LLM Fine-tuning (QLoRA/PEFT) | GPU access limited; high complexity | HF Space A10G available; project needs custom model |
| Kubernetes & Distributed Systems | Overkill for current projects | Scaling need arises |
| Compiler Design (LLVM) | Academic interest only | Curiosity spike; no deliverable |
| Advanced Algorithms (MIT 6.046) | DSA prep covers 80% | FAANG interview loop demands it |

**Rules:**
- Zero guilt. Zero mental load.
- Agent surfaces one item/month in weekly loop: "Still parked? Promote to Open?"
- Human decides: Promote / Keep Parked / Delete

---

## Lane Transition Protocol
| From → To | Trigger | Agent Action |
|-----------|---------|--------------|
| Parking Lot → Open | Human says "promote X" or weekly loop surfaces | Move to Open lane, assign timebox |
| Open → Build | Open deliverable shipped + human confirms | Promote to Build, demote current Build to Reading/Open |
| Build → Reading | Build deliverable shipped + no immediate next | Demote to Reading (maintenance mode) |
| Any → Parking Lot | Human says "park X" or 4 weeks no progress | Move to Parking Lot, preserve bookmark |

**Human always decides. Agent only suggests.**