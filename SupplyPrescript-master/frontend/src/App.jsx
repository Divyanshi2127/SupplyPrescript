import { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [scheduledDays, setScheduledDays] = useState(4);
  const [actualDays, setActualDays] = useState(5);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const predictShipment = async () => {
    setLoading(true);
    setResult(null);

    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/predict",
        {
          delivery_days: Number(actualDays),
          scheduled_days: Number(scheduledDays),
          quantity: 2,
          sales: 100,
          discount_rate: 0.1,
          profit_ratio: 0.2,
          product_price: 50,
          shipping_mode: "Standard Class",
          market: "USCA",
          order_region: "West",
          category_name: "Sporting Goods",
          customer_segment: "Consumer",
        }
      );

      const data = response.data;

      const prediction =
        data.prediction ||
        data.result ||
        "Prediction Available";

      const delayed =
        Number(actualDays) > Number(scheduledDays);

      setResult({
        prediction,
        risk: delayed ? "High Risk" : "Low Risk",
        status: delayed
          ? "Delayed Shipment"
          : "On-Time Shipment",
      });
    } catch (error) {
      console.error(error);

      setResult({
        prediction: "Prediction Failed",
        risk: "Unknown",
        status: "Backend Error",
      });
    }

    setLoading(false);
  };

  return (
    <div className="page">
      <div className="container">

        <div className="header">
          <div className="logo">SP</div>

          <h1>SupplyPrescript</h1>

          <p>
            AI-Powered Supply Chain Decision Support System
          </p>
        </div>

        <div className="form">

          <div className="input-group">
            <label>Scheduled Delivery Days</label>

            <input
              type="number"
              min="0"
              max="30"
              value={scheduledDays}
              onChange={(e) =>
                setScheduledDays(e.target.value)
              }
              placeholder="Enter scheduled days"
            />
          </div>

          <div className="input-group">
            <label>Actual Delivered Days</label>

            <input
              type="number"
              min="0"
              max="30"
              value={actualDays}
              onChange={(e) =>
                setActualDays(e.target.value)
              }
              placeholder="Enter actual delivered days"
            />
          </div>

          <button
            onClick={predictShipment}
            disabled={loading}
          >
            {loading
              ? "AI Predicting..."
              : "Predict Shipment Risk"}
          </button>

        </div>

        {result && (
          <div className="results">

            <h2>AI Prediction Result</h2>

            <div className="result-grid">

              <div className="result-card">
                <div className="icon-box blue">
                  ✦
                </div>

                <h3>AI Prediction</h3>
                <p>{result.prediction}</p>
              </div>

              <div className="result-card">
                <div className="icon-box orange">
                  !
                </div>

                <h3>Risk Level</h3>
                <p>{result.risk}</p>
              </div>

              <div className="result-card">
                <div className="icon-box green">
                  ✓
                </div>

                <h3>Shipment Status</h3>
                <p>{result.status}</p>
              </div>

            </div>

          </div>
        )}

      </div>
    </div>
  );
}

export default App;