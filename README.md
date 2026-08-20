# 📦 SupplyPrescript – AI-Powered Supply Chain Decision Support System

SupplyPrescript is an end-to-end data analytics and machine learning project designed to help businesses make smarter supply chain decisions. The system predicts product demand, analyzes historical sales patterns, and recommends inventory optimization strategies through an interactive dashboard.

It integrates **Machine Learning, FastAPI, React, and Prescriptive Analytics** into a single decision support platform.

---

## 🚀 Project Overview

Modern supply chains generate massive amounts of sales and inventory data. SupplyPrescript transforms this data into actionable insights by combining predictive and prescriptive analytics.

The project helps organizations:

- Forecast future product demand
- Reduce overstock and stock shortages
- Optimize inventory decisions
- Visualize KPIs through an interactive dashboard
- Deploy prediction services using FastAPI

---

## ✨ Key Features

- 📈 Demand Forecasting using Machine Learning
- 📊 Exploratory Data Analysis (EDA)
- ⚙️ Feature Engineering & Data Preprocessing
- 🧠 Predictive Analytics Models
- 📦 Prescriptive Inventory Optimization
- 🌐 FastAPI REST API Backend
- 💻 React + Material UI Dashboard
- 📉 Interactive Charts & Business KPIs
- 🐳 Docker Deployment Ready

---

## 🛠️ Tech Stack

| Category | Technologies |
|----------|--------------|
| Programming | Python, JavaScript |
| Data Analysis | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn, Plotly |
| Machine Learning | Scikit-learn |
| Backend | FastAPI |
| Frontend | React, Material UI |
| API Testing | Swagger UI |
| Deployment | Docker |
| Version Control | Git & GitHub |

---

## 📂 Project Structure

```text
SupplyPrescript/
│
├── backend/
│   ├── main.py
│   ├── prediction.py
│   ├── optimization.py
│   ├── model_loader.py
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   ├── public/
│   └── package.json
│
├── data/
│   └── SupplyChain.csv
│
├── notebooks/
│   ├── 01_Business_Understanding.ipynb
│   ├── 02_Data_Preprocessing.ipynb
│   ├── 03_Exploratory_Data_Analysis.ipynb
│   ├── 04_Feature_Engineering.ipynb
│   ├── 05_Predictive_Modeling.ipynb
│   ├── 06_Prescriptive_Analytics_Optimization.ipynb
│   ├── 07_FastAPI_Backend.ipynb
│   ├── 08_React_Dashboard.ipynb
│   ├── 09_Deployment.ipynb
│   └── 10_Project_Documentation_and_Portfolio.ipynb
│
├── Dockerfile
├── README.md
└── requirements.txt
```

---

## 📊 Machine Learning Workflow

1. Business Understanding
2. Data Collection
3. Data Cleaning & Preprocessing
4. Exploratory Data Analysis
5. Feature Engineering
6. Model Training
7. Demand Prediction
8. Inventory Optimization
9. API Development
10. Dashboard Visualization

---

## 📷 Dashboard Modules

The React dashboard includes:

- Executive KPI Cards
- Sales Trend Analysis
- Demand Prediction Form
- Inventory Optimization Table
- Interactive Business Charts
- REST API Integration

---

## 🔌 FastAPI Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/` | API Status |
| POST | `/predict` | Predict Product Demand |
| POST | `/optimize` | Generate Inventory Recommendation |
| GET | `/docs` | Swagger Documentation |

---

## 📈 Business Benefits

- Improve forecasting accuracy
- Reduce inventory holding costs
- Prevent stock shortages
- Enable data-driven decision making
- Provide real-time analytics through APIs

---

## 🐳 Docker

Build the application:

```bash
docker build -t supplyprescript .
```

Run the container:

```bash
docker run -p 8000:8000 supplyprescript
```

---

## ▶️ Installation

Clone the repository:

```bash
git clone https://github.com/Tanmayik20/SupplyPrescript.git
```

Move into the project:

```bash
cd SupplyPrescript
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run FastAPI:

```bash
uvicorn backend.main:app --reload
```

Start the React frontend:

```bash
cd frontend
npm install
npm start
```

---

## 📚 Learning Outcomes

This project demonstrates practical knowledge of:

- Data Analytics
- Machine Learning
- Supply Chain Optimization
- FastAPI Development
- React Dashboard Design
- Docker Deployment
- Git & GitHub Collaboration

---

## 👩‍💻 Author

**Tanmayi K**

B.Tech Computer Science Engineering

---

## ⭐ Acknowledgement

This project was developed as a real-world academic and portfolio project to demonstrate end-to-end supply chain analytics using modern data science and full-stack development technologies.