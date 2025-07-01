import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

# Load trained model
model = joblib.load('models/fraud_model.pkl')

st.set_page_config(page_title="Fraud Detector", layout="centered")
st.title("💳 Credit Card Fraud Detection App")

# Let user upload a CSV file
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)

        # Check if it has exactly 30 columns (Time, V1–V28, Amount)
        if df.shape[1] != 30:
            st.error("❌ The file must have exactly 30 columns (Time, V1–V28, Amount)")
        else:
            # Predict
            preds = model.predict(df)
            probs = model.predict_proba(df)[:, 1]

            # Add predictions to the dataframe
            df['Prediction'] = preds
            df['Fraud Probability'] = np.round(probs, 2)
            df['Result'] = df['Prediction'].apply(lambda x: 'Fraud' if x == 1 else 'Legit')

            # Show summary and table
            st.success(f"✅ {len(df)} Transactions Processed")
            st.dataframe(df[['Time', 'Amount', 'Result', 'Fraud Probability']])
    except Exception as e:
        st.error(f"⚠️ Could not read file: {e}")
else:
    st.info("📎 Please upload a CSV file with 30 columns (Time, V1–V28, Amount)")
