from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from backend.predictor import predict_shipment


app = FastAPI(
    title="SupplyPrescript API",
    description="AI-powered supply chain delay prediction and decision support system",
    version="1.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ShipmentInput(BaseModel):
    delivery_days: float
    scheduled_days: float
    quantity: float
    sales: float
    discount_rate: float
    profit_ratio: float
    product_price: float
    shipping_mode: str
    market: str
    order_region: str
    category_name: str
    customer_segment: str


@app.get("/")
def home():
    return {
        "message": "SupplyPrescript Backend Running Successfully!"
    }


@app.get("/health")
def health():
    return {
        "status": "OK"
    }


@app.post("/predict")
def predict(data: ShipmentInput):

    prediction, risk = predict_shipment(
        data.delivery_days,
        data.scheduled_days,
        data.quantity,
        data.sales,
        data.discount_rate,
        data.profit_ratio,
        data.product_price,
        data.shipping_mode,
        data.market,
        data.order_region,
        data.category_name,
        data.customer_segment
    )

    return {
        "prediction": prediction,
        "risk": risk
    }