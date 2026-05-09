import joblib

model = joblib.load("../Models/attrition_model.pkl")

scaler = joblib.load("../Models/scaler.pkl")

feature_columns = joblib.load("../Models/feature_columns.pkl")