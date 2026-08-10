"""
03 — Get a real dataset (works offline).
Run:  python data/make_titanic.py   (once) -> creates data/titanic.csv
      python ml-code/03_get_data.py
Also: how to pull the REAL Titanic dataset from Kaggle later.
"""
import pandas as pd

df = pd.read_csv("data/titanic.csv")
print("Titanic shape:", df.shape)
print(df.head(3).to_string())

# ---- The Kaggle way (for the REAL dataset later) ----
# kaggle.com -> sign in -> 'titanic' competition -> Data tab -> Download
# put train.csv into data/ then:  df = pd.read_csv("data/train.csv")

print("\nMissing values:")
print(df.isnull().sum()[df.isnull().sum() > 0])
print("\nSurvived counts (0 = died, 1 = survived):")
print(df["survived"].value_counts())