from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import joblib
import os
import json
from fluvio import Fluvio
from config import MODEL_DIR, FLUVIO_TOPIC

app = FastAPI()

# Load model and preprocessing artifacts
model = joblib.load(os.path.join(MODEL_DIR, "xgb_fraud_model.pkl"))
label_encoders = joblib.load(os.path.join(MODEL_DIR, "label_encoders.pkl"))
feature_columns = joblib.load(os.path.join(MODEL_DIR, "feature_columns.pkl"))

with open(os.path.join(MODEL_DIR, "best_threshold.txt")) as f:
    best_threshold = float(f.read().strip())

# Connect to Fluvio
fluvio = Fluvio.connect()
producer = fluvio.topic_producer(FLUVIO_TOPIC)

# Define transaction input schema
class Transaction(BaseModel):
    Amount: float
    SenderLocation: str
    ReceiverLocation: str
    IsFlaggedBefore: bool
    DeviceType: str
    MerchantCategory: str
    DeviceChange: bool
    TransactionGap: int
    IsAmountUsualForUser: bool
    txn_id: str

@app.post("/predict")
def predict(transaction: Transaction):
    df = pd.DataFrame([transaction.dict()])

    # Label encode categorical features
    for col, le in label_encoders.items():
        if col in df.columns:
            try:
                df[col] = le.transform(df[col])
            except Exception as e:
                raise HTTPException(400, f"Encoding error in '{col}': {df[col].iloc[0]}")

    df = df[feature_columns]
    df = df.apply(pd.to_numeric, errors="coerce")

    # Predict fraud probability
    prob = model.predict_proba(df)[0][1]
    prediction = int(prob >= best_threshold)

    # Send transaction to Fluvio stream
    producer.send("", json.dumps(transaction.dict()).encode('utf-8'))

    return {
        "txn_id": transaction.txn_id,
        "prediction": prediction,
        "probability": round(prob, 4),
        "threshold": best_threshold
    }
