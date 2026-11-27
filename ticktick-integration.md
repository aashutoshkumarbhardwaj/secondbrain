# TickTick Integration Plan (Optional Enhancement)

**Status:** App downloaded on phone. Hermes can integrate via API.

---

## Why Add TickTick?
| Benefit | Current Hermes/Cron | With TickTick |
|---------|---------------------|---------------|
| **Push notifications** | Telegram only | ✅ Native Android alerts at 9 AM / 3:30 PM / 9 PM |
| **Checkbox dopamine** | Text in Telegram | ✅ Satisfying tap, streaks, visual progress |
| **Calendar view** | Manual | ✅ Time-blocked day view |
| **Pomodoro timer** | Manual | ✅ Built-in focus sessions |
| **Offline access** | Needs internet | ✅ Full offline, syncs later |

---

## Integration Options

### Option A: Manual Sync (Zero Code)
1. Morning cron sends micro-tasks → You manually add to TickTick (30 sec)
2. You tick in TickTick → Evening cron asks for scorecard
3. **Cost:** 30 sec/day. **Benefit:** Full TickTick UX.

### Option B: API Sync (One-Time Setup)
1. Get TickTick API token: `https://ticktick.com/developer` → Create App → OAuth
2. Store token in Hermes auth or env
3. Python script: `cron → create TickTick tasks → you tick → cron reads completion`
4. **Cost:** 30 min setup. **Benefit:** Fully automated.

### Option C: ticktick-cli (CLI Tool)
```bash
pip install ticktick-cli
ticktick auth login
ticktick task add "LeetCode" --due "today 09:00"
ticktick task list --today
```
**Cost:** 5 min. **Benefit:** Terminal-native, scriptable.

---

## My Recommendation: **Start with Option A (Manual) for 1 week.**

**Reason:** You just set up the entire system. Adding API complexity now = friction. The cron prompts already give you the exact micro-tasks. Just copy → TickTick → tick.

**After 1 week:** If you feel the manual step is annoying, we'll do Option C (ticktick-cli) in 5 minutes.

---

## TickTick Project Structure (Mirror Your Lanes)
```
📁 Projects (in TickTick)
├── 🟢 BUILD — ATS Extension + Job Apps
├── 📚 READING — CS224n, Papers
├── 🎯 OPEN — Clipping Tool, Content
├── 🅿️ PARKING LOT — Rust, Fine-tuning, K8s...
├── 🏋️ PHYSIQUE — Workout, Minoxidil, Skincare
└── 🌙 DAILY RITUAL — DSA 3, Sleep, Journal
```

**Tags:** `#build` `#reading` `#open` `#parking` `#physique` `#ritual`

---

## Next Step
**For now:** Ignore this file. Use the cron micro-tasks in Telegram. 
**When ready:** Say "Setup TickTick CLI" and I'll install `ticktick-cli` and hook it to the morning/evening cron jobs.