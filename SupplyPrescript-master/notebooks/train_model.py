import zipfile
import os
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report


# --------------------------------------------------
# 1. Load Dataset
# --------------------------------------------------

ZIP_PATH = "../SupplyChain.csv.zip"
MODEL_PATH = "../models/Best_model.pkl"

with zipfile.ZipFile(ZIP_PATH, "r") as zip_file:
    csv_file = zip_file.namelist()[0]

    with zip_file.open(csv_file) as file:
        df = pd.read_csv(file, encoding="latin1")


print("Dataset loaded successfully!")
print("Shape:", df.shape)


# --------------------------------------------------
# 2. Select Features and Target
# --------------------------------------------------

features = [
    "Days for shipping (real)",
    "Days for shipment (scheduled)",
    "Order Item Quantity",
    "Sales",
    "Order Item Discount Rate",
    "Order Item Profit Ratio",
    "Product Price",
    "Shipping Mode",
    "Market",
    "Order Region",
    "Category Name",
    "Customer Segment"
]

target = "Late_delivery_risk"


X = df[features]
y = df[target]


# --------------------------------------------------
# 3. Identify Column Types
# --------------------------------------------------

numeric_features = [
    "Days for shipping (real)",
    "Days for shipment (scheduled)",
    "Order Item Quantity",
    "Sales",
    "Order Item Discount Rate",
    "Order Item Profit Ratio",
    "Product Price"
]

categorical_features = [
    "Shipping Mode",
    "Market",
    "Order Region",
    "Category Name",
    "Customer Segment"
]


# --------------------------------------------------
# 4. Preprocessing
# --------------------------------------------------

numeric_pipeline = Pipeline(
    steps=[
        ("imputer", SimpleImputer(strategy="median"))
    ]
)

categorical_pipeline = Pipeline(
    steps=[
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OneHotEncoder(handle_unknown="ignore"))
    ]
)


preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_pipeline, numeric_features),
        ("cat", categorical_pipeline, categorical_features)
    ]
)


# --------------------------------------------------
# 5. Model
# --------------------------------------------------

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    n_jobs=-1,
    class_weight="balanced"
)


pipeline = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("model", model)
    ]
)


# --------------------------------------------------
# 6. Train-Test Split
# --------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


print("Training model...")


# --------------------------------------------------
# 7. Train
# --------------------------------------------------

pipeline.fit(X_train, y_train)


# --------------------------------------------------
# 8. Evaluation
# --------------------------------------------------

y_pred = pipeline.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:", round(accuracy * 100, 2), "%")

print("\nClassification Report:")
print(classification_report(y_test, y_pred))


# --------------------------------------------------
# 9. Save Model
# --------------------------------------------------

os.makedirs("../models", exist_ok=True)

joblib.dump(pipeline, MODEL_PATH)

print("\nModel saved successfully!")
print("Location:", MODEL_PATH)