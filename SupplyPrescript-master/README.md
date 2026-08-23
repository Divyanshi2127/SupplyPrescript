
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
```

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
```

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


This project is intended for academic and educational purposes.