import streamlit as st
import pandas as pd
import joblib
from textblob import TextBlob

model = joblib.load("/content/churn_model.pkl")

st.title("Telco Customer Churn Prediction App")
st.write("This app predicts whether a telecom customer is likely to churn.")

gender = st.selectbox("Gender", ["Female", "Male"])
SeniorCitizen = st.selectbox("Senior Citizen", [0, 1])
Partner = st.selectbox("Partner", ["Yes", "No"])
Dependents = st.selectbox("Dependents", ["Yes", "No"])
tenure = st.number_input("Tenure", min_value=0, max_value=100, value=12)
PhoneService = st.selectbox("Phone Service", ["Yes", "No"])
MultipleLines = st.selectbox(
    "Multiple Lines",
    ["No", "Yes", "No phone service"]
)
InternetService = st.selectbox(
    "Internet Service",
    ["DSL", "Fiber optic", "No"]
)
OnlineSecurity = st.selectbox(
    "Online Security",
    ["No", "Yes", "No internet service"]
)
OnlineBackup = st.selectbox(
    "Online Backup",
    ["Yes", "No", "No internet service"]
)
DeviceProtection = st.selectbox(
    "Device Protection",
    ["No", "Yes", "No internet service"]
)
TechSupport = st.selectbox(
    "Tech Support",
    ["No", "Yes", "No internet service"]
)
StreamingTV = st.selectbox(
    "Streaming TV",
    ["No", "Yes", "No internet service"]
)
StreamingMovies = st.selectbox(
    "Streaming Movies",
    ["No", "Yes", "No internet service"]
)
Contract = st.selectbox(
    "Contract",
    ["Month-to-month", "One year", "Two year"]
)
PaperlessBilling = st.selectbox("Paperless Billing", ["Yes", "No"])
PaymentMethod = st.selectbox(
    "Payment Method",
    [
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]
)
MonthlyCharges = st.number_input(
    "Monthly Charges",
    min_value=0.0,
    value=70.0
)
TotalCharges = st.number_input(
    "Total Charges",
    min_value=0.0,
    value=1000.0
)

CustomerFeedback = st.text_area("Customer Feedback")


def get_sentiment(text):
    analysis = TextBlob(str(text))

    if analysis.sentiment.polarity > 0:
        return "Positive"
    elif analysis.sentiment.polarity < 0:
        return "Negative"
    else:
        return "Neutral"


if st.button("Predict Churn"):
    Sentiment = get_sentiment(CustomerFeedback)
    ReviewLength = len(str(CustomerFeedback))

    input_data = pd.DataFrame({
        "gender": [gender],
        "SeniorCitizen": [SeniorCitizen],
        "Partner": [Partner],
        "Dependents": [Dependents],
        "tenure": [tenure],
        "PhoneService": [PhoneService],
        "MultipleLines": [MultipleLines],
        "InternetService": [InternetService],
        "OnlineSecurity": [OnlineSecurity],
        "OnlineBackup": [OnlineBackup],
        "DeviceProtection": [DeviceProtection],
        "TechSupport": [TechSupport],
        "StreamingTV": [StreamingTV],
        "StreamingMovies": [StreamingMovies],
        "Contract": [Contract],
        "PaperlessBilling": [PaperlessBilling],
        "PaymentMethod": [PaymentMethod],
        "MonthlyCharges": [MonthlyCharges],
        "TotalCharges": [TotalCharges],
        "ReviewLength": [ReviewLength],
        "Sentiment": [Sentiment]
    })

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    st.subheader("Prediction Result")

    if prediction == 1:
        st.error("Customer is likely to churn.")
    else:
        st.success("Customer is not likely to churn.")

    st.write(
        "Churn Probability:",
        round(probability * 100, 2),
        "%"
    )
    st.write("Customer Sentiment:", Sentiment)
