# 01 — Getting Started (Day 1) · Setup Everything Once

Read this on the day you begin (your **Day 1** — pick any day) and complete the
checklist. You will never repeat this setup.

> **First do the full Windows installs in `00_SETUP_WINDOWS.md`** — Python, Java, Node,
> MongoDB, MySQL, PostgreSQL, Git, VS Code, Postman, all PATH steps, then the final
> verify block. Come back here after every version command prints a number.

---

## Why this matters

Most juniors fail classes not because they don't study, but because setup took them 3 weeks and then they quit. This page makes Day 1–2 = **6 hours of installs**, then you're free to actually learn.

---

## 1. Install the tools (order matters)

| Tool | Why | Where |
|------|-----|-------|
| VS Code | Editor for everything | https://code.visualstudio.com |
| Git | Version control (all projects) | https://git-scm.com/downloads |
| Python 3.12+ | ML + scripting | https://python.org (tick "Add to PATH") |
| Node.js 20 LTS | Full Stack backend | https://nodejs.org |
| Android Studio | Mobile (if choosing Android) | https://developer.android.com/studio |
| MySQL / SQLite | SQL practice | SQLite is bundled; MySQL for projects |
| Google Chrome + Postman | Test APIs | https://www.postman.com/downloads |
| Anaconda (optional) | Python + Jupyter + ML libs in one | https://www.anaconda.com |

**Tip:** For ML you can also just use **Google Colab** (zero installs, free GPU). Don't let installs block your first day — Colab in the browser works instantly.

---

## 2. Accounts (create same @handle everywhere → looks professional)

from README §6:
1. **GitHub** — `https://github.com` — username like `yourname-dev`
2. **LeetCode** — `https://leetcode.com`
3. **GFG practice** — `https://practice.geeksforgeeks.org`
4. **Kaggle** — `https://kaggle.com` (ML datasets + free mini-courses)
5. **HackerRank** — same handle
6. **LinkedIn** — professional headline: `BTech CSE '28 · Full Stack + AI/ML`
7. **Unstop** — `https://unstop.com` (hackathons/contests/internships)
8. **Overleaf** — `https://overleaf.com` (LaTeX resume, template later)
9. **Google Colab** — `https://colab.research.google.com`
10. **Discord** — join GFG & LeetCode+JSM communities

---

## 3. Verify every tool works (5-minute smoke test)

Open VS Code terminal (Ctrl+`) and run:

```bash
git --version          # → git version 2.x
python --version       # → Python 3.12.x
node --version         # → v20.x
```

Then verify Git identity (you "own" your commits):

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

Login to GitHub in terminal with PAT (Personal Access Token) or `gh` CLI:

```bash
# Easy route — install gh CLI: https://cli.github.com
gh auth login
```

---

## 4. Day-1 mini victory (build momentum)

**Never coded before? Start with `01_PYTHON_FROM_ZERO.md` + run `ml-code/00_python_first.py`
right now** — it's your first program, ~10 minutes. Then come back here.

Make your first "Hello world" simultaneously on **GitHub + VS Code + terminal**:

1. `git init` a folder named `hello-world`
2. Add `hello.py` (`print("I started skill-day 1 today")`)
3. `git add . && git commit -m "Day 1"`
4. Create a repo `hello-world` on GitHub, then `git remote add origin <url>` and `git push -u origin main`

Now your GitHub has a green square. Do this **every day from now on** — with real work, not empty commits.

Full Git training → `05_GIT_GITHUB.md`.

---

## 5. Get your daily-learning workspace ready

Create one folder on your machine:

```
~/btech-journey/
  ├── dsa/          # your solutions, one file per problem
  ├── projects/     # full-stack, mobile, ml mini-projects
  ├── notes/        # 1-line daily log (markdown)
  └── resume/       # all resume files
```

Save the daily log format (notes/daily.md):

```markdown
## Skill-day 1 (day 1 of your journey)
- DSA: 88 Merge Sorted Array (solved after hint, revisit 7d)
- SQL: 1757 Recyclable (JOIN/WHERE refresher)
- Aptitude: 15 qs, avg time 2.1 min/q
- Focus: HTML/CSS basics → made first landing section
- Commit: pushed to github ✅
```

---

## 6. Learning rules that make or break you

| Do | Don't |
|----|-------|
| 1 problem/day Mon–Sat | Skip because "exam time" — rd contains 5 min/day works |
| Watch → code yourself → run | Copy-paste from video |
| Ask for hint after 40 min stuck | Look at solution immediately |
| Finish ONE course fully | 3 half-done courses |
| Push to GitHub daily | Losing all your code to a dead laptop |
| Keep the daily log | "I'll remember it later" |

---

## Result after Day 1-2
You have: all 10 tools working, all 10 accounts, your first GitHub push, a notes folder, and a winning habit. That's the hardest week done — everything from here is just showing up daily.

**Next:** `02_DAILY_ROUTINE.md` to know exactly what happens at which hour for 2 years.