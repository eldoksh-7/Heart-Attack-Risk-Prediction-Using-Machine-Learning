# Heart Attack Risk Prediction Using Machine Learning

## Project Overview

Cardiovascular diseases are among the leading causes of death worldwide. Early prediction of heart attack risk can significantly improve prevention and treatment outcomes.

This project applies Machine Learning techniques to predict heart attack risk based on clinical and demographic data. The workflow includes data preprocessing, exploratory data analysis (EDA), feature engineering, model development, evaluation, and deployment.

---

## Project Objectives

* Predict heart attack risk using patient health data.
* Compare multiple machine learning models.
* Identify the most important risk factors.
* Deploy the model as an interactive web application.

---

## Dataset

**Dataset:** Heart Attack Prediction Dataset

**Source:** Kaggle

### Features

* Age
* Cholesterol Level
* Blood Pressure
* Heart Rate
* Smoking Status
* Diabetes Status
* Obesity Indicator

### Target Variable

* 0 = Low Risk
* 1 = High Risk

---

## Data Preprocessing

The following preprocessing steps were performed:

* Handling missing values
* Removing duplicate records
* Encoding categorical variables
* Feature scaling
* Data cleaning and validation

---

## Exploratory Data Analysis (EDA)

Several visualizations were used to understand the dataset:

* Histograms
* Boxplots
* Countplots
* Scatterplots
* Correlation Heatmaps

### Key Findings

* Higher cholesterol levels are associated with increased heart attack risk.
* Older individuals have a higher probability of heart attack.
* High blood pressure significantly contributes to risk.
* Lifestyle factors such as smoking and obesity influence cardiovascular health.

---

## Feature Engineering

Additional features were created to improve model performance:

* Age Groups (Young, Adult, Senior, Elder)
* Cholesterol Categories (Normal, Borderline, High)

---

## Machine Learning Models

The following models were implemented and evaluated:

1. Logistic Regression
2. Random Forest Classifier
3. Gradient Boosting Classifier

### Best Model

**Random Forest Classifier**

Reasons:

* High Accuracy
* Balanced Precision and Recall
* Strong Generalization Performance

---

## Model Evaluation Metrics

The models were evaluated using:

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix

---

## Deployment

The final model was deployed using Streamlit.

### Application Access

**Local URL:**
http://localhost:8501

**Network URL:**
http://10.94.63.231:8501

---

## Project Structure

```bash
Heart-Attack-Risk-Prediction/
│
├── data/
├── notebooks/
├── models/
├── app.py
├── requirements.txt
├── README.md
└── assets/
```

---

## Video Presentation

Presentation Video:

[https://drive.google.com/file/d/1YyvTbvyzWN4FD6t7Y9bV9PHmFYdTWB70/view?usp=sharing]

---

## Future Improvements

* Deep Learning Models
* Larger Medical Datasets
* Cloud Deployment
* Real-Time Clinical Integration

---

## Supervisor

Mohamed Elsayeh

---

## Author

Youssef Hatem

---

## Acknowledgments

Special thanks to the course instructor and all contributors who supported this project.
