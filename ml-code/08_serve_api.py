"""
08 — (Optional) Serve the trained model as an API for your full-stack app.
After running 05 (titanic_model.joblib + titanic_scaler.joblib):

    pip install fastapi uvicorn
    uvicorn 08_serve_api:app --reload      # run from ml-code folder

Open http://127.0.0.1:8000 (Swagger UI) or POST JSON to /predict.
NOTE: file must be 08_serve_api.py (module name in uvicorn).
"""
import joblib
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd

# init errors if model files missing -> run 05 first
model = joblib.load("titanic_model.joblib")
scaler = joblib.load("titanic_scaler.joblib")

app = FastAPI(title="Titanic Survival API")


class Passenger(BaseModel):
    pclass: int
    age: float
    sex_male: int  # 1 = male, 0 = female
    fare: float = 100.0


@app.post("/predict")
def predict(p: Passenger):
    # same 8 features + order the 05 pipeline used
    row = pd.DataFrame([[p.pclass, p.age, 0, 0, p.fare, p.sex_male, 0, 1]],
                       columns=["pclass", "age", "sibsp", "parch", "fare",
                                "sex_male", "embark_town_Queenstown",
                                "embark_town_Southampton"])
    row = scaler.transform(row)
    prob = float(model.predict_proba(row)[0][1])
    return {"survival_probability": round(prob, 3), "survives": prob >= 0.5}