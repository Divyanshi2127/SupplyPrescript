from predictor import predict_shipment


test_shipment = {

    "Type": 2,
    "Days for shipment (scheduled)": 4,
    "Benefit per order": 23.5,
    "Sales per customer": 50.0,

    "Category Name": 47,
    "Customer City": 66,
    "Customer Country": 1,
    "Customer Segment": 0,
    "Customer State": 36,

    "Department Name": 6,
    "Market": 0,
    "Order City": 66,
    "Order Country": 1,

    "Order Item Discount": 10.0,
    "Order Item Discount Rate": 0.10,
    "Order Item Product Price": 50.0,
    "Order Item Profit Ratio": 0.20,
    "Order Item Quantity": 1,

    "Sales": 50.0,
    "Order Item Total": 45.0,
    "Order Profit Per Order": 10.0,

    "Order Region": 5,
    "Order State": 36,

    "Product Name": 59,
    "Product Price": 50.0,
    "Product Status": 0,

    "Shipping Mode": 3,

    "Lead_Time": 5,
    "Order_Month": 7,
    "Order_Year": 2017,
    "Order_Weekday": 4,

    "Profit_Margin": 0.20,
    "High_Value_Order": 0
}


result = predict_shipment(test_shipment)

print("\nSUPPLYPRESCRIPT PREDICTION")
print("--------------------------")

print("Prediction:", result["prediction"])

print(
    "Delay Probability:",
    f"{result['delay_probability']:.2%}"
)

print("Risk Level:", result["risk_level"])