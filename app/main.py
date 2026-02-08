from fastapi import FastAPI, HTTPException
import joblib
import pandas as pd
import os
from .schemas import CustomerData, PredictionResponse

app = FastAPI(title="E-commerce Customer Satisfaction API")

# Setup the path to the model
main_dir = os.path.dirname(__file__)
model_path = os.path.join(main_dir, "models", "full_pipeline.pkl")

# Load the model once
try:
    model = joblib.load(model_path)
except Exception as e:
    model = None
    print(f"CRITICAL: Could not load model from {model_path}. Error: {e}")

@app.get("/")
def read_root():
    return {"status": "API is active", "model_loaded": model is not None}

@app.post("/predict", response_model=PredictionResponse)
def predict_satisfaction(data: CustomerData):
    if model is None:
        raise HTTPException(status_code=500, detail="Model file missing on server.")

    try:
        # the schema map for mapping the josn data to datafame for our model its our bridge 
        input_dict = {
            "Gender": data.gender,
            "Age": data.age,
            "City": data.city,
            "Membership Type": data.membership_type,
            "Total Spend": data.total_spend,
            "Items Purchased": data.items_purchased,
            "Average Rating": data.average_rating,
            "Discount Applied": data.discount_applied,
            "Days Since Last Purchase": data.days_since_last_purchase
        }

        # convert to DataFrame
        input_df = pd.DataFrame([input_dict])

        # the predict process 
        raw_prediction = model.predict(input_df)[0]
        prediction_text = str(raw_prediction)
        
        # get Probability
        probabilities = model.predict_proba(input_df)[0]
        max_prob = float(max(probabilities))

        #  here are the great trick -- sending a discount coupon if unsatisfied
        alert_level = "Normal"
        action = "Maintain current service level."

        if "Unsatisfied" in prediction_text:
            alert_level = "Critical"
            action = "Urgent: Send 20% discount coupon and trigger support call."
        elif "Neutral" in prediction_text:
            alert_level = "Medium"
            action = "Send customer feedback survey and 5% discount."

        return {
            "satisfaction_score": prediction_text,
            "probability": round(max_prob, 2),
            "alert_level": alert_level,
            "action_required": action
        }

    except Exception as e:
        # Returns the exact error for debugging (will show in Swagger UI)
        raise HTTPException(status_code=500, detail=f"Prediction Error: {str(e)}")