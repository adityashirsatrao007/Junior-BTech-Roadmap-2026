# 05 — Git & GitHub from Zero (you'll use this every single day)

Git = a tool to **save versions of your code** (like undo history, but team-ready).
GitHub = a website that **hosts those versions** and lets others see/collaborate.

You already ran the Day-1 setup (git installed, identity set, first push done). This file completes the skill.

---

## 1. The 3 concepts that answer 90% of git questions

```
Working folder  --git add-->  Staging  --git commit-->  Local history  --git push-->  GitHub
```

- `git add file` — put a file into the "staging box"
- `git commit -m "msg"` — take a snapshot of the staged files
- `git push` — upload snapshots to GitHub
- `git pull` — download new snapshots from GitHub

---

## 2. Command cheat-sheet (memorise — 15 min)

```bash
git init                       # make a folder a "repository"
git status                     # what's changed? (check this ALL the time)
git add .                      # stage everything (dot = all)
git commit -m "message"        # snapshot
git log --oneline              # history
git push -u origin main        # first upload
git push                       # later uploads
git pull                       # get latest
git branch                     # see branches
git checkout -b feature-1      # create + switch to a branch
git checkout main              # switch branch
git merge feature-1            # merge a branch into current
git clone <url>                # copy a repo from GitHub
git stash                      # temporarily hide uncommitted changes
```

> **Practice:** `git cheat sheet for beginners` on YouTube (freeCodeCamp "Git and GitHub for Beginners" ~1 hr). Then do the mini-project below — that's the real teacher.

---

## 3. Mini-project (must do, ~2 hours)

Build a tiny app (even a text todo-list in plain JS) and:
1. Make a GitHub repo, commit early and often (every 20 min worked).
2. Create a branch `add-feature`, add a feature, merge it back.
3. Write a proper `README.md` (what it does, install, screenshots).
4. Push. Your profile now shows real work.

Rules for commits:
```
feat: add login page
fix: solve merge conflict on main
docs: update README
```
One logical change = one commit. Message says *what*.

---

## 4. Working in teams (hackathon & group projects — YOU WILL NEED THIS)

Golden workflow:
```
1. git pull                     # get fresh main
2. git checkout -b my-task      # your safe island
3. [code code code]
4. git add . && git commit -m "my-task done"
5. git push -u origin my-task
6. open GitHub → Pull Request to main → assign teammate
7. resolve conflicts if any (read the conflict markers <<<<<<< ======= >>>>>>>)
```

Hackathon tip: 1 computer = 1 problem area branch. Never push directly to main in a team.

---

## 5. GitHub profile = your first resume

Make it look like a senior dev:
- ✅ README on your **profile repo** (name = your username): intro, skills, what you're building
- ✅ pinned 3 best projects with READMEs + live demos
- ✅ contribute daily → green streak graph
- ✅ star + fork repos you learned from (shows engagement)
- ❌ no junk repos, no "semester lab work" clutter, no copied projects

This is literally what recruiters look at before your resume.

---

## Resources
- Git & GitHub for Beginners — freeCodeCamp (YouTube)
- Learn Git Branching (interactive game) — https://learngitbranching.js.org
- GitHub Docs — https://docs.github.com/en/get-started
- Pro Git book (free) — https://git-scm.com/book/en/v2

---

## DO / DON'T
- **DO** commit daily, **DON'T** push to main blindly in teams.
- **DO** read conflict markers, **DON'T** `git reset --hard` when scared (use it only when you know).
- **DO** write READMEs, **DON'T** commit secrets/API keys (add `.gitignore`!).

**Next:** with Git in hand, start `06_FULLSTACK.md` (your Phase-1 focus module).