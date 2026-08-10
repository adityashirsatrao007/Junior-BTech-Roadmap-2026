"""
05 — Train, evaluate, tune, save. THE CORE PIPELINE.
Run:  python ml-code/05_train_evaluate_tune.py   (run 04 first -> creates data_clean.pkl)
Learn: split, scaling, baseline, two models, confusion matrix, cross-validation,
       hyperparameter tuning (GridSearchCV), save/load object.
"""
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import joblib

df = pd.read_pickle("data_clean.pkl")
features = ["pclass", "age", "sibsp", "parch", "fare",
            "sex_male", "embark_town_Queenstown", "embark_town_Southampton"]
X, y = df[features], df["survived"]

# 1) split 70/30, stratified so class balance survives the split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y)
print("train:", X_train.shape, "test:", X_test.shape)

# 2) scale features (fit on TRAIN ONLY, then transform test -> no leakage)
scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s = scaler.transform(X_test)

# 3) baseline: predicting always the majority class
baseline = max(y_train.mean(), 1 - y_train.mean())
print("baseline accuracy:", round(baseline, 3))

# 4) two models
log = LogisticRegression(max_iter=1000, random_state=42)
log.fit(X_train_s, y_train)
pred = log.predict(X_test_s)
print("LogisticRegression test accuracy:", round(accuracy_score(y_test, pred), 3))
print("confusion matrix [TN FP; FN TP]:\n", confusion_matrix(y_test, pred))

rf = RandomForestClassifier(n_estimators=200, random_state=42)
rf.fit(X_train, y_train)
print("RandomForest test accuracy:      ", round(accuracy_score(y_test, rf.predict(X_test)), 3))

# 5) cross-validation: reliable score (5 folds)
cv = cross_val_score(rf, X_train, y_train, cv=5, scoring="accuracy")
print("RandomForest CV accuracy:", round(cv.mean(), 3), "+-", round(cv.std(), 3))

# 6) tune hyperparameters with grid search
gs = GridSearchCV(
    RandomForestClassifier(random_state=42),
    {"n_estimators": [50, 200], "max_depth": [None, 6, 10]},
    cv=3, scoring="accuracy", n_jobs=-1)
gs.fit(X_train, y_train)
best = gs.best_estimator_
print("best params:", gs.best_params_)
print("best test accuracy:", round(accuracy_score(y_test, best.predict(X_test)), 3))

# 7) save model + scaler, demo a prediction on a brand-new row
joblib.dump(best, "titanic_model.joblib")
joblib.dump(scaler, "titanic_scaler.joblib")
print("saved titanic_model.joblib + titanic_scaler.joblib")
print("reload with: joblib.load('titanic_model.joblib')")


def predict_new(age, sex_male, pclass):
    row = scaler.transform([[pclass, age, 0, 0, 100.0, sex_male, 0, 1]])
    return round(best.predict_proba(row)[0][1], 3)


print("25yo male, 1st class -> survival prob:", predict_new(25, 1, 1))
print("25yo female, 1st class -> survival prob:", predict_new(25, 0, 1))