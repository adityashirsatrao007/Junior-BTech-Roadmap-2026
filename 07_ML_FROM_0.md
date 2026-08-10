# 07 — Machine Learning from ZERO (theory + guided code)

All real, runnable code ships in **`ml-code/`** — read this page for the *why*, then run each script with **`python ml-code/01_env_check.py`**, etc.

No math beyond school level needed to start. You'll go: **concept → tiny code → real dataset → improve accuracy.**

---

## 1. What even is ML? (60 seconds)

Traditional code:
```python
if input == known_rule: answer
```
ML instead: give the computer **examples (data)**, it **learns the rule itself**, then you ask it questions on **new data**.

- **Example:** show a computer 200 photos of "cat" vs "dog" → it learns patterns → you show a new photo → it predicts.
- That's why ML = *"programming with data"*.

Three families (remember with examples):
| Type | Question it answers | Example |
|------|---------------------|---------|
| **Supervised** | "Given X, predict Y" | price prediction (regression), spam/not (classification) |
| **Unsupervised** | "Group similar things" | customer segments, movie recommendations |
| **Reinforcement** | "Which action maximises reward?" | game AI, route planning |

Word map so you're never lost in a video:
- **Dataset** = table of examples. **Features (X)** = inputs. **Label (y)** = the answer column.
- **Training set / Test set** = we learn on one part, check correctness on the hidden part.
- **Model** = the "learned rule" (equation / tree / weights).
- **Accuracy / loss** = how wrong the model is.
- **Overfitting** = model memorised the training data and fails on new data (the #1 trap).

---

## 2. Your learning path (Phases 2 & 3 of the repo)

1. **Python for ML** — NumPy (math on arrays), Pandas (tables), Matplotlib (plots). → `ml-code/02`
2. **Where data lives** — Kaggle datasets → `ml-code/03`
3. **Clean the data** (real data is ugly): missing values, convert text→numbers, scale. → `ml-code/04`
4. **Train your first models**: Linear/Logistic Regression, Decision Tree, Random Forest, KNN. → `ml-code/05`
5. **Tune parameters** (hyperparameters) + evaluate properly (confusion matrix, cross-validation). → `ml-code/05`
6. **Use pretrained models** (transfer learning) for text/image — you don't always need to train from zero. → `ml-code/06`
7. **Improve accuracy** (the kit you'll always reach for). → `ml-code/07`
8. **Ship it**: save/load the model, serve it behind a FastAPI/Flask endpoint, add to your full-stack app.

**FREE courses to follow along:**
- Machine Learning Specialization — Andrew Ng (Coursera, auditable free) | his YouTube lectures
- freeCodeCamp "Machine Learning for Everybody" (YouTube, full)
- Kaggle free micro-courses: Python, Pandas, Intro to ML, Intermediate ML https://kaggle.com/learn
- Krish Naik & campusX (india) YouTube — excellent for placements, sklearn hands-on
- 3Blue1Brown neural network series (YouTube) — the "aha!" for deep learning

---

## 3. Setup

Install (already done on Day 1, verify):
```bash
pip install numpy pandas matplotlib scikit-learn seaborn joblib
# for transfer learning (only if you have space/time):
pip install torch transformers
```
Or just use **Google Colab** — with Kaggle you can also run on Kaggle's free notebooks.

---

## 4. The FULL workflow (memorise this — it's the template for every project)

> AI/DS students: do this whole loop inside **Jupyter** (see `12_AI_DS_TRACK.md` +
> `ds-code/01_jupyter_demo.ipynb`). Notebooks ARE your lab record.

```
1. GET DATA          (Kaggle / API / scraped)         ml-code/03
2. EXPLORE           (shape, nulls, target balance)   ml-code/04
3. CLEAN             (fill/remove missing, encode)    ml-code/04
4. SPLIT             (train/val/test, no leakage)     ml-code/05
5. MODEL             (pick simple first!)             ml-code/05
6. EVALUATE          (accuracy vs confusion vs CV)    ml-code/05
7. IMPROVE           (feature eng, tune, ensemble)    ml-code/07
8. SAVE + SERVE      (pickle/joblib → API endpoint)   ml-code/05/08
```

**Golden rule #1:** always compare against a **baseline** (majority class, or a dumb model). If a fancy model doesn't beat it by much, it's overcomplicated.
**Golden rule #2:** **never touch the test set** to improve the model — improve on the validation split only, or you'll fool yourself.

---

## 5. Datasets to ramp up with (Kaggle or built-in)

1. **Iris** — 150 flowers, 3 species (built into sklearn). First 30 minutes.
2. **Titanic** — survival (offline starter dataset in `data/make_titanic.py`; swap in the real Kaggle `train.csv` anytime). The classic first competition.
3. **Wine quality** — regression + classification practice.
4. **MNIST digits** — image classification, CNNs later.
5. **House prices** (Kaggle) — your first real competition, teaches feature engineering.

Get any of them two ways:
- starter (offline!): `python data/make_titanic.py` → `data/titanic.csv` · `sklearn.datasets.load_iris()`
- Kaggle: create account → "Dataset → Download" → or use the code way in `ml-code/03`.

---

## 6. Hyperparameters vs. learned parameters (interview question)

- **Learned parameters:** the model finds these during training (e.g., the *weights/coefficients* of logistic regression, split points of a tree).
- **Hyperparameters:** you *choose these before* training (e.g., depth of tree, learning rate, number of estimators, K in KNN).
- Finding good hyperparameters = **GridSearchCV / RandomSearchCV** (code in `ml-code/05`).

---

## 7. Improving accuracy — the checklist (use in this order)

1. **Get more / better data** (more rows, fewer bad rows).
2. **Feature engineering** — create new columns that capture real patterns (e.g., family size from SibSp+Parch).
3. **Clean up outliers, fix skew** (log transform).
4. **Scale** features (StandardScaler) for distance-based models.
5. **Class imbalance** — use `class_weight`, resample (SMOTE), or fix thresholds.
6. **Cross-validation** (KFold) instead of one train/test split → reliable numbers.
7. **Better algorithm** — RandomForest/GradientBoosting over a single tree.
8. **Ensemble** — average multiple models (voting).
9. **Tune hyperparameters** (grid/random search).
10. **Regularisation / pruning** when overfitting.

→ All implemented in `ml-code/07_accuracy_improve.py`.

---

## 8. Pretrained models & transfer learning (don't reinvent)

"Training from zero" is rare in real life. Usually you **download a pretrained model** and either use it as-is or fine-tune it on your data.

- Text: **HuggingFace** — `pip install transformers`, then pick a model like `distilbert` or `google-bert`. Sentiment, NER, translation in 5 lines (`ml-code/06`).
- Image: torchvision models (ResNet, EfficientNet) — fine-tune last layers for your custom dataset.
- This is how hackathon projects ship AI in one night.

---

## 9. How to practice (mini-journal)

- Day 1: run `01`→`02`, explain out loud what each line does.
- Day 2: `03`+`04` on Titanic.
- Day 3: `05` full pipeline → write your accuracy in the daily log.
- Day 4: `07` → edit features, re-run, note the accuracy change (this is *real* learning).

---

## 10. DO / DON'T

**DO**
- Start with the **simplest model that could work** (Linear / DecisionTree), then complexity only if needed.
- Log every experiment (model, params, accuracy) — a mini notes table.
- Understand the confusion matrix before reporting just "accuracy".
- Split data *before* any scaling/imputation (avoid leakage).

**DON'T**
- Don't tune hyperparameters on the test set.
- Don't add random features hoping accuracy improves — add features with a reason.
- Don't lie about accuracy in projects — a modest honest score + good reasoning beats inflated numbers in interviews.
- Don't jump into neural networks before you can explain logistic regression.

---

**Resources roundup:** Andrew Ng ML Specialization · freeCodeCamp ML for Everybody · Kaggle Learn · Krish Naik · campusX · statquest (concepts) · sklearn docs https://scikit-learn.org/stable/user_guide.html

**Next:** the code files in `ml-code/`. Start with `01_env_check.py`.