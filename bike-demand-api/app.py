import joblib
from fastapi import FastAPI
from pydantic import BaseModel, Field

from train import FEATURES, MODEL_PATH

app = FastAPI(title="Bike Rental Demand API")
model = joblib.load(MODEL_PATH)


class RentalInput(BaseModel):
    temperature_c: float = Field(ge=0, le=40)
    hour: int = Field(ge=0, le=23)
    weekend: bool
    raining: bool


@app.get("/")
def home():
    return {"message": "Bike Rental Demand API is running", "docs": "/docs"}


@app.post("/predict")
def predict(data: RentalInput):
    features = [[getattr(data, name) for name in FEATURES]]
    return {"predicted_rentals": round(float(model.predict(features)[0]))}
