# 06 — Full Stack Development from Scratch (+ how to explain a project in interviews)

By the end of Phase 1 you will have built and deployed **3 projects** you can explain in any interview.

Stack you'll learn (industry standard): **HTML → CSS → JavaScript → React (frontend) + Node/Express (backend) + MongoDB (database)** = the MERN stack.

---

## 1. What is a "full stack" app? (30-second version)

A web app = 3 layers:
```
Browser (Frontend: what user sees) 
   ↕  talks to (via HTTP/API)
Server (Backend: business logic, auth) 
   ↕  talks to
Database (stores data: MongoDB text/PostgreSQL)
```

**Frontend:** HTML (structure), CSS (look), JavaScript (behavior), React (framework).
**Backend:** Node.js + Express (server + routes).
**Database:** MongoDB (documents) or PostgreSQL (tables).

---

## 2. Learning order (follow this, not your friends)

| Step | What | When | Key resource |
|------|------|------|--------------|
| 1 | HTML & CSS basics | Week 1–2 | freeCodeCamp "Responsive Web Design" |
| 2 | JavaScript core (variables, functions, arrays, DOM, fetch/async) | Week 3–5 | freeCodeCamp "JavaScript Algorithms & DS" + JavaScript Mastery |
| 3 | React basics (components, props, state, hooks) | Week 6–9 | freeCodeCamp React + build 1 small app |
| 4 | Node + Express (routes, REST API, middleware) | Week 10–12 | Traversy "Node.js Crash Course" |
| 5 | MongoDB (schemas, CRUD, mongoose) | Week 13–14 | Traversy / MongoDB University free |
| 6 | Connect it all → build, auth (JWT), deploy | Week 15–18 | follow one full MERN tutorial |
| 7 | YOUR OWN project (not a tutorial clone) | Week 19–24 | plan below |

**Resource links:**
- Full Stack JS roadmap video — Traversy Media (YouTube: "Full Stack JavaScript Developer Roadmap")
- American/Indian both good: **CodeWithHarry**, **freeCodeCamp**, **Traversy Media**, **JavaScript Mastery**, **Bro Code** (HTML/CSS basics)
- Interactive full roadmap: https://roadmap.sh/full-stack

---

## 3. Phase-1 mini projects (build, don't just watch)

1. **Landing page** (pure HTML/CSS) — copy the design of any fav site, pixel-close (day 3–6).
2. **Interactive todo / calculator** (JS + DOM) — events, arrays, localStorage (week 5).
3. **React app calling an API** — e.g., weather or movie search (week 9).
4. **REST API** (Express + MongoDB) — CRUD on a `todos` or `books` collection (week 13).
5. **Full stack app with auth** — signup/login with JWT, protected pages (week 16+).

**Then your own** (pick ONE, make it YOUR THING):
- Expense / budget tracker (users + categories + charts)
- Library / inventory manager
- Society/event portal for your college
- Fitness/workout log

---

## 4. How to EXPLAIN a project in an interview (they always ask this)

Use the **S.T.O.P.** structure — under 90 seconds, no rambling:
1. **S — Situation/Problem:** *"College clubs had no central place to book equipment..."*
2. **T — Tech stack + why:** *"MERN. React for fast UI, Express for REST API, MongoDB for flexible event data + JWT auth."*
3. **O — What I did (features):** user login, CRUD on bookings, "no double-booking" logic, deployed on Render.
4. **P — Proud point / learning / numbers:** *"Handled conflicts with a database check, refactored pages into components → cut duplicate code by 30%."*

Then be ready for 3 follow-ups:
- *"Why MongoDB not SQL here?"* → data shape flexible, but honestly a relational model also works → acknowledge trade-off.
- *"How does JWT auth work end to end?"* → login returns signed token → client sends in header → server verifies on every protected route.
- *"What's a Promise / how does fetch work?"* → be honest: watch 1 video, then you'll answer.

---

## 5. MAS-important DO / DON'T

**DO**
- Build with **your own feature ideas**, comment line-by-line so you can explain it.
- Deploy (Render / Vercel / Netlify) even the small projects → live links on resume.
- Add screenshots + README + live URL to GitHub repos.
- Learn to read errors (log is your best friend; Google error text verbatim).

**DON'T**
- Watch 20 tutorials and build 0. **Build > watch.**
- Copy entire project code and claim it (interviewers will cross-question you on it).
- Use AI to write the whole project and then you can't explain it.
- Skip the database step to "save time" — DB is the second-half of full stack.

---

## Resources
- full roadmap interactive: https://roadmap.sh/full-stack
- free MERN+full project: JavaScript Mastery / Traversy MERN playlist (YouTube)
- deploy: https://render.com (free tier), https://vercel.com (frontends)
- free practice/plan: `dev.to` The Complete Full Stack Roadmap 2026

**Next when done with P1:** `07_ML_FROM_0.md` — ML is your Phase-2 focus module and it pairs beautifully with the full-stack skills you just built.