<<<<<<< HEAD

# SupplyPrescript: AI-Powered Supply Chain Decision Support System

## Overview

SupplyPrescript is an intelligent supply chain decision support system that goes beyond traditional predictive analytics. Instead of only predicting disruptions, it recommends the optimal business action using mathematical optimization and continuously improves its recommendations through a closed-loop feedback system.

The project integrates Machine Learning, Operations Research, FastAPI, SQL databases, and an interactive dashboard to help logistics managers make cost-effective decisions during supply chain disruptions.

---

## Problem Statement

Traditional predictive analytics can forecast supply chain delays but leave the final decision to human operators.

For example, if a shipment is predicted to be delayed by 14 days, the manager still has to decide whether to:

- Use air freight
- Purchase from another supplier
- Delay production
- Delay product launch

Choosing the wrong option can result in unnecessary costs or operational losses.

SupplyPrescript solves this problem by automatically recommending the mathematically optimal decision while considering business constraints such as budget, delivery deadlines, and supplier capacity.

---

## Project Objectives

- Predict supply chain disruptions using Machine Learning
- Recommend optimal business decisions using Linear Programming
- Allow users to execute decisions directly from the dashboard
- Record operational decisions in the database
- Learn from previous decisions using a closed-loop analytics framework
- Improve future recommendations based on historical outcomes

---

## Key Features

### Predictive Analytics

- Predict shipment delays
- Estimate delay duration
- Calculate disruption probability

Algorithms:
- XGBoost
- LightGBM

---

### Prescriptive Analytics

Generate optimized recommendations such as:

- Air Freight
- Secondary Supplier
- Production Rescheduling
- Product Launch Delay

Optimization Engine:

- PuLP
- SciPy Linear Programming

---

### Closed-Loop Analytics

The system records:

- Selected recommendation
- Actual transportation cost
- Actual delay
- Business outcome

These outcomes are used to continuously improve optimization weights.

---

### Interactive Dashboard

Users can

- View predicted disruptions
- Compare recommended actions
- Execute decisions
- Track historical decisions
- Monitor KPIs

---

## System Architecture

Historical Data
        │
        ▼
Data Cleaning & Feature Engineering
        │
        ▼
Machine Learning Model
        │
        ▼
Delay Prediction
        │
        ▼
Optimization Engine
        │
        ▼
Recommended Actions
        │
        ▼
Interactive Dashboard
        │
        ▼
Manager Decision
        │
        ▼
Operational Database
        │
        ▼
Outcome Evaluation
        │
        ▼
Model Improvement

---

## Tech Stack

### Programming Language

- Python

### Data Processing

- Pandas
- NumPy

### Machine Learning

- XGBoost
- LightGBM
- Scikit-learn

### Optimization

- PuLP
- SciPy

### Backend

- FastAPI
- SQLAlchemy

### Database

- Snowflake (planned)
- SQLite (development)

### Dashboard

- React
or
- Retool
(Streamlit may be used during initial development)

### Visualization

- Plotly
- Matplotlib

---

## Project Structure

```
SupplyPrescript/

│── api/
│── dashboard/
│── data/
│   ├── raw/
│   └── processed/
│
│── docs/
│── models/
│── notebooks/
│── src/
│── tests/
│
│── README.md
│── requirements.txt
│── .gitignore
=======
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
>>>>>>> teammate/main
```

---

<<<<<<< HEAD
## Workflow

1. Collect historical shipment data

2. Clean and preprocess data

3. Perform exploratory data analysis

4. Train Machine Learning model

5. Predict future shipment delays

6. Generate optimized recommendations

7. Display recommendations on dashboard

8. User selects an action

9. Save decision in database

10. Evaluate outcome

11. Update optimization parameters

---

## Expected Input

Examples of features

- Supplier
- Product
- Lead Time
- Transportation Mode
- Warehouse
- Order Quantity
- Manufacturing Time
- Shipping Distance
- Weather Conditions
- Historical Delay
- Inventory Level

---

## Expected Output

Prediction

- Delay Probability
- Expected Delay Duration

Recommendation

- Air Freight
- Secondary Supplier
- Delay Production
- Delay Product Launch

Business Metrics

- Expected Cost
- Expected Savings
- Service Level

---

## Evaluation Metrics

Machine Learning

Classification

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC

Regression

- MAE
- RMSE
- R² Score

Optimization

- Total Cost
- Delivery Time
- Resource Utilization

---

## Future Enhancements

- Reinforcement Learning
- Digital Twin Simulation
- Real-time IoT Integration
- Multi-objective Optimization
- Explainable AI (SHAP)
- Cloud Deployment
- Kubernetes
- Docker
- Automated Retraining Pipeline

---

## Installation

Clone the repository

```bash
git clone https://github.com/yourusername/SupplyPrescript.git
```

Navigate into the project
=======
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
>>>>>>> teammate/main

```bash
cd SupplyPrescript
```

<<<<<<< HEAD
Install dependencies
=======
Install dependencies:
>>>>>>> teammate/main

```bash
pip install -r requirements.txt
```

<<<<<<< HEAD
---

## Current Status

Project Phase: Planning and Architecture Design

Upcoming Milestones

- Dataset Collection
- Data Cleaning
- Exploratory Data Analysis
- Feature Engineering
- Predictive Model Development
- Optimization Engine
- Dashboard Development
- API Integration
- Closed-Loop Analytics
- Deployment

---

## Author

Divyanshi Gusainwal

B.Tech Computer Science Engineering (IoT & IS)

Manipal University Jaipur

---

## License

# SupplyPrescript: AI-Powered Supply Chain Decision Support System

## Overview

SupplyPrescript is an intelligent supply chain decision support system that goes beyond traditional predictive analytics. Instead of only predicting disruptions, it recommends the optimal business action using mathematical optimization and continuously improves its recommendations through a closed-loop feedback system.

The project integrates Machine Learning, Operations Research, FastAPI, SQL databases, and an interactive dashboard to help logistics managers make cost-effective decisions during supply chain disruptions.

---

## Problem Statement

Traditional predictive analytics can forecast supply chain delays but leave the final decision to human operators.

For example, if a shipment is predicted to be delayed by 14 days, the manager still has to decide whether to:

- Use air freight
- Purchase from another supplier
- Delay production
- Delay product launch

Choosing the wrong option can result in unnecessary costs or operational losses.

SupplyPrescript solves this problem by automatically recommending the mathematically optimal decision while considering business constraints such as budget, delivery deadlines, and supplier capacity.

---

## Project Objectives

- Predict supply chain disruptions using Machine Learning
- Recommend optimal business decisions using Linear Programming
- Allow users to execute decisions directly from the dashboard
- Record operational decisions in the database
- Learn from previous decisions using a closed-loop analytics framework
- Improve future recommendations based on historical outcomes

---

## Key Features

### Predictive Analytics

- Predict shipment delays
- Estimate delay duration
- Calculate disruption probability

Algorithms:
- XGBoost
- LightGBM

---

### Prescriptive Analytics

Generate optimized recommendations such as:

- Air Freight
- Secondary Supplier
- Production Rescheduling
- Product Launch Delay

Optimization Engine:

- PuLP
- SciPy Linear Programming

---

### Closed-Loop Analytics

The system records:

- Selected recommendation
- Actual transportation cost
- Actual delay
- Business outcome

These outcomes are used to continuously improve optimization weights.

---

### Interactive Dashboard

Users can

- View predicted disruptions
- Compare recommended actions
- Execute decisions
- Track historical decisions
- Monitor KPIs

---

## System Architecture

Historical Data
        │
        ▼
Data Cleaning & Feature Engineering
        │
        ▼
Machine Learning Model
        │
        ▼
Delay Prediction
        │
        ▼
Optimization Engine
        │
        ▼
Recommended Actions
        │
        ▼
Interactive Dashboard
        │
        ▼
Manager Decision
        │
        ▼
Operational Database
        │
        ▼
Outcome Evaluation
        │
        ▼
Model Improvement

---

## Tech Stack

### Programming Language

- Python

### Data Processing

- Pandas
- NumPy

### Machine Learning

- XGBoost
- LightGBM
- Scikit-learn

### Optimization

- PuLP
- SciPy

### Backend

- FastAPI
- SQLAlchemy

### Database

- Snowflake (planned)
- SQLite (development)

### Dashboard

- React
or
- Retool
(Streamlit may be used during initial development)

### Visualization

- Plotly
- Matplotlib

---

## Project Structure

```
SupplyPrescript/

│── api/
│── dashboard/
│── data/
│   ├── raw/
│   └── processed/
│
│── docs/
│── models/
│── notebooks/
│── src/
│── tests/
│
│── README.md
│── requirements.txt
│── .gitignore
```

---

## Workflow

1. Collect historical shipment data

2. Clean and preprocess data

3. Perform exploratory data analysis

4. Train Machine Learning model

5. Predict future shipment delays

6. Generate optimized recommendations

7. Display recommendations on dashboard

8. User selects an action

9. Save decision in database

10. Evaluate outcome

11. Update optimization parameters

---

## Expected Input

Examples of features

- Supplier
- Product
- Lead Time
- Transportation Mode
- Warehouse
- Order Quantity
- Manufacturing Time
- Shipping Distance
- Weather Conditions
- Historical Delay
- Inventory Level

---

## Expected Output

Prediction

- Delay Probability
- Expected Delay Duration

Recommendation

- Air Freight
- Secondary Supplier
- Delay Production
- Delay Product Launch

Business Metrics

- Expected Cost
- Expected Savings
- Service Level

---

## Evaluation Metrics

Machine Learning

Classification

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC

Regression

- MAE
- RMSE
- R² Score

Optimization

- Total Cost
- Delivery Time
- Resource Utilization

---

## Future Enhancements

- Reinforcement Learning
- Digital Twin Simulation
- Real-time IoT Integration
- Multi-objective Optimization
- Explainable AI (SHAP)
- Cloud Deployment
- Kubernetes
- Docker
- Automated Retraining Pipeline

---

## Installation

Clone the repository

```bash
git clone https://github.com/yourusername/SupplyPrescript.git
```

Navigate into the project

```bash
cd SupplyPrescript
```

Install dependencies

```bash
pip install -r requirements.txt
=======
Run FastAPI:

```bash
uvicorn backend.main:app --reload
```

Start the React frontend:

```bash
cd frontend
npm install
npm start
>>>>>>> teammate/main
```

---

<<<<<<< HEAD
## Current Status

Project Phase: Planning and Architecture Design

Upcoming Milestones

- Dataset Collection
- Data Cleaning
- Exploratory Data Analysis
- Feature Engineering
- Predictive Model Development
- Optimization Engine
- Dashboard Development
- API Integration
- Closed-Loop Analytics
- Deployment

---

## Author

Divyanshi Gusainwal

B.Tech Computer Science Engineering (IoT & IS)

Manipal University Jaipur

---

## License


This project is intended for academic and educational purposes.
=======
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
>>>>>>> teammate/main
