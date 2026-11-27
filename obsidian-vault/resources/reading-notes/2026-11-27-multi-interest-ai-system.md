# Reading Notes: Multi-Interest AI System (Hesam Sheikh)

**Source:** https://multyhead.substack.com/p/if-you-have-too-many-interests-build
**Date:** 2026-11-27
**Lane:** Reading
**Spine Connection:** Validates my entire Hermes + Second Brain architecture

---

## Core Thesis
> You're not unfocused — you're **unplanned**. ADHD brains negotiate interests every morning. Fix: Externalize planning force to AI agent.

---

## Rule 1: Lanes, Not Sequences
| Lane | Purpose | Your Current Mapping |
|------|---------|---------------------|
| **Build** | Main focus (70%) | ATS Extension + Job Apps |
| **Reading** | Slow burn (15%) | 1 chapter/paper/week |
| **Open** | Side quest (10%) | Clipping tool + content automation |
| **Parking Lot** | Bookmarked (5%) | Rust, Fine-tuning, K8s, Compilers, Advanced Algos |

**Key Insight:** Nothing gets dropped → no anxiety. Agent spreads lanes across week.

---

## Rule 2: Find the Spine
**My Spine:** *Shipping production-grade AI/Full-Stack products that solve real hiring problems*

| Interest | Spine Role |
|----------|------------|
| Full-Stack (FastAPI, Next.js) | **CODE builds it** |
| AI/ML (LangChain, RAG, LLMs) | **CODE builds it** |
| DevOps (Linux, Docker, HF) | **CODE builds it** |
| UI/UX (Tailwind) | **DESIGN makes it usable** |
| Psychology/Behavioral Econ | **PSYCHOLOGY understands users** |
| Tech Writing | **WRITING markets it** |
| Content (Reels, Tweets, Shayari) | **VIDEO gets it seen** |
| DSA/Algorithms | **CODE builds it (efficiently)** |

---

## 5-Part System
| # | Component | My Implementation |
|---|-----------|-------------------|
| 1 | **Agent** | ✅ Hermes (this instance) |
| 2 | **Resources** | ✅ `resources.json` (CV, GitHub, jobs, papers) |
| 3 | **Notion** | ✅ Second Brain (GitHub + HF Space) + `roadmap.md` |
| 4 | **Obsidian** | ✅ `/root/obsidian-vault` (this vault) |
| 5 | **Planner** | ✅ Cron jobs + `diary.py` + micro-tasks |

---

## Weekly Loop (Automated)
**Trigger:** Sunday 10 AM IST (cron job `709508e30233`)
**Process:**
1. Read completed tasks (diary), Obsidian notes, blockers
2. Update roadmap.md (week summary, metrics, next week)
3. Update lanes.md (transitions if needed)
4. Plan daily micro-tasks (3-5/day)
5. Deliver Telegram summary

---

## Research Backing
- **Barkley (2011):** ADHD = executive function deficit → externalize planning
- **Harkin et al. (2016, n=19,951):** Progress tracking + physical record = massive goal boost
- **ADHD coaching (148 students, 8 weeks):** Improved study skills, self-esteem, satisfaction

---

## My Assessment
**This article describes exactly what I've built.** The only gaps were:
1. Explicit Parking Lot (now in lanes.md + resources.json)
2. Structured Roadmap/Spine docs (now created)
3. Weekly Loop cron (now active)
4. Daily micro-task checkboxes in cron prompts (updated)

**Next:** Execute the loop. Trust the system.