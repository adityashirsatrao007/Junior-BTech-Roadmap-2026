"""
data/make_titanic.py — build the OFFLINE starter dataset (no internet needed).
Run:  python data/make_titanic.py  -> creates data/titanic.csv
WHY: seaborn's load_dataset('titanic') downloads from the internet, which can
block college wifi / offline labs. This generates a *schema-identical* dataset so
all ml-code exercises work offline. Replace with Kaggle's real train.csv anytime —
the columns are the same.
"""
import os
import numpy as np
import pandas as pd

rng = np.random.default_rng(42)
N = 891

pclass = rng.choice([1, 2, 3], size=N, p=[0.24, 0.21, 0.55])
sex = rng.choice(["male", "female"], size=N, p=[0.65, 0.35])
age = np.round(np.clip(rng.normal(29, 14, N), 0.5, 80), 1)
sibsp = rng.choice([0, 1, 2, 3], size=N, p=[0.68, 0.24, 0.06, 0.02])
parch = rng.choice([0, 1, 2], size=N, p=[0.76, 0.13, 0.11])
# fare correlated with class, always > 0
fare = np.round(np.where(pclass == 1, rng.uniform(40, 260, N),
        np.where(pclass == 2, rng.uniform(12, 60, N), rng.uniform(5, 30, N))), 2)
embark_town = rng.choice(["Cherbourg", "Queenstown", "Southampton"], size=N, p=[0.19, 0.09, 0.72])

# survival is NOT random — it depends on features (so students can learn real patterns)
prob = np.zeros(N)
prob += np.where(np.array(sex) == "female", 0.72, 0.36)          # women survived more
prob += np.where(np.array(pclass) == 1, 0.22, np.where(np.array(pclass) == 2, 0.05, -0.12))
prob += (age - 29) / 120.0
prob = np.clip(prob, 0.03, 0.97)
survived = (rng.random(N) < prob).astype(int)

df = pd.DataFrame({
    "survived": survived,
    "pclass": pclass,
    "sex": sex,
    "age": age,
    "sibsp": sibsp,
    "parch": parch,
    "fare": fare,
    "embark_town": embark_town,
})

os.makedirs("data", exist_ok=True)
df.to_csv("data/titanic.csv", index=False)
print("wrote data/titanic.csv", df.shape, "| survived rate:", round(df.survived.mean(), 3))