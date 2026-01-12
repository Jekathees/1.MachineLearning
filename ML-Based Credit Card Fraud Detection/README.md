# Credit Card Fraud Detection 

## Project Overview
This project focuses on detecting fraudulent credit card transactions using machine learning.  
The dataset is first preprocessed to balance the classes, and then a model is trained using **GridSearchCV** to find the best hyperparameters for improved performance.

---

## Dataset

### Dataset Link
I downloaded the dataset from Kaggle:   
[Credit Card Fraud Detection Dataset](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)

### Context
It is important that credit card companies are able to recognize fraudulent credit card transactions so that customers are not charged for items they did not purchase.

### Content
- The dataset contains credit card transactions made by European cardholders in **September 2013**.  
- It contains transactions over **two days**, with **492 fraudulent transactions out of 284,807 total transactions**.  
- The dataset is highly **imbalanced**; the positive class (frauds) accounts for only **0.172%** of all transactions.  

### Features
- Only **numerical input variables** are provided as a result of **PCA transformation**.  
- PCA features: `V1, V2, ..., V28`  
- Non-PCA features:  
  - `Time` – seconds elapsed between each transaction and the first transaction  
  - `Amount` – transaction amount (useful for example-dependent cost-sensitive learning)  
- Target variable: `Class` – 1 for fraud, 0 for non-fraud  

### Important Notes
- Due to class imbalance, **confusion matrix accuracy is not meaningful**.  
- It is recommended to evaluate models using **Area Under the Precision-Recall Curve (AUPRC)** or **F1-score**.  

---
## Features of the Project
- Preprocessing to handle **imbalanced data**  
- Train-test split with **stratification**  
- Hyperparameter tuning using **GridSearchCV**  
- Evaluation with **F1-score, Confusion Matrix**
<img width="559" height="430" alt="Screenshot (288)" src="https://github.com/user-attachments/assets/7741c4d3-c11a-4a8f-ad85-7cb171cba3db" />
