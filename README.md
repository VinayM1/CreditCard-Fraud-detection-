# 💳 Credit Card Fraud Detection – ML Project with Jupyter Notebook

This project uses a Jupyter Notebook to detect fraudulent credit card transactions using machine learning. It is based on the Kaggle dataset and includes full steps: data loading, preprocessing, handling class imbalance with SMOTE, model training using Random Forest, evaluation, and saving the model for future use.

---

## 📌 Features

- Notebook-based end-to-end workflow
- Random Forest Classifier with high accuracy
- SMOTE used to fix class imbalance
- Model performance shown via classification report and ROC-AUC
- Model saved using Joblib (`fraud_model.pkl`)
- Beginner-friendly, well-commented notebook

---

## 📁 Files Included

```
credit-card-fraud/
├── CreditCardFraudDetection.ipynb  # Jupyter notebook (main project)
├── creditcard.csv                  # Dataset (from Kaggle)
├── fraud_model.pkl                 # Trained model
├── requirements.txt                # Required libraries
└── README.md                       # This file
```

---

## 💻 How to Use

1. Download dataset from:  
   🔗 https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud

2. Place `creditcard.csv` in the same folder as the notebook.

3. Open the notebook:

```bash
jupyter notebook CreditCardFraudDetection.ipynb
```

4. Run cells step by step:
   - Preprocess data
   - Handle imbalance
   - Train the model
   - Evaluate performance
   - Save model

---

## 🔮 Output

- Model Accuracy, Precision, Recall, F1-Score
- ROC-AUC Score
- Saved model file (`fraud_model.pkl`) for deployment

---

## 📦 Requirements

Install dependencies:

```bash
pip install -r requirements.txt
```

```
pandas
numpy
scikit-learn
imbalanced-learn
matplotlib
seaborn
joblib
```

---

## 📌 Dataset Info

- Source: [Kaggle – Credit Card Fraud Detection](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)
- 284,807 transactions
- Highly imbalanced dataset (0 = legit, 1 = fraud)

---

## 🛡️ License

This project is licensed under the MIT License.

---

> Created with 💻 in Jupyter Notebook by Vinay
