# 05 — Git & GitHub: Complete Course from Absolute Zero

Everything about Git + GitHub, from **"I have never touched a terminal"** to working
in teams and contributing to open source. No other resource needed — this is the whole
thing. Read it in order, do the exercises, and you will never be stuck in git again.

> **Time:** ~1 day (chunks), then you use pieces daily forever.

---

## Contents

1. What Git and GitHub actually are
2. Step 1 — Create your GitHub account (from zero)
3. Step 2 — Install Git on Windows (exact clicks)
4. Step 3 — First setup: tell Git who you are
5. Step 4 — Your first file + first commit (the core loop)
6. Step 5 — Put your code on GitHub (push)
7. The complete command reference (all of them explained)
8. README files (make your projects readable)
9. .gitignore (stop committing junk & secrets)
10. Copying someone else's repo (clone)
11. Branches (your safe workspace) + merging
12. Pull Requests — how teams work
13. Forks — contributing to other people's projects
14. Fixing mistakes: undo, revert, reset (safely)
15. Merge conflicts — what they are, how to fix
16. Authentication: PAT vs SSH vs `gh` CLI (pick one)
17. GitHub profile = your resume (set it up right)
18. GitHub Issues & project boards (basic)
19. GitHub Actions (one example, so it's not scary)
20. Common errors + their fixes (FAQ)
21. Mini projects / practice drills
22. Quick reference card (print this)
23. Bonus resources (only if you want more)

---

## 1. What Git and GitHub actually are

Two different things:

- **Git** — a *free program installed on YOUR computer*. It watches a folder ("repo")
  and takes **snapshots** ("commits") whenever you tell it. You can rewind to any
  snapshot forever. Works with zero internet.
- **GitHub** — a *website* that **stores copies** of your repos online. It gives you:
  backups (dead laptop ≠ dead code), sharing, team collaboration, and a **profile
  recruiters actually check**.

Analogy: Git = the save-game system. GitHub = the cloud-save server where your
team's saves live.

The whole course is 7 commands, used in one loop:

```
write code → git add → git commit → git push → (repeat)  ...and git pull before you start
```

---

## 2. Step 1 — Create your GitHub account (from zero)

1. Open your browser → go to **https://github.com/signup**
2. Enter an **email** you check daily → **Set a password** (make it strong) → **Continue**.
3. Pick a **username** — this becomes your public identity. Rules:
   - Professional: `aditya-dev`, `itsaditya`, `adityacodes` (NOT `gamer_rockstar_007`).
   - Same username across GitHub/LeetCode/LinkedIn looks pro.
   - All lowercase, no spaces.
4. Complete the **puzzle** (they check you're human).
5. Check your email → click the **verification link** GitHub sends.
6. Choose **Free plan** (skip Pro — Free is all you need).

**First 10 minutes after signing up:**
- Click your avatar (top-right) → **Settings → Profile**: add name, location, a short
  bio ("BTech CSE | Building with code"), and a photo. Recruiters click profiles with faces.
- Email **verified**? → you get the green "Verified" badge on pushes. Set it in:
  **Settings → Emails → Add email → verify**.
- Optional: turn **2FA** on (**Settings → Password and authentication**). Not required
  for classes, strongly recommended later.

You now have an account. Git (the program) isn't there yet — Step 3 installs it.

---

## 3. Step 2 — Install Git on Windows (exact clicks)

1. Go to **https://git-scm.com/download/win** → click the big **64-bit** download
   (looks like `Git-2.xx.x-64-bit.exe`).
2. Double-click the downloaded file → **Next** through the wizard, **except** these screens:
   - **"Adjusting your PATH"** → choose **"Git from the command line and also from 3rd-party software"** (this one is *required*).
   - **"Choosing HTTPS transport backend"** → leave **"Use the OpenSSL library"** (default).
   - **"Line ending conversions"** → leave **"Checkout Windows-style, commit Unix-style"** (default).
   - Everything else → **Next** → **Install** → **Finish**.
3. **Verify it worked:**
   - Press `Win` → type `cmd` → open Command Prompt → type:
     ✓ `git --version` → prints something like `git version 2.47.0`
4. Install **GitHub Desktop** (optional but great for first week):
   https://desktop.github.com → it's a visual Git that does the same things. Use Desktop
   for the first 2 weeks to *see* what git does, then switch to terminal (faster).

> **If "git is not recognized":** you missed the PATH option. Uninstall, reinstall,
> and this time choose the "third-party software" PATH option. Or use **Git Bash**
> (a terminal that comes with Git — search "Git Bash" in the start menu and use that).

---

## 4. Step 3 — First setup: tell Git who you are

Git stamps every commit with a name. Do this **once, ever** (commands run in
Git Bash / cmd / VS Code terminal):

```bash
git config --global user.name "Your Full Name"
git config --global user.email "your.email@example.com"
```

- `--global` = applies to every project (don't make commits without it).
- Use **the same email as your GitHub account** — this is how GitHub links commits to you.
- Check it worked:
  ```bash
  git config --global --list
  ```
- Change your default editor (optional): VS Code users run
  `git config --global core.editor "code --wait"`.

**Why 99% of beginners get "You don't have any commits yet":** their git email ≠ GitHub
email. Set them equal right now and it never happens.

---

## 5. Step 4 — The core loop (create file → commit)

Open a terminal (in VS Code: top menu **Terminal → New Terminal**, bottom panel opens).

**A. Make your project folder & turn it into a repo:**

```bash
mkdir my-first-repo
cd my-first-repo
git init
```

- `mkdir` = make directory, `cd` = change into it.
- `git init` = "make this folder a Git repo". Run it ONCE per project.
- A hidden `.git` folder now lives there — it holds all history. **Never delete it.**

**B. Create a file** (`my-first-repo/index.html`):
- Open VS Code → **File → Open Folder** → pick `my-first-repo`.
- Click the new-file icon, name it `index.html`, paste anything (a heading, a paragraph).
- Save (`Ctrl+S`).

**C. Check what git sees:**

```bash
git status
```

Shows `index.html` as **untracked** (red / "U") — git knows it exists but isn't tracking it.

**D. Stage it:**

```bash
git add index.html
```

File moves to the **staging area** (green / "A"). Staging = "I want THIS version
in my next snapshot". Check with `git status` again.

**E. Commit it (take the snapshot):**

```bash
git commit -m "add my first html page"
```

- `-m` = message. **Always** write what changed. 3 rules:
  `feat:` new feature · `fix:` a bug · `docs:` readme/docs changes.
- Example: `commit -m "feat: add login form"`.

**F. See history:**

```bash
git log --oneline
```

Prints your commits newest-first. That's it — the core loop:

```
edit → git status (look) → git add <files> → git commit -m "msg" → repeat
```

**Exercise:** make 3 commits (edit the file, commit; add a CSS file, commit; add a JS
file, commit). Stretch: `git log` should show 3 snapshots you can rewind to.

---

## 6. Step 5 — Put your code on GitHub (push)

Now upload the repo so it exists online:

1. Go to **https://github.com/new** — create a new repository:
   - **Repository name:** same as your folder: `my-first-repo`
   - **Description:** one line (e.g. "My first website")
   - **Public** (Public = free unlimited, visible to everyone — good for your portfolio)
   - **Do NOT** tick "Add a README" yet (we already made files; ticking it causes a conflict we'll see in §15).
   - Click **Create repository**.
2. GitHub shows a blank page with three "push an existing repository" commands.
   Copy-paste these **into your project folder's terminal** (where you ran `git init`):

```bash
git remote add origin https://github.com/YOUR-USERNAME/my-first-repo.git
git branch -M main
git push -u origin main
```

Explanation:
- `git remote add origin <url>` — "remember that GitHub repo is called `origin`" (once).
- `git branch -M main` — rename the default branch to `main` (modern standard, once).
- `git push -u origin main` — upload commits. `-u` remembers this URL for next time (once).

3. **Refresh github.com** → your files are online! 🎉
4. From now on, saving to GitHub is just two commands:

```bash
git add .
git commit -m "what changed"
git push
```

> `.` means "all files". Never type files one-by-one again unless you want to split commits.

---

## 7. The complete command reference (every command, explained)

Master these — ~95% of all git usage:

| Command | What it does | When |
|---|---|---|
| `git init` | turn current folder into a repo | once per project |
| `git status` | show changed/staged files | **all the time** |
| `git add .` | stage all changes | before commit |
| `git add file.py` | stage one file | before commit |
| `git commit -m "msg"` | snapshot staged changes | after add |
| `git log --oneline` | list commit history | check history |
| `git push` | upload commits to GitHub | end of a work session |
| `git pull` | download others' commits from GitHub | **start of every session** |
| `git clone <url>` | copy a GitHub repo to your PC | joining existing work |
| `git branch` | list branches (a `*` = current) | check |
| `git branch <name>` | create branch | new feature |
| `git switch`, `git switch -c <name>` | switch branch / create+switch | before branching work |
| `git merge <branch>` | merge that branch into the current one | finishing a feature |
| `git stash` | temporarily hide uncommitted changes (get them back with `git stash pop`) | "my work is messy, pull first" |
| `git diff` | show exact line changes (unstaged) | review before commit |
| `git diff --staged` | show staged changes | review before commit |
| `git remote -v` | show linked GitHub URLs | check where you push |
| `git fetch` | download changes WITHOUT merging (safer pull) | advanced teams |

**The golden workflows:**

```bash
# START a work session (do this first!)
git pull                    # get everyone's latest
git status                  # see where you are
```
```bash
# END a work session (do this last!)
git add .
git commit -m "feat: finished X"
git push
```

---

## 8. README files (make projects readable)

A `README.md` at the top of a repo is the **front page** GitHub shows. Every repo needs one.

Minimal template (plain text + Markdown):

```markdown
# Project name

One line: what it does.

## Features
- Feature one
- Feature two

## How to run
1. Install X
2. Run `npm start`

## Tech
HTML, CSS, JavaScript

## Screenshots
![title](images/demo.png)
```

- Markdown cheat-sheet: `#` headings, `**bold**`, `-` lists, `[text](url)` links, `` `code` ``,
  ``` ``` code block ``` ``` (3 backticks).
- Git commit message = the *what*; README = the *why + how*. Both are part of the grade.

---

## 9. .gitignore (stop committing junk & secrets)

A `.gitignore` file tells git "never track these". **Every repo gets one on day one.**

Create `.gitignore` in your project root (VS Code → new file → name it `.gitignore`).

```gitignore
# system & editor junk
.DS_Store
Thumbs.db
node_modules/

# python
__pycache__/
*.pyc
.env            # ← SECRETS: API keys, passwords (NEVER commit these!)

# build output
dist/
build/
*.log
```

- `node_modules/` is the #1 ignored folder (hundreds of MB of dependencies).
- **Never ever commit `.env`**, API keys, passwords, tokens. If you leaked one:
  rotate it on the website immediately (keys in git history are hunted by bots in minutes).
- After creating it: `git add .gitignore && git commit -m "docs: add gitignore"`.

GitHub even auto-suggests a `.gitignore` when you create a repo (the dropdown shows
language templates such as `Python`, `Node`).

---

## 10. Copying someone else's repo (clone)

To work on any public repo on your machine:

```bash
git clone https://github.com/USER/REPO-NAME.git
cd REPO-NAME
```

- Downloads the *entire* history + files.
- `git clone` already linked the remote for you — you can `git pull`/`git push` immediately.
- To *update* your copy later: `git pull` (it fetches + merges).
- **Clone ≠ Fork** (see §13): clone = your local copy; fork = a copy under *your own GitHub account*.

---

## 11. Branches (safe workspace) + merging

Purpose: work on a new feature **without breaking the working version** on `main`.

```bash
git switch -c add-navbar     # create branch "add-navbar" + move to it
# ... write code ...
git add . && git commit -m "feat: add navbar"
git push -u origin add-navbar   # first push of this branch

git switch main              # go back to main
git pull                     # make main fresh
git merge add-navbar        # bring the feature in
git push                     # publish merged main
```

Rules:
- `main` itself should stay **always deployable** — never break it.
- One feature/bug = one short-lived branch. Delete branches you're done with (web UI: the
  branch page → trash icon) to keep the repo tidy.
- Branch names commute into feature descriptions automatically — great for PRs (§12).

---

## 12. Pull Requests — how teams work

A Pull Request (PR) is **"please merge MY branch into main"** — with discussion, review,
and automatic conflict warnings. This is how every real team ships code.

**From your terminal:**
1. `git switch -c my-task` → `git commit` → `git push -u origin my-task`
2. GitHub shows a yellow **"Compare & pull request"** banner on your fork/repo page → click it.

**On GitHub (if the banner is gone):**
1. Open **Pull requests → New pull request**.
2. `base: main` (the target) ← `compare: my-task` (your branch).
3. Click **Create pull request** → fill title (`feat: …`) + description (what/why/how).
4. Click **Create pull request** again.

**The team loop:**
```
me:   pull → branch → code → commit → push → open PR
them: review → comment "change X" → approve
me:   (fix comments, commit, push — the PR updates automatically)
me:   click "Merge pull request" → "Delete branch"
```

- The PR is **the record** of your work — recruiters click into merged PRs.
- Write 2–4 lines describing the change; it forces you to understand your own code.

---

## 13. Forks — contributing to OTHER people's projects

When you don't have write-access to a repo (99% of repos), you **fork** it:

1. Go to any GitHub repo → top-right button **Fork** → creates a copy under *your* account.
2. `git clone https://github.com/YOUR-USERNAME/REPO.git` → your fork is now local.
3. Add the *original* repo as a second remote (standard name `upstream`):
   ```bash
   git remote add upstream https://github.com/ORIGINAL-OWNER/REPO.git
   ```
4. Branch → code → commit → push to YOUR fork (`origin`).
5. Go to **your fork on GitHub → Pull requests → New pull request** → the banner usually
   says **"compare across forks"** — create the PR into the original repo.
6. Maintainer reviews/merges. This is exactly how open-source contributions (and your
   GitHub contribution graph) really start.
7. Keep your fork updated with the original:
   ```bash
   git fetch upstream
   git switch main
   git merge upstream/main
   git push
   ```

---

## 14. Fixing mistakes: undo, revert, reset (safely)

**Mis-staged a file?**
```bash
git restore --staged file.txt    # un-stage it (keep changes in working folder)
```
Equivalent older command: `git reset HEAD file.txt`.

**Changed files but want the last committed version back?**
```bash
git restore file.txt             # CAREFUL: permanently deletes those edits
```

**Committed a typo / forgot a file — fix the LAST commit:**
```bash
git add . && git commit --amend -m "new, correct message"
```
- Only amend if you haven't pushed yet. If already pushed to a shared branch: don't amend, make a new commit.

**Undo a commit but KEEP the code changes (kind, safe):**
```bash
git reset --soft HEAD~1          # "un-commit" the last one, files stay edited
```

**Delete the last commit AND its changes (dangerous — history rewritten):**
```bash
git reset --hard HEAD~1          # ONLY on code you can re-download / don't care about
```

**Older commit pushed to GitHub — roll it back with a NEW commit (team-safe):**
```bash
git revert <commit-id>           # creates an inverse commit; history stays clean
```

Rule of thumb: **before push** use `reset`/`amend` freely; **after push** use `revert` or new commits.
Never `--hard` on repo you can't restore.

---

## 15. Merge conflicts — what they are, how to fix

**Cause:** you and someone else changed the SAME lines, and git can't guess which version wins.

**What you'll see when it happens** (merge or during `git pull`):
```
CONFLICT (content): Merge conflict in index.html
Automatic merge failed; fix conflicts and then commit the result.
```

Open that file — git drew markers:
```html
<<<<<<< HEAD
my version of the line
=======
their version of the line
>>>>>>> their-branch
```

**Fix procedure (this is normal, happens daily in teams):**
1. Read both sides (`HEAD` = yours, `=======` to `>>>>>>>` = theirs).
2. Decide what the line should actually be → **delete the markers** `<<<<<<<`, `=======`,
   `>>>>>>>` and keep the correct content.
3. Save the file.
4. If using VS Code, conflict markers are color-coded with **"Accept Current / Accept Incoming"** buttons — click them, then hit save.
5. `git add <file>` → `git commit -m "fix: resolve merge conflict"`.
6. `git push`.

You cannot push until unresolved conflicts are fixed (git/VS Code will show them).
Got scared mid-conflict? `git merge --abort` puts everything back to before the merge.

---

## 16. Authentication: PAT vs SSH vs gh CLI (pick ONE)

GitHub needs to know pushes are *you*. Three ways — **do the gh CLI one, it's easiest**:

**Option A — `gh` CLI (recommended for students):**
```bash
# install: https://cli.github.com → run installer/manager, restart terminal
gh auth login
```
- Arrow → **GitHub.com** → HTTPS → **Login with a web browser** → press Enter → a code
  appears → confirm in the browser → done. Pushes just work after this.

**Option B — Personal Access Token (PAT) with HTTPS:**
1. GitHub → **Settings → Developer settings → Personal access tokens → Tokens (classic)**
   → **Generate new token (classic)**.
2. Skip the note, tick **`repo`** (full control of private repos; `repo` covers public too)
   → Generate → **copy the token NOW** (shown once!).
3. On first push, git asks for password → **paste the token** (not your GitHub password).
   Git remembers it from then on (Windows Credential Manager).
   If it asks again later, update the stored credential → **Settings > Credential Manager** on Windows, edit `git:https://github.com`.

**Option C — SSH key (advanced, most secure):**
```bash
ssh-keygen -t ed25519 -C "your.email@example.com"      # press Enter x3
cat ~/.ssh/id_ed25519.pub                                # copy output
```
→ GitHub **Settings → SSH and GPG keys → New SSH key** → paste → Add.
Then use SSH URLs (git@github.com:USER/REPO.git) when adding remotes.

Authentication flow after setup:
```bash
git clone https://github.com/USER/REPO.git      # easy
git push -u origin main                          # will prompt once, then remember
```

---

## 17. GitHub profile = your resume (set it up right)

Recruiters and mentors open your GitHub before your resume. Make it look like a dev:

1. **Profile repo (name = your username):** create a repo named exactly your username,
   tick "Add a README", and write an intro README — who you are, skills, what you're building.
   It renders at the top of your profile page.
2. **Pin 3 best projects** (Profile → Customize your pins → pick the 3 you're proudest of).
3. **Every pinned project** needs: a README, a screenshot/demo link, and a `.gitignore`.
4. **Green streak:** commit every single day (even one line) — GitHub builds a grid graph.
   Recruiters scan the graph for consistency, not brilliance.
5. **Star and fork** repos you learn from — it shows taste and curiosity.
6. **Delete junk:** no "lab experiment1", no copies of tutorials. Quality over quantity.

---

## 18. GitHub Issues & project boards (basic)

**Issues** = bug reports / feature to-do's living in a repo (**Issues → New issue**).
- Teams scatter tasks as issues; PRs reference them: `Fixes #12` (auto-closes the issue on merge).
- Your own projects: write 3 issues for next week's tasks, then complete them.

**Project boards** (Projects tab) = kanban columns `To do / In progress / Done`.
- Drag issues/PRs across as you work. Minimum setup: 3 columns, your top tasks.

This is exactly how hackathon teams and open-source maintainers stay sane.

---

## 19. GitHub Actions (one example, so it's not scary)

Actions = free "robots" that run tasks when code changes (e.g. auto-run your tests).
You'll *use* them later in Full Stack/ML; for now just know the shape.

Example `.github/workflows/check.yml` that checks Python syntax on every push:

```yaml
name: check
on: [push]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: '3.12' }
      - run: python src/main.py --check
```

- File goes in `.github/workflows/`. Push it → GitHub runs it automatically.
- **Actions → your repo tab** shows each run + green/red result.
- If your repo ever runs an "X failed" check, click the run → see the log → fix → push.

---

## 20. Common errors + fixes (FAQ)

| Error | Meaning | Fix |
|---|---|---|
| `fatal: not a git repository` | not in a repo folder | `cd` into the project (where `git init`/`clone`) happened |
| `git` is not recognized | PATH problem | reinstall git choosing the PATH option, or use Git Bash |
| `Please tell me who you are` | no user.name/email yet | run the two `git config --global` commands (§4) |
| `You don't have any commits yet` on profile | git email ≠ GitHub email | match them (§4), the next push fixes it |
| `Authentication failed` | wrong credentials/token | run `gh auth login` or re-paste PAT (§16) |
| `remote: Repository not found` | wrong URL or private repo you can't see | check the URL; `git remote -v` |
| `fatal: The current branch has no upstream branch` | first push needs `-u` | `git push -u origin main` (or your branch name) |
| `error: failed to push some refs` | your main is behind theirs | `git pull` first, fix conflicts (§15), then push |
| `CONFLICT ...` | both changed same lines | fix markers → `add` → `commit` (§15) |
| `Changes not staged for commit` | you forgot `git add` | `git add .` then commit |
| `Your branch is ahead of 'origin/main'` | local commits not pushed yet | `git push` |
| `git commit` opened vim (stuck) | no `-m` given for first time | type `:q!` + Enter to quit; always use `-m "msg"` |
| Messed up badly | you want a clean undo | `git reflog` shows every past position; or `git reset --hard <id>` (§14) |
| `Please make sure you have the correct access rights` (ssh) | bad SSH key | regenerate/add key (§16-C) |

---

## 21. Mini projects / practice drills

**Drill 1 — The daily loop (5 min/day for a week)**
Pick any small project (a notes page, a to-do list). Make **at least 1 commit every day**.
Rules: `git status` before, meaningful commit message, `git push` at the end.

**Drill 2 — Branch & merge (30 min)**
1. `git init` a fresh repo, commit a base `index.html`.
2. `git switch -c add-style` → add a `style.css` and link it → commit → `git switch main`.
3. `git merge add-style` → push. You just did the full branching workflow.
4. Repeat with a 2nd branch that edits the SAME file line as main → force a conflict → fix it (§15).

**Drill 3 — The GitHub portfolio (1 hour)**
A. Create your **profile repo** (§17). B. Put 3 real projects on GitHub with READMEs.
C. Pin them. **This is now your public resume.**

**Drill 4 — Contribute to ANY public repo (2 hours, optional but gold)**
Pick a beginner-friendly repo (search GitHub for `good first issue`), fork it (§13),
fix one typo/issue in a branch, open a PR. Even a README typo fix is a merged PR
on your record — and recruiters *love* seeing 10+ merged PRs.

---

## 22. Quick reference card (print this)

```bash
git config --global user.name  "Name"        # once per machine
git config --global user.email "you@x.com"   # MUST match GitHub email

# daily
git status               # what's changed?
git add .                # stage everything
git commit -m "msg"      # snapshot
git push                 # upload
git pull                 # download others' latest (do this BEFORE you start)

# branching
git switch -c feature    # new branch + go there
git switch main          # go back
git merge feature        # merge feature into the current branch

# undo
git restore file         # discard edits (careful)
git restore --staged f   # unstage
git commit --amend -m x  # fix last commit (before push)
git reset --soft HEAD~1  # un-commit, keep edits

# sharing
git clone <url>          # copy a repo down
git remote -v            # show linked URLs
```

---

## 23. Bonus resources (only if you want more — NOT required)

- GitHub's own beginner docs (free): https://docs.github.com/en/get-started
- Interactive *game* for branches: https://learngitbranching.js.org
- Full book, free, every command: https://git-scm.com/book/en/v2
- Cheat sheet PDF (official Git): https://training.github.com/downloads/github-git-cheat-sheet.pdf
- GitHub Desktop (visual Git, good for week 1): https://desktop.github.com

---

## Next steps

Git is your **daily habit now** — commit every day, push every day (your streak is your
proof of work). With this in hand, continue to `06_FULLSTACK.md` (Phase-1 focus module).
The Day-1 checklist already covered the first push in `01_GETTING_STARTED.md`.