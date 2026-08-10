# 🧭 MENTOR KIT — how YOU run the check-ins (15 min, one student at a time)

Juniors run themselves if the repo works. Your job is **15 min/week to catch drift,
not to teach**. This page is intentionally minimal — read only what you need.

---

## The Saturday 20:30 check-in (15 min)

Fix a **set slot** each week (e.g. Sat 20:30). Same flow every week:

1. **Look, don't read aloud** — open their `log.md` (DAILY_LOG_TEMPLATE) for the week.
2. Ask in order:
   - "What DSA did you solve this week, and what was the algorithm?"
   - "All 6 problems pushed? SQL both days? aptitude ≥5 days?"
   - "What did you ship?" (from the `15` planner's "This week you ship")
   - "What's blocked?" (their log's ★ Blocked line)
3. **Fix ONE thing only** — pick the single highest-leverage blocker, give a 5-min
   steer (watch X, try Y), never a lecture. Everything else waits for next week.
4. Praise a specific win from the log ("your House Prices README is the best so far").

> If they show up without a log: that IS the signal. The error is the habit, not the topic.

---

## How to spot a stuck student (from their log, in seconds)

| Pattern | Read it as | Do |
|---------|-----------|----|
| 3+ empty days | motivation closure | reset to smallest task (02 rule: 15 min) |
| "solve nothing, watched tutorials" | tutorial trap | assign ONE 30-min task + no new resources |
| blocker line empty 2 weeks | not asking = guessing | force one question in the next log |
| STAR stories blank by W30 | skips round 3 forever | do one together during check-in |
| daily commit missing, excuses present | habit slip | shrink scope: commit ANY file daily |
| "too busy with college" | over-based guilt | re-read `02` note: 2.5h/day is enough |

---

## Canary milestones (Week N = the student's own week N in `15`)

- **W5**: Core CS sprint done — ask 3 of the 12 classics out loud.
- **W10**: Mini-app #1 exists & pushed.
- **W23**: full stack deployed (they should be able to open the URL).
- **W29**: 3 git repos, 2 READMEs, S.T.O.P. answer in 60s.
- **W41**: House Prices submission + a plot.
- **W58**: resume exists on Overleaf, ATS-checkable.
- **W60**: ≥3 portfolio projects. From here the system runs itself.

---

## What gets someone suspended from the plan (red flags)

- Copy-pasting an AI solution they can't explain (ask them to explain their own code).
- Skipping DSA daily for "fast progress" elsewhere.
- Not committing (no commit = no learning surfaced to you).
- Hoarding courses ("I'm collecting resources") for 2 straight weeks.

---

## Mentor shortcuts (your own prep)

- Kanban/home screen: a table of students × (DSA# · SQL# · ship# · blocked?) that only
  you update from Saturday logs. 10 minutes.
- Batch email/message template: start with the student's own log line, end with ONE
  action. Never send a wall of tips.
- If 2+ students hit the same blocker, resolve it once in a 10-min group call and
  paste the fix into the repo (that's how the roadmap grows).

Cross-links: the weeks/Study Days you check → `15_WEEKLY_PLANNER.md`; the snapshot checklist
→ `02_DAILY_ROUTINE.md` §3; log format → `DAILY_LOG_TEMPLATE.md`.