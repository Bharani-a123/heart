# ❤️ Heart Disease Prediction using Machine Learning

This project uses a machine learning model to predict the likelihood of heart disease based on user-input medical data. It provides a simple web interface built with Flask, where users can enter their information and get real-time predictions.

## 🔍 Overview

Heart disease is a leading cause of death globally. Early prediction and prevention can save lives. This project uses a dataset from Kaggle (Heart Disease UCI) and applies a Random Forest Classifier to detect the presence of heart disease.

## 📁 Project Structure

heart-disease-prediction/
├── model.py # Trains and saves the machine learning model
├── app.py # Flask web app for user input and prediction
├── heart.csv # Heart disease dataset (from Kaggle)
├── templates/
│ └── index.html # Frontend form for user input
├── static/ # (Optional) CSS or images for styling
└── requirements.txt # Required Python libraries


## 🧠 Model Info

- **Algorithm**: Random Forest Classifier
- **Dataset**: Heart Disease UCI from Kaggle
- **Features Used**:
  - Age
  - Sex
  - Chest Pain Type
  - Resting Blood Pressure
  - Cholesterol
  - Fasting Blood Sugar
  - Resting ECG
  - Max Heart Rate
  - Exercise-induced Angina
  - Oldpeak
  - Slope
  - CA (Number of major vessels)
  - Thalassemia

## 🚀 How to Run

### 1. Clone the repo

```bash
git clone https://github.com/your-username/heart-disease-prediction.git
cd heart-disease-prediction
