# 🍔 Food Delivery Time Prediction

A Machine Learning project that predicts food delivery time based on factors such as delivery person details, weather conditions, traffic level, order type, vehicle type, and delivery distance.

This project includes:
- Data cleaning and preprocessing
- Feature engineering
- Machine Learning model training
- Model evaluation
- Streamlit web application for real-time predictions

---

## 📌 Problem Statement

Food delivery time is affected by multiple factors such as traffic, weather, distance, and delivery conditions. Predicting delivery time accurately can help improve customer experience and delivery planning.

This project uses Machine Learning techniques to estimate delivery time in minutes.

---

## ✨ Features

- Data preprocessing pipeline
- Missing value handling
- Coordinate cleaning and distance calculation
- Feature engineering
- Random Forest Regression model
- Model saving using Joblib
- Interactive Streamlit web application
- Real-time delivery time prediction

---

## 🛠️ Tech Stack

### Programming Language
- Python

### Libraries
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Streamlit

### Machine Learning
- Random Forest Regressor

---

## 📊 Dataset Features

### Numerical Features
- Delivery Person Age
- Delivery Person Ratings
- Temperature
- Humidity
- Precipitation
- Distance (km)

### Categorical Features
- Traffic Level
- Weather Description
- Type of Order
- Type of Vehicle

### Target Variable
- Delivery Time (minutes)

---

## ⚙️ Machine Learning Workflow

1. Data Cleaning
2. Handling Missing Values
3. Coordinate Correction
4. Distance Calculation
5. Feature Selection
6. Data Preprocessing
7. Train-Test Split
8. Model Training
9. Model Evaluation
10. Model Deployment using Streamlit

---

## 📈 Model Performance

| Metric | Value |
|----------|---------|
| MAE | 3.04 |
| RMSE | 5.42 |
| R² Score | 0.88 |

---

## 📁 Project Structure

```text
Food-Delivery-Time-Prediction/
│
├── app/
│   └── app.py
│
├── data/
│   └── delivery_data.csv
│
├── models/
│   └── delivery_model.pkl
│
├── notebooks/
│   └── food_delivery_prediction.ipynb
│
├── .gitignore
├── .gitattributes
├── README.md
└── requirements.txt
```

---

## 🚀 Run Locally

Clone the repository:

```bash
git clone https://github.com/Shrutir09/Food-Delivery-Time-Prediction.git
```

Move to project folder:

```bash
cd Food-Delivery-Time-Prediction
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run Streamlit app:

```bash
streamlit run app/app.py
```

---

## 🖥️ Streamlit Application

The application allows users to enter:
- Delivery person details
- Weather conditions
- Traffic level
- Distance
- Vehicle type
- Order type

and get an estimated delivery time instantly.

---

## 🔮 Future Improvements

- Hyperparameter tuning
- Model comparison
- Live map integration
- Route optimization
- Deployment on Streamlit Cloud

---

## 👩‍💻 Author

Shruti Riya