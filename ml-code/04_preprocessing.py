"""
04 — Clean + prep data (the 'data science' 80%).
Run:  python ml-code/04_preprocessing.py
Learn: handle missing, encode text -> numbers, split features X and label y.
"""
import pandas as pd

df = pd.read_csv("data/titanic.csv")
print("before:", df.shape)

# 1) MISSING VALUES
print("\nmissing before:\n", df.isnull().sum()[df.isnull().sum() > 0])
# 'age': fill with median (robust to outliers)
df["age"] = df["age"].fillna(df["age"].median())
# 'embark_town': fill with the mode (most common)
df["embark_town"] = df["embark_town"].fillna(df["embark_town"].mode()[0])
# 'deck': a lot missing -> drop the column (too many holes to trust it)
# our starter schema has no 'deck' column

# 2) CONVERT text -> numbers (models need numbers)
#    one-hot encode 'sex' and 'embark_town'
df = pd.get_dummies(df, columns=["sex", "embark_town"], drop_first=True)
print("after encoding columns:\n", [c for c in df.columns if "sex_" in c or "embark_" in c])

# 3) choose FEATURES (inputs) and LABEL (answer)
features = ["pclass", "age", "sibsp", "parch", "fare", "sex_male", "embark_town_Queenstown", "embark_town_Southampton"]
X = df[features]
y = df["survived"]                      # label
print("\nfeature matrix shape:", X.shape, "labels:", y.value_counts().to_dict())

# Save cleaned data for the next script (same row order as original!)
df.to_pickle("data_clean.pkl")
print("saved clean data -> data_clean.pkl (05 will reload it)")
print("memorise: X = inputs (2D), y = answer (1D). X.shape is (rows, features).")