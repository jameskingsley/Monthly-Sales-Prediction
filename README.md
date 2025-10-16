# Monthly-Sales-Prediction


## Monthly Sales Prediction System

An End-to-End MLOps Project using MLflow and Streamlit

### Project Overview

This project demonstrates the full lifecycle of a machine learning regression model — from training and experiment tracking to deployment in an interactive web app.

The goal is to predict future monthly sales using lag-based historical data, enabling businesses to make informed decisions based on trends and patterns.

### Features

End-to-End ML Lifecycle — Includes data preprocessing, model training, evaluation, versioning, and deployment.
MLflow Integration — Tracks all model runs, parameters, metrics, and artifacts.
Model Registry — Manages multiple versions with “Staging” and “Production” stages.
Streamlit Web App — Interactive prediction dashboard with real-time forecasting and visualization.
Prediction History — Automatically saves and visualizes prediction trends using Plotly.

## Tech Stack
Category	Tools
Language	Python
Frameworks	Streamlit, Scikit-learn
MLOps Tooling	MLflow
Visualization	Plotly
Data Handling	Pandas, NumPy
Environment	pip / virtualenv
Project Structure
Monthly_Sales_Prediction
│
├── app.py                  # Streamlit app for deployment
├── requirements.txt        # Dependencies
├── prediction_history.csv  # Saved predictions
├── mlruns/                 # MLflow tracking folder
└── README.md               # Project documentation

Model Training & Tracking

Models trained: Linear Regression, Random Forest Regressor, Gradient Boosting Regressor

Metrics logged to MLflow (RMSE, MAE, R²)

Best model registered as:
Monthly_Sales_Model → Version 1 → Stage: Production

Example logging snippet:

with mlflow.start_run():
    mlflow.log_param("model_type", "RandomForest")
    mlflow.log_metric("rmse", rmse)
    mlflow.sklearn.log_model(rf_model, "model", registered_model_name="Monthly_Sales_Model")

Streamlit App Workflow

1️⃣ User enters input values: Year, Month, lag_1, lag_2, lag_3
2️⃣ Model (loaded from MLflow Registry) predicts the sales
3️⃣ Prediction is displayed and saved to history
4️⃣ Plotly chart visualizes sales trends over time

▶️ Running the App
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run MLflow server (optional)
mlflow ui --backend-store-uri file:///C:/path/to/mlruns

# 3. Launch the app
streamlit run app.py


👤 James Kingsley Philip
Data Scientist | MLOps Enthusiast | Machine Learning Engineer

Would you like me to also generate a README version with emojis and badges (for GitHub visual appeal) — e.g., with shields like “Built with MLflow”, “Made with Streamlit”, etc.?
It looks great in portfolios.

ChatGPT can make mistakes. Check important info.
