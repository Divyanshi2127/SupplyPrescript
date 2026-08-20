import os
import joblib
import pandas as pd


# --------------------------------------------------
# PROJECT PATHS
# --------------------------------------------------

BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

MODEL_PATH = os.path.join(
    BASE_DIR,
    "Models",
    "Best_model.pkl"
)


# --------------------------------------------------
# LOAD MODEL
# --------------------------------------------------

model = joblib.load(MODEL_PATH)


# --------------------------------------------------
# EXPECTED FEATURES
# --------------------------------------------------

FEATURES = [
    "Type",
    "Days for shipment (scheduled)",
    "Benefit per order",
    "Sales per customer",
    "Category Name",
    "Customer City",
    "Customer Country",
    "Customer Segment",
    "Customer State",
    "Department Name",
    "Market",
    "Order City",
    "Order Country",
    "Order Item Discount",
    "Order Item Discount Rate",
    "Order Item Product Price",
    "Order Item Profit Ratio",
    "Order Item Quantity",
    "Sales",
    "Order Item Total",
    "Order Profit Per Order",
    "Order Region",
    "Order State",
    "Product Name",
    "Product Price",
    "Product Status",
    "Shipping Mode",
    "Lead_Time",
    "Order_Month",
    "Order_Year",
    "Order_Weekday",
    "Profit_Margin",
    "High_Value_Order"
]


# --------------------------------------------------
# PREDICTION FUNCTION
# --------------------------------------------------

def predict_shipment(features):

    # Convert input dictionary into DataFrame
    input_data = pd.DataFrame([features])

    # Make sure feature order is exactly the same
    input_data = input_data[FEATURES]

    # Prediction
    prediction = model.predict(input_data)[0]

    # Prediction probability
    probability = model.predict_proba(input_data)[0][1]

    # Risk classification
    if probability >= 0.70:
        risk_level = "High Risk"

    elif probability >= 0.40:
        risk_level = "Medium Risk"

    else:
        risk_level = "Low Risk"

    return {
        "prediction": int(prediction),
        "delay_probability": float(probability),
        "risk_level": risk_level
    }