# 12 — AI & Data Science Track: everything an AI/DS student needs

For **AI & DS** students only. (General CSE students: keep ML on `07_ML_FROM_0.md`.)

Three career lanes — pick yours, but the first 6 months are identical.

| Lane | Daily work | Interview focus | Landing |
|------|-----------|-----------------|---------|
| Data Analyst | SQL, Excel, dashboards, Power BI | SQL + statistics + 1 dashboard portfol | TCS/Wipro data teams, finance |
| Data Scientist | EDA, models, business decisions | ML theory + stats + 2 projects deep | product/data companies |
| ML / DL Engineer | modeling, training, MLOps | DL theory + PyTorch + deployment | AI startups |

---

## 1. Your tool stack

**Local (Windows — installed via `00_SETUP_WINDOWS.md`):**
- **Jupyter / JupyterLab** — interactive notebooks. Start: `ds-code/01_jupyter_demo.ipynb` → then `ds-code/02_stats_viz.ipynb` (statistics + seaborn, run 01 first)
- **Python itself** — **never coded before?** first do `01_PYTHON_FROM_ZERO.md` + run `ml-code/00_python_first.py` (5-day ramp). Everything here assumes you've done that.
- Python: pandas, numpy, matplotlib, seaborn, scikit-learn, joblib
- VS Code (opening a `.ipynb` gives you a full notebook editor)

**Cloud (free, for heavy/DL work — zero install):**
- **Google Colab** → <https://colab.research.google.com> — free GPU/TPU in the browser. Upload a notebook + `data/titanic.csv`, run online. Perfect when college PCs have no GPU.
- **Kaggle Notebooks** → <https://www.kaggle.com/code> — free GPU + pre-loaded datasets (titanic, iris, house prices).

**How to start Jupyter on Windows (3 ways):**
1. VS Code → open `ds-code/` folder → open `01_jupyter_demo.ipynb` → pick Python kernel.
2. Terminal: `jupyter lab` → browser opens → click the notebook. `Ctrl+C` stops it.
3. Anaconda Prompt: `jupyter notebook` (if you installed Anaconda).

> Notebooks ARE your lab record — commit them to GitHub.

---

## 2. The math you cannot skip

Interviews WILL ask "explain p-value" or "what is a gradient".

| Topic | Why | Free course |
|-------|-----|-------------|
| Statistics (mean/median, distributions, z-score, p-value, correlation) | #1 interview block | freeCodeCamp "Statistics" + Khan Academy |
| Probability (Bayes, expectation) | Naive Bayes, metrics | 3Blue1Brown Probability + Khan |
| Linear algebra (vectors, matrices, dot product) | numpy, embeddings | **3Blue1Brown "Essence of Linear Algebra"** |
| Calculus-lite (derivatives, gradient) | gradient descent | 3Blue1Brown "Essence of Calculus" |

Order: statistics → probability → linear algebra → calculus-lite. 90 min/day, then solve GFG math MCQs.

---

## 3. WHERE to learn ML (pick ONE path, do not hoard courses)

1. **Kaggle Learn** → <https://www.kaggle.com/learn> — free 2–4h micro-courses, real datasets. **Start here.** Do: Python → Intro to ML → Intermediate ML → Data Viz.
2. **Andrew Ng / DeepLearning.AI "Machine Learning Specialization"** (Coursera) — the classic; audit videos free.
3. **Google ML Crash Course** → <https://developers.google.com/machine-learning/crash-course> — free.
4. **fast.ai** → <https://course.fast.ai/> — learn-by-building, free.
5. Your **local base**: `07_ML_FROM_0.md` + `ml-code/` scripts — theory lands here.

**Deep learning** (after sklearn feels easy): Andrew Ng *Deep Learning Specialization* (audit) or fast.ai; then the PyTorch 60-min intro → <https://pytorch.org/tutorials/beginner/deep_learning_60min_blitz.html>. DL needs a GPU → use Colab free.

---

## 4. The project pipeline (memorize — it's your interview answer)

```
1 PROBLEM   what are we predicting? (survival / price / churn)
2 GET DATA  Kaggle / CSV / API             (ml-code 03)
3 EXPLORE   shape, nulls, target balance   (Jupyter + ml-code 04)
4 CLEAN     fill missing, encode, scale    (ml-code 04)
5 SPLIT     train/val/test, no leakage     (ml-code 05)
6 MODEL     simple first: LogisticRegression → RandomForest (ml-code 05)
7 EVALUATE  accuracy + confusion matrix + CV (ml-code 05)
8 IMPROVE   features, tuning, ensembles    (ml-code 07)
9 SHARE     GitHub README + one plot + numbers
```

`01_jupyter_demo.ipynb` walks steps 1–3 visually; `ml-code/04`–`07` complete 4–8.

---

## 5. Datasets & practice (all free)

- Kaggle: Titanic, Iris, House Prices, Heart Disease (easy → real)
- Dataset hub: <https://www.kaggle.com/datasets>
- Indian data: <https://data.gov.in>
- Interview practice: **StrataScratch** → <https://www.stratascratch.com> (real DS questions, free tier); LeetCode + HackerRank Python; GFG stats/math quizzes.

---

## 6. Deep learning in one page

- sklearn owns tabular/structured data ~90% of the time. Go DL for **images, text, audio**, or when a job asks for PyTorch.
- Tools: **PyTorch** (industry/research) or Keras/TensorFlow (friendlier).
- First DL project: MNIST classifier (~40 lines) → then fine-tune a **HuggingFace** model (see `ml-code/06`).

---

## 7. The 3 portfolio projects that make you hireable (months 3–12)

1. **Titanic → House Prices** (tuned ensemble — beats just-following-the-tutorial).
2. **End-to-end dashboard** (pandas → matplotlib/Power BI → notebook on GitHub) = Data Analyst showcase.
3. **One DL project** (image classification or sentiment — reuse `ml-code/06`).

AI/DS ready = SQL (`04`) + statistics (section 2) + these 3 projects + GitHub profile.

---

## 8. Certifications that carry weight (free / audit)

1. Google Data Analytics Professional Certificate (analyst signal).
2. Google Advanced Data Analytics (stronger ML intro).
3. Kaggle Learn course certs (proof of practice).
4. IBM Data Science Professional Certificate (interview-friendly, audit videos free).
5. Microsoft Azure AI / Data Fundamentals (if you touch cloud).

Free certs link into `10_RESUME_CERTS_INTERN.md` — put the ones you finished on the resume.

---

## 9. AI/DS weekly rhythm (on top of the base clock)

- Keep base `02` schedule.
- Add: **math 60 min** on Sunday; **Jupyter lab habit** every evening module; **1 Kaggle notebook/week** from month 6; **read 1 "Kaggle winning solution" writeup/month**.

**Next after setup:** run `ds-code/01_jupyter_demo.ipynb`, then `ml-code/03→07` in order. That is your first week of real DS work.