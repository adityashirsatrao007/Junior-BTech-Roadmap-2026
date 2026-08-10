"""
09 — House Prices (your SECOND end-to-end ML project: REGRESSION).
Run (from repo root):
    python data/make_house_prices.py   # once
    python ml-code/09_house_prices.py

What's new vs Titanic (05):
  1. Predicting a NUMBER (price) -> regression metrics (RMSE, MAE, R2), not accuracy
  2. Real missing values in numeric AND categorical columns
  3. Log-transform the target (standard trick in price prediction)
  4. Cross-validation on the final model BEFORE committing to it
Goal: beat the baseline; then improve with ml-code/07 ideas (log features, interactions).
"""
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import Ridge
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib

df = pd.read_csv("data/houses.csv")
print("houses:", df.shape)

y = df["SalePrice"]
X = df.drop(columns=["SalePrice"])

num_cols = X.select_dtypes(include=np.number).columns.tolist()
cat_cols = X.select_dtypes(include="object").columns.tolist()
print("num cols:", num_cols, "| cat cols:", cat_cols, "| nulls total:", int(X.isnull().sum().sum()))

# log-transform target (makes prices closer to Gaussian -> better RMSE)
y_log = np.log1p(y)

# pipelines*: impute missing -> scale numerics; impute strings -> one-hot
num_pl = Pipeline([("impute", SimpleImputer(strategy="median")), ("scale", StandardScaler())])
cat_pl = Pipeline([("impute", SimpleImputer(strategy="most_frequent")),
                   ("onehot", OneHotEncoder(handle_unknown="ignore", sparse_output=False))])

pre = ColumnTransformer([("num", num_pl, num_cols), ("cat", cat_pl, cat_cols)])
Xf = pre.fit_transform(X)

Xtr, Xte, ytr, yte = train_test_split(Xf, y_log, test_size=0.2, random_state=1)
print("train:", Xtr.shape[0], "test:", Xte.shape[0])

# baseline: predict the median of log-price
base = np.full_like(yte, np.median(ytr))
rmse_base = float(np.sqrt(mean_squared_error(yte, base)))
print(f"baseline RMSE (median-guess): {rmse_base:.4f}")

ridge = Ridge(alpha=10)
ridge.fit(Xtr, ytr)
ypred = ridge.predict(Xte)
rmse = float(np.sqrt(mean_squared_error(yte, ypred)))
mae  = float(mean_absolute_error(yte, ypred))
r2   = float(r2_score(yte, ypred))
print(f"Ridge            RMSE {rmse:.4f} | MAE {mae:.4f} | R2 {r2:.4f}")

rf = RandomForestRegressor(n_estimators=200, random_state=1)
rf.fit(Xtr, ytr)
ypred2 = rf.predict(Xte)
rmse2 = float(np.sqrt(mean_squared_error(yte, ypred2)))
print(f"RandomForest     RMSE {rmse2:.4f} | R2  {r2_score(yte, ypred2):.4f}")

cv = cross_val_score(rf, Xf, y_log, cv=5, scoring="neg_root_mean_squared_error")
print(f"RF cross-val RMSE: {-cv.mean():.4f} +- {cv.std():.4f}")

# final model + reload demo
joblib.dump(rf, "houses_model.joblib")
m = joblib.load("houses_model.joblib")
sample = Xf[-1].reshape(1, -1)
price_pred = float(np.expm1(m.predict(sample)[0]))
print("reload ok | sample raw prediction: ₹{:.0f} (log->exp)".format(price_pred))

print("\nImprove next (ml-code/07 kit): add log(features), room*area interaction, or a Ridge+RF blend.")