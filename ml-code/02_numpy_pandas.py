"""
02 — NumPy + Pandas crash intro (ML's building blocks).
Run:  python ml-code/02_numpy_pandas.py
"""
import numpy as np
import pandas as pd

# ---- NumPy: math on arrays (fast) ----
arr = np.array([1, 2, 3, 4, 5])
print("mean:", arr.mean(), "sum:", arr.sum(), "square:", arr ** 2)

rng = np.random.default_rng(0)
mat = rng.integers(0, 10, size=(3, 3))  # 3x3 matrix (Generator uses 'integers')
print("matrix:\n", mat, "\nrow sum:", mat.sum(axis=1), "col sum:", mat.sum(axis=0))

# ---- Pandas: tables (DataFrame) ----
df = pd.DataFrame({
    "name":  ["ana", "bob", "carl", "dave"],
    "age":   [22, 25, np.nan, 30],      # one missing value!
    "score": [90, 55, 77, 63],
})
print("\n--- data ---"); print(df)
print("\n--- shape/null/describe ---")
print("shape:", df.shape, "| nulls:\n", df.isnull().sum())
print(df.describe())

# ---- pandas + numpy together (the daily pattern in real ML) ----
df["age"].fillna(df["age"].median(), inplace=True)   # fill missing with median
df["passed"] = (df["score"] >= 65).astype(int)        # make a label column
print("\n--- cleaned & labelled ---"); print(df)

print("\nHint: DataFrames come from pandas, arrays from numpy. Both are everywhere in ML.")