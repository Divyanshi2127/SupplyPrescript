import joblib
import os
import pandas as pd


MODEL_PATH = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "models",
    "Best_model.pkl"
)

model = joblib.load(MODEL_PATH)


def predict_shipment(
    delivery_days,
    scheduled_days,
    quantity,
    sales,
    discount_rate,
    profit_ratio,
    product_price,
    shipping_mode,
    market,
    order_region,
    category_name,
    customer_segment
):

    data = pd.DataFrame([{
        "Days for shipping (real)": delivery_days,
        "Days for shipment (scheduled)": scheduled_days,
        "Order Item Quantity": quantity,
        "Sales": sales,
        "Order Item Discount Rate": discount_rate,
        "Order Item Profit Ratio": profit_ratio,
        "Product Price": product_price,
        "Shipping Mode": shipping_mode,
        "Market": market,
        "Order Region": order_region,
        "Category Name": category_name,
        "Customer Segment": customer_segment
    }])

    prediction = model.predict(data)[0]

    if int(prediction) == 1:
        return "Delayed Shipment", "High"
    else:
        return "On-Time Shipment", "Low"