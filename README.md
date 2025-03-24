# ❤️ Heart Disease Prediction App

## 📌 Overview
This project is a **Machine Learning-based Heart Disease Prediction App** that predicts the severity of heart disease based on patient input features. The app is built using:
- **Scikit-Learn** for machine learning
- **Streamlit** for a web-based interface
- **Pandas & NumPy** for data preprocessing
- **Joblib** for model persistence

## ⚙️ Features
- Preprocessing and encoding of categorical variables
- Feature scaling using **StandardScaler**
- Class balancing using **SMOTE**
- Multiple machine learning models:
  - Logistic Regression
  - Decision Tree
  - Random Forest
  - AdaBoost
  - Voting Classifier (ensemble model)
- **Best model is automatically selected and saved**
- **User-friendly web app** built with Streamlit

## 🚀 Run the App
You can access the live app here:  
🔗 **[Heart Disease Prediction App](https://m-aitisam-heart-disease-prediction-app-5ouc1r.streamlit.app/)**

To run locally, install dependencies and start the app:
```sh
pip install -r requirements.txt
streamlit run app.py
or
python -m streamlit run app.py
```

## 🛠️ Troubleshooting
### 🔹 **ModuleNotFoundError**
If you get missing module errors, install dependencies:
```sh
pip install -r requirements.txt
```

### 🔹 **Model Loading Error**
Ensure **heart_disease_model.pkl** exists. If missing, retrain the model:
```sh
python train_model.py
```

## 📜 License
This project is open-source and available under the **MIT License**.

## 🙌 Contributing
Feel free to fork the repository and submit a pull request to improve the project!

## 💡 Acknowledgments
Special thanks to the **Scikit-Learn** and **Streamlit** communities for their amazing libraries! 🚀

