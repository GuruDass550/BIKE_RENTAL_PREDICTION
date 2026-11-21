import csv
from pathlib import Path

import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

ROOT = Path(__file__).resolve().parent
FEATURES = ("temperature_c", "hour", "weekend", "raining")
MODEL_PATH = ROOT / "bike_model.joblib"


def main():
    with (ROOT / "bike_rentals.csv").open(newline="", encoding="utf-8") as file:
        rows = list(csv.DictReader(file))

    features = [[float(row[name]) for name in FEATURES] for row in rows]
    rentals = [int(row["rentals"]) for row in rows]
    x_train, x_test, y_train, y_test = train_test_split(
        features, rentals, test_size=0.2, random_state=42
    )

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(x_train, y_train)
    error = mean_absolute_error(y_test, model.predict(x_test))
    joblib.dump(model, MODEL_PATH)

    print(f"Held-out MAE: {error:.2f} rentals ({len(y_test)} examples)")
    print(f"Saved {MODEL_PATH.name}")


if __name__ == "__main__":
    main()
