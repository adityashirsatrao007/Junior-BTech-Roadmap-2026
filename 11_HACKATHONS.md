# 11 — Hackathons, opencode, Gamma AI

Hackathons are your 3-day crash courses + hiring-stage. This file: how to win a
hackathon (any campus/national one), how to build fast with **opencode**, and how
to pitch with **Gamma AI**.

---

## 1. Hackathon strategy (24–48h, from zero to demo)

Treat every hackathon like a startup sprint. (Your first hackathon = training ground
for national events.)

**Phase 0 — before it starts (30 min)**
- Pick a **theme/problem** (not a feature): "cutting water waste" > "a dashboard".
- Pre-plan the stack: FastAPI or Next.js + MongoDB/Postgres + one AI API.
- Git repo initialized with `.gitignore` + README, dependencies pinned.

**Phase 1 — hour 0-8 (build the skeleton)**
- Auth + 1 core CRUD flow + first API call = "the walking Skeleton".
- Demo this online as soon as it runs — judges love an early working thing.

**Phase 2 — hour 8-20 (the real feature)**
- Build the ONE feature that solves the problem. Everything else = garnish.
- Wire a simple analytics/ML call only if it's genuinely the core.

**Phase 3 — hour 20-30 (polish + pitch)**
- UI shine, empty states, error handling, screenshot demo gifs.
- Prepare a **2-min demo script** and a **pitch deck**.

**Phase 4 — submission** — video + README + linked demo URL. Never submit the raw
repo only. Code the whole thing **the day before**: sleep, then pitch.

---

## 2. opencode — code 10x faster (your hackathon superpower)

`opencode` is an AI coding agent that runs in your terminal.

- **Hook it up:** `npx opencode` or the CLI — point it at your repo and give clear tasks.
- **Hackathon flow:** give opencode the spec ("build a Node/Express + SQLite booking
  API with 3 routes"), it writes the scaffold, you verify + fix edge cases.
- **Rules of engagement:** opencode is your engine, you are the reviewer. You must
  understand every line you commit (judges will ask you about the code).
- **Combine with Gamma AI** (next section) to make the deck while opencode builds the app.

**Speed formula = opencode for boring boilerplate + you for judgment + Gamma for the deck.**

---

## 3. Gamma AI — pitch decks in 30 minutes

**gamma.app** — AI that turns text into designed slides.

- **Prompt template for Gamma:**
  > "Create a 10-slide startup pitch deck for [NAME]: we solve [PROBLEM] for [USERS] by [SOLUTION]. Tech: [STACK]. Traction: [DATAPOINT]. Ask: [WHAT WE NEED]."
- Set brand colors matching your project, then **edit tone, not words** — judges read it fast.
- 3 golden slides: Problem → Demo screenshot → Impact/market. Keep ≤ 10 slides.

---

## 4. Using hackathon wins (this is the point)

- LinkedIn post 24h after win (photo of pitch stage + 2-line tech summary). This gets
  recruiter DMs via alumni skims.
- Add to resume: "1st Place, [Hackathon name], 150+ teams — built X in 36h".
- Example line for your own profile: "1st Place, Hack from the Future 3.0 (600+ teams)".
  Each win compounds — first one is the hardest, the flow is identical after.

**Kill rule:** never say "we'll use AI for everything, so more features" — a solved
one problem with a demo >> five half-working tabs.

---
Next: recap + daily ritual is in `02_DAILY_ROUTINE.md`. Start: `01_GETTING_STARTED.md`.