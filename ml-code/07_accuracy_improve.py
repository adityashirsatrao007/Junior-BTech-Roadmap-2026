"""
07 — Improving accuracy (the practical toolkit).
Run:  python ml-code/07_accuracy_improve.py   (run 04 + 05 first -> data_clean.pkl)
Shows each technique moving the number, using ONE fixed train/test split so
comparisons are apples-to-apples.
"""
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import numpy as np

df = pd.read_pickle("data_clean.pkl")

# Feature engineering FIRST, then split once, so all models use the same data.
df["family_size"] = df["sibsp"] + df["parch"] + 1
feat = ["pclass", "age", "sibsp", "parch", "fare",
        "sex_male", "embark_town_Queenstown", "embark_town_Southampton", "family_size"]
X, y = df[feat].astype(float), df["survived"]

X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)
results = {}

# 1) start simple
rf = RandomForestClassifier(n_estimators=200, random_state=42)
rf.fit(X_tr, y_tr)
results["RandomForest (start)"] = round(accuracy_score(y_te, rf.predict(X_te)), 3)

# 2) imbalance handling
rf_b = RandomForestClassifier(n_estimators=200, class_weight="balanced", random_state=42)
rf_b.fit(X_tr, y_tr)
results["+ class_weight"] = round(accuracy_score(y_te, rf_b.predict(X_te)), 3)

# 3) stronger algorithm
gb = GradientBoostingClassifier(random_state=42)
gb.fit(X_tr, y_tr)
results["GradientBoosting"] = round(accuracy_score(y_te, gb.predict(X_te)), 3)

# 4) ensemble / voting => average experts
vote = VotingClassifier([
    ("rf", RandomForestClassifier(n_estimators=200, random_state=42)),
    ("gb", GradientBoostingClassifier(random_state=42)),
    ("lr", LogisticRegression(max_iter=1000, random_state=42)),
], voting="soft")
vote.fit(X_tr, y_tr)
results["Soft-voting ensemble"] = round(accuracy_score(y_te, vote.predict(X_te)), 3)

# 5) reliable final estimate via cross-validation on train
cv = cross_val_score(vote, X_tr, y_tr, cv=5, scoring="accuracy")
results["ensemble CV (mean)"] = round(cv.mean(), 3)

print("\n--- accuracy ladder (same fixed test set) ---")
for k, v in results.items():
    print(f"{k:<24}: {v}")
print("\nWhy: better features + stronger model + ensembling beat any silver bullet.")
print("Copy this table into your daily log.")