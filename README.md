# 🏋️ Exercise Recognition using Machine Learning

An end-to-end Machine Learning project that recognises human physical activities using sensor (IMU) data. This project simulates a real-world fitness AI pipeline similar to those used in wearable fitness devices.

## 📌 Project Overview

Modern fitness wearables rely on Inertial Measurement Unit (IMU) sensors such as accelerometers and gyroscopes to understand human movement. The objective of this project is to build a machine learning model capable of recognising different physical activities from sensor readings.

The project demonstrates the complete machine learning workflow including:

* Data preprocessing
* Exploratory Data Analysis (EDA)
* Feature engineering
* Model training
* Model evaluation
* Performance comparison
* Prediction on unseen data

---

## 🎯 Objectives

* Understand IMU sensor data
* Build activity recognition models
* Compare multiple machine learning algorithms
* Evaluate model performance using classification metrics
* Develop a foundation for wearable fitness AI applications

---

## 📊 Dataset

This project uses the **UCI Human Activity Recognition (HAR) Dataset**.

Activities include:

* Walking
* Walking Upstairs
* Walking Downstairs
* Sitting
* Standing
* Laying

Each activity is represented using accelerometer and gyroscope measurements collected from smartphones.

---

## 🛠️ Tech Stack

* Python
* NumPy
* Pandas
* Matplotlib
* Scikit-learn
* Jupyter Notebook

---

## 📂 Project Structure

```
Exercise-Recognition-ML/
│
├── data/
│
├── notebooks/
│   └── Exercise_Recognition.ipynb
│
├── src/
│   ├── preprocess.py
│   ├── train.py
│   ├── predict.py
│   └── utils.py
│
├── models/
│
├── images/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🤖 Machine Learning Workflow

1. Load dataset
2. Clean and preprocess data
3. Explore data visually
4. Split training and testing datasets
5. Train multiple ML models
6. Evaluate performance
7. Select the best-performing model
8. Save the trained model for inference

---

## 📈 Models to be Compared

* K-Nearest Neighbours (KNN)
* Decision Tree
* Random Forest

Future versions may also include:

* Support Vector Machine (SVM)
* XGBoost
* Neural Networks

---

## 📏 Evaluation Metrics

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix

---

## 🚀 Future Improvements

* Real-time activity prediction
* IMU data visualisation
* BLE sensor integration
* TensorFlow Lite deployment
* Mobile application integration
* Lightweight TinyML models for wearable devices

---

## 📚 Learning Outcomes

Through this project I aim to gain practical experience in:

* Data preprocessing
* Machine learning pipelines
* Sensor data analysis
* Human Activity Recognition (HAR)
* Model evaluation and optimisation
* AI applications in wearable fitness technology

---

## 📄 License

This project is created for educational and portfolio purposes.
