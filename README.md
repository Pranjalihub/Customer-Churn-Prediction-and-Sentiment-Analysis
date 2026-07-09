# Customer-Churn-Prediction-and-Sentiment-Analysis
Telco Customer Churn Prediction and Customer Sentiment Analysis using Machine Learning, TextBlob, and Streamlit for interactive churn prediction.
# 📊 Telco Customer Churn Prediction & Sentiment Analysis

## 📌 Project Overview

Customer churn is one of the biggest challenges for telecom companies. This project predicts whether a customer is likely to leave the telecom service using Machine Learning. It also analyzes customer feedback using Sentiment Analysis to understand customer satisfaction.

The model is deployed as an interactive Streamlit web application that allows users to enter customer information and instantly receive churn predictions.

---

## 🚀 Features

- Customer Churn Prediction
- Customer Feedback Sentiment Analysis
- Interactive Streamlit Web App
- Data Preprocessing using OneHotEncoder
- Logistic Regression Classification
- Confusion Matrix
- Accuracy, Precision, Recall and F1-Score Evaluation
- Beautiful User Interface

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- TextBlob
- Joblib
- Streamlit

---

## 📂 Dataset

The project uses the **Telco Customer Churn Dataset** containing customer demographic information, service usage, billing information, and customer feedback.

---

## 📈 Machine Learning Workflow

1. Load Dataset
2. Data Cleaning
3. Handle Missing Values
4. Convert TotalCharges to Numeric
5. Perform Exploratory Data Analysis (EDA)
6. Sentiment Analysis using TextBlob
7. Feature Engineering
8. One-Hot Encoding of Categorical Variables
9. Train Logistic Regression Model
10. Model Evaluation
11. Save Trained Model
12. Deploy using Streamlit

---

## 📊 Model Evaluation

The model is evaluated using:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

---

## 💻 Streamlit Application

The Streamlit application allows users to:

- Enter customer information
- Enter customer feedback
- Perform sentiment analysis
- Predict customer churn
- View churn probability

## 📁 Project Structure
```
├── app.py
├── churn_model.pkl
├── requirements.txt
├── telco_churn_with_all_feedback.csv
├── README.md
```

---

## ▶️ How to Run

Clone the repository

```bash
git clone <repository-link>
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## 🎯 Future Improvements

- Random Forest Classifier
- XGBoost Classifier
- Hyperparameter Tuning
- Model Comparison Dashboard
- SHAP Explainability
- Customer Retention Recommendation System
- Cloud Deployment

---

## 👩‍💻 Author

**Pranjali Dhoke**

Aspiring Data Scientist | AI & Machine Learning Enthusiast
