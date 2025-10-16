# Monthly-Sales-Prediction


# Monthly Sales Prediction System

An End-to-End MLOps Project using MLflow, MySQL, and Streamlit

## Project Overview

This project implements a complete MLOps workflow for a monthly sales forecasting model, integrating:

MySQL as the backend tracking database for MLflow,

MLflow for experiment tracking, model registry, and version control, and

Streamlit for web deployment and visualization.

The system predicts monthly sales using lag features derived from historical data, empowering organizations to forecast revenue trends and plan proactively.

## Key Features

*  End-to-End ML Lifecycle – Data preprocessing, model training, tracking, registry, and deployment.
*  MySQL-Backed MLflow Tracking – Logs all experiments, parameters, metrics, and models to a relational database for durability.
*  Model Registry & Versioning – Tracks multiple versions of models and allows seamless promotion to Production.
*  Interactive Streamlit App – Clean dashboard for generating sales predictions and viewing historical results.
*  Forecast Visualization – Historical prediction trends displayed using Plotly charts.

# Tech Stack
* Category	               Tools
* Programming Language	   Python
* Frameworks	            Streamlit, Scikit-learn
* MLOps Tools         	   MLflow, MySQL
* Visualization	         Plotly
* Data Handling	         Pandas, NumPy

##  System Architecture
   ┌──────────────────────┐
   │      Data Input      │
   └──────────┬───────────┘
              │
              ▼
   ┌──────────────────────┐
   │  Model Training &    │
   │  Tracking (MLflow)   │
   └──────────┬───────────┘
              │
     MySQL Backend (for MLflow metadata)
              │
              ▼
   ┌──────────────────────┐
   │  Model Registry      │
   └──────────┬───────────┘
              │
              ▼
   ┌──────────────────────┐
   │  Streamlit App       │
   │ (Prediction + Viz)   │
   └──────────────────────┘

## Project Structure
#### Monthly_Sales_Prediction

*  app.py                  # Streamlit app for deployment
*  requirements.txt        # Dependencies
*  prediction_history.csv  # Saved predictions
*  lruns/                  # MLflow tracking folder
*  README.md               # Project documentation

# How It Works

## Model Training & Logging

Trains models (Linear, RandomForest, GradientBoosting).

Logs params, metrics, and artifacts to MLflow connected to MySQL.

## Model Registry & Promotion

The best model is registered and promoted to Production in MLflow.

## Deployment via Streamlit

The app loads the production model dynamically:
Users enter year, month, and lag sales; the system returns predictions.
Predictions are logged and visualized using Plotly.


