# 00 — Install EVERYTHING (Windows): step-by-step, nothing broken

All students are on **Windows**. Follow in order. Every section ends with a **"check"**
command — run it in a NEW terminal window, because PATH changes only apply to
newly-opened windows. Official links only (verified reachable). If a download page
looks empty in a browser, refresh it — do NOT grab installers from random sites.

**Rule of the whole session:** after installing, close every terminal/cmd window and
open a fresh one before testing. This fixes 80% of "Command not recognized" panic.

---

## 0. Understand PATH first (this solves everything later)

Windows needs to know **where** your software's executable files live. PATH is a
list of folders it searches whenever you type a command like `python` or `java`.

**Where you change it (once per tool):**
1. Press `Win` → type **environment variables** → hit Enter (or run `sysdm.cpl`).
2. **Environment Variables…** →
3. Under **User variables** → click **Path** → **Edit…** → **New** → paste the folder → **OK**.
4. Close & reopen terminals. Done.

If `xyz` is not recognized → either it's not in PATH, or install didn't finish. Both
are fixable in 60 seconds. Commands that finish with output = success.

---

## 1. Visual Studio Code (your main editor)

1. Download: <https://code.visualstudio.com/download> → **Windows User Installer (64-bit)**
2. Run the installer: accept defaults, but tick **[x] Add to PATH** when asked.
3. Open VS Code → **Extensions** tab (Ctrl+Shift+X) and install:
   - **Python** (Microsoft) · **Pylance** (comes with Python ext)
   - **Prettier** — code formatter
   - **GitLens** — see Git history inline
   - **Live Server** — for HTML/CSS practice
4. Check: `code --version` → should print a version number.

---

## 2. Git for Windows (version control — see `05_GIT_GITHUB.md`)

1. Download: <https://git-scm.com/download/win> → **64-bit for Windows Setup**
2. Run installer, accept defaults **except**: finish **SELECTING COMPONENTS** → tick
   **[x] Git Bash Here** and **[x] Git GUI Here** if not ticked; leave editor = VSCode
   if asked; keep the rest default.
3. Check: open **Git Bash** (right-click desktop → Git Bash Here) → `git --version`.
4. Set your identity (your GitHub username/email from `01_GETTING_STARTED.md`):
   ```bash
   git config --global user.name  "adityashirsatrao007"
   git config --global user.email "your-email@example.com"
   ```

---

## 3. Python 3.12+ (the single most important install)

1. Download: <https://www.python.org/downloads/> → **Download Python 3.12.x / 3.13.x**
2. Run the installer. **CRITICAL: tick the box at the bottom:**
   `[x] Add python.exe to PATH` — this is what makes `python` work everywhere.
3. Click **Install Now** (default location is fine). Let it finish.
4. Check (new terminal):
   ```
   python --version
   pip --version
   ```
   If `python` fails but `py` works, run `py -m ensurepip` and use `py` — and set
   PATH manually (section 0). If you installed with the checkbox ticked it will work.

> `pip` = Python's package installer. If `pip` isn't found, use `python -m pip …`.

---

## 4. Java (JDK 21 LTS — needed for DSA practice and Android path)

Use **Adoptium Temurin** (free, open-source, the build most companies use).

1. Download: <https://adoptium.net/temurin/releases/> → choose **21** → **Windows x64** →
   download the **.msi** installer.
2. Run the .msi: accept defaults. It sets `JAVA_HOME` and PATH **automatically**.
3. Check:
   ```
   java -version
   javac -version
   echo %JAVA_HOME%
   ```
4. If `JAVA_HOME` is empty, set it via section 0:
   - New variable `JAVA_HOME` = `C:\Program Files\Eclipse Adoptium\jdk-21.0.x\`
   - Add `%JAVA_HOME%\bin` to user PATH.

---

## 5. Node.js + npm (for Full Stack — `06_FULLSTACK.md`)

1. Download: <https://nodejs.org/en/download> → **LTS** version → **Windows Installer (.msi)**
2. Run installer, add defaults. **Check [x] Add to PATH** is enabled (default yes).
3. Check: `node --version` and `npm --version`.

---

## 6. MongoDB (NoSQL database — used in the Full Stack project) + MongoDB Compass

1. Download: <https://www.mongodb.com/try/download/community> →
   version **latest**, Platform **Windows**, Package **MSI**.
2. Run the installer → choose **Complete** setup → tick
   `[x] Install MongoDB as a Windows Service` (check in the options page) →
   also tick `[x] Install MongoDB Compass` (graphical browser for the DB).
3. Add MongoDB to PATH manually (section 0): add `C:\Program Files\MongoDB\Server\8.0\bin`
   (folder name = your installed version — check in that directory).
4. Create the database folder (MongoDB needs it):
   - `Win`+`R` → `cmd` → run: `mkdir C:\data\db`
5. Check — the `mongod` service auto-starts from boot now; test the shell:
   ```
   mongosh --version       # the new shell
   ```
   If `mongosh` is missing, open **MongoDB Compass** once and connect to
   `mongodb://localhost:27017` — that proves the server is running.
6. When you run the full-stack project: wherever code says `mongodb://localhost:27017`
   it will just work.

---

## 7. MySQL (relational DB — used with SQL practice and backend projects) + Workbench

1. Download: <https://dev.mysql.com/downloads/installer/> → **MySQL Installer for Windows**
   (pick the ~400 MB "web" or full one — if the page seems empty, refresh; it uses
   bot-protection for scripts but works in a normal browser).
2. Run installer → **Developer Default** → it will auto-install **MySQL Server** +
   **MySQL Workbench** + Connectors.
3. During setup it asks for a **root password** — make one you won't forget (e.g.
   `root123` for dev). Write it in your setup notes. Same password for re-confirm.
4. Tick `[x] Add MySQL Server to Windows PATH` when offered (in the server-settings
   step) — skip this step if you'll rely on Workbench.
5. Check:
   ```
   mysql --version
   ```
   Then open **MySQL Workbench** → connect "Local instance MySQL80" with your root
   password → run `SELECT VERSION();` — a result = success.

---

## 8. PostgreSQL + pgAdmin (bonus DB — many companies use it, costs nothing)

1. Download: <https://www.postgresql.org/download/windows/> → **Interactive installer by EDB**.
2. Run it → keep the port **5432 default**, set a `postgres` superuser password you
   remember, and let it install **pgAdmin 4**.
3. Check: `psql --version` (new terminal). Open pgAdmin → connect to `localhost`.

---

## 9. Postman (test your APIs — you'll use it in the Full Stack phase)

1. Download: <https://www.postman.com/downloads/> → **Windows 64-bit**.
2. Install. Open → you can skip login to try it, but create a free account for
   saving collections.
3. No PATH needed — it's a GUI. Open it when your API routes need testing.

---

## 10. Android Studio (only when you reach `08_MOBILE_DEV.md` — install LATER)

1. Download: <https://developer.android.com/studio> → **Download Android Studio**.
2. It installs the Android SDK + emulator for you. Requires ~8 GB free disk — do this
   only in Phase P2/P3, and it's optional if you choose Flutter/React-Native
   from `08_MOBILE_DEV.md`.

---

## 11. FINAL VERIFY — open a new terminal and run all of these

Browser works → copy this block into cmd / PowerShell (Windows):

```
python --version
pip --version
java -version
node --version
npm --version
git --version
code --version
mongosh --version
mysql --version
psql --version
```

**Every line prints a version = everything is installed. Done — you're ready for `01_GETTING_STARTED.md` Day 1.**

---

## 13. AI & DS students: Jupyter + Notebooks (bonus for `12_AI_DS_TRACK.md`)

Notebooks = the DS/ML home base. Two ways to run them:

**Option A (easiest, no extra install):** VS Code already installed → open a `.ipynb`
file, pick the **Python 3.x** kernel (top-right), done. Open `ds-code/01_jupyter_demo.ipynb`.

**Option B — full JupyterLab:**
```
python -m pip install ipykernel jupyterlab
jupyter lab            # opens in your browser
```
Stop it with `Ctrl+C` in the terminal. Optionally install **Anaconda** (formerdefault
for DS) from <https://www.anaconda.com/download> — but plain `pip` + VS Code is
lighter and just as good.

Check it works: opening a notebook and running a cell prints a result (e.g. `2+2` → `4`).

---

## 14. Common errors + fixes (copy-paste this section to whoever panics)

| You see | Cause | Fix |
|---|---|---|
| `'python' is not recognized` | Python not in PATH | Reinstall with checkbox ticked, or add path manually (section 0) |
| `'pip' is not recognized` | pip not on PATH | Use `python -m pip install <pkg>` |
| `'java' is not recognized` | JAVA_HOME wrong | Set `JAVA_HOME` + add `%JAVA_HOME%\bin` (section 0) |
| `'mongosh' is not recognized` | MongoDB bin not in PATH | Add `C:\Program Files\MongoDB\Server\<ver>\bin` to PATH |
| `Error: connect ECONNREFUSED 127.0.0.1:27017` | MongoDB service stopped | Start **MongoDB** service → services.msc → MongoDB → Start; or run `net start MongoDB` |
| `ERROR 1045 Access denied` | Wrong MySQL password | Re-run installer → reconfigure → set root password you remember |
| Terminal still says "not recognized" after installing | Bad terminal | Close ALL terminals, open a new one — PATH only loads in new windows |
| Installer says "Windows protected your PC" | SmartScreen on unknown exe | App is official → click **More info** → **Run anyway** |

**Next:** after this block passes, your Day 1 setup is done — go to `01_GETTING_STARTED.md`
(accounts + GitHub setup + smoke tests), then start Day 1 DSA in `03_LEETCODE_150.md`.