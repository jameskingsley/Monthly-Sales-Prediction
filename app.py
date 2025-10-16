

import streamlit as st
import mlflow.pyfunc
import pandas as pd
import os
from datetime import datetime
import plotly.express as px
import mlflow

# ---------------- MLflow Configuration ----------------
# Set local MLflow tracking URI
mlflow.set_tracking_uri("http://127.0.0.1:5000")

# Load the model 
MODEL_URI = "models:/Monthly_Sales_Model/1"  
model = mlflow.pyfunc.load_model(MODEL_URI)

# ---------------- Streamlit Page Setup ----------------
st.set_page_config(
    page_title="📊 Monthly Sales Prediction",
    page_icon="📈",
    layout="wide",
)

# Header
st.title("Monthly Sales Prediction Dashboard")
st.markdown("""
Welcome to the **Monthly Sales Forecasting App**!  
Predict upcoming sales based on recent months’ performance.  
Model powered by **MLflow** and **Random Forest**.
""")

# ---------------- Input Section ----------------
st.subheader("🧮 Enter Prediction Parameters")

col1, col2, col3 = st.columns(3)
with col1:
    year = st.number_input("Year", min_value=2000, max_value=2100, step=1, value=2025)
    lag_1 = st.number_input("Previous Month Sales (lag_1)", min_value=0.0, step=1000.0)
with col2:
    month = st.number_input("Month", min_value=1, max_value=12, step=1, value=10)
    lag_2 = st.number_input("Sales 2 Months Ago (lag_2)", min_value=0.0, step=1000.0)
with col3:
    lag_3 = st.number_input("Sales 3 Months Ago (lag_3)", min_value=0.0, step=1000.0)

# ---------------- Prediction Logic ----------------
if st.button("Predict Sales"):
    # Prepare input for model
    input_data = pd.DataFrame({
        'Year': [year],
        'Month': [month],
        'lag_1': [lag_1],
        'lag_2': [lag_2],
        'lag_3': [lag_3]
    })
    
    # Predict
    prediction = model.predict(input_data)[0]
    st.success(f"### Predicted Sales: {prediction:,.2f}")

    # Save Prediction to History
    history_file = "prediction_history.csv"
    new_entry = pd.DataFrame({
        'Date': [datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
        'Year': [year],
        'Month': [month],
        'lag_1': [lag_1],
        'lag_2': [lag_2],
        'lag_3': [lag_3],
        'Predicted_Sales': [prediction]
    })

    if os.path.exists(history_file):
        history = pd.read_csv(history_file)
        history = pd.concat([history, new_entry], ignore_index=True)
    else:
        history = new_entry
    history.to_csv(history_file, index=False)
    st.success("Prediction saved to history! 💾")

# ---------------- Display History & Visualization ----------------
st.markdown("---")
st.subheader("Prediction History")

if os.path.exists("prediction_history.csv"):
    history = pd.read_csv("prediction_history.csv")
    st.dataframe(history.tail(10), use_container_width=True)

    st.markdown("### Sales Prediction Trend")
    fig = px.line(
        history,
        x="Date",
        y="Predicted_Sales",
        markers=True,
        title="Sales Forecast Over Time",
        labels={"Predicted_Sales": "Predicted Sales", "Date": "Prediction Date"},
    )
    st.plotly_chart(fig, use_container_width=True)
else:
    st.info("No prediction history found. Make a prediction to get started!")

# ---------------- Footer ----------------
st.markdown("---")
st.caption("Powered by MLflow + Streamlit | Built by James Kingsley Philip")
