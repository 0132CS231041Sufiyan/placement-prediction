# 🎓 Placement Prediction using Machine Learning

This project predicts whether a student is likely to be placed based on their **CGPA** and **IQ**.

## 🚀 Project Overview

A Machine Learning model is trained to predict student placement status.  
The trained model is integrated with a **Streamlit web application** where users can enter their CGPA and IQ and get a prediction.

## 🛠️ Technologies Used

- Python
- NumPy
- Pandas
- Scikit-learn
- Streamlit
- Logistic Regression

## 📊 Input Features

- CGPA
- IQ

## 🤖 Machine Learning Model

**Logistic Regression**

The input data is scaled using `StandardScaler` before making predictions.

## 🎯 Model Accuracy

The model achieved approximately **90% accuracy** on the test data.

## 🌐 Streamlit Application

The application provides a simple interface where users can:

1. Enter their CGPA
2. Enter their IQ
3. Click the **Predict** button
4. View the placement prediction
## 📁 Project Structure

```text
placement-prediction/
│
├── app.py
├── model.pkl
├── scaler.pkl
├── placement.csv
├── placement_prediction_project.ipynb
├── requirements.txt
└── README.md
```

## ▶️ How to Run

Install the required libraries:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```
