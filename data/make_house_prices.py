"""
data/make_house_prices.py — OFFLINE starter dataset for the House Prices exercise.
Run:  python data/make_house_prices.py  -> creates data/houses.csv
WHY: parallel to titanic (data/make_titanic.py) — no internet needed. Swap in the
real Kaggle 'house-prices-xed' train.csv anytime: columns below match the Ames set.
Surprisingly good for a generated file: true price dependencies + real missing data.
"""
import os
import numpy as np
import pandas as pd

rng = np.random.default_rng(7)
N = 1200

area   = np.round(rng.normal(1500, 700, N), 2)             # sqft
area   = np.clip(area, 350, 5000)
rooms  = rng.choice([2, 3, 3, 4, 4, 5, 6], size=N)
age    = np.clip(rng.normal(40, 30, N), 0, 120).round().astype(int)
bathrooms = rng.choice([1, 1, 2, 2, 2, 3], size=N)
garage = rng.choice([0, 0, 1, 1, 1, 2, 3], size=N)
quality = rng.choice([1, 2, 3, 3, 4, 5, 5, 6], size=N)     # 1..6 overall quality
neighborhood = rng.choice(["OldTown", "College", "SawyerW", "NAmes", "Crawfor"], size=N, p=[.25, .3, .2, .15, .1])

base = 45_000 + area * 65 + quality * 12_000 + rooms * 4_000 + bathrooms * 3_500 + garage * 6_000
noise = rng.normal(0, 15_000, N)
price = (base + noise).round().astype(int)
price = np.clip(price, 25_000, 800_000)

df = pd.DataFrame({
    "SalePrice": price,
    "LotArea":   area.round(0).astype(int),
    "Bedroom":   rooms,
    "FullBath":  bathrooms,
    "GarageCars": garage,
    "YearBuilt": 2024 - age,
    "OverallQual": quality,
    "Neighborhood": neighborhood,
})
# deliberately introduce missing values so students must handle NaN (like the real Ames set)
if True:
    df.loc[rng.random(N) < 0.12, "GarageCars"] = np.nan
    df.loc[rng.random(N) < 0.07, "YearBuilt"] = np.nan

os.makedirs("data", exist_ok=True)
df.to_csv("data/houses.csv", index=False)
print("wrote data/houses.csv", df.shape, "| price mean:", price.mean().round(0))