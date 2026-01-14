# Breast Cancer Classification using Random Forest & GridSearchCV

## Overview
This project uses the **Breast Cancer Wisconsin dataset** from `sklearn.datasets` to train a **Random Forest Classifier**.  
We apply **GridSearchCV** to find the best hyperparameters and improve model performance.

---

## Dataset

### Description
Features are computed from a digitized image of a **fine needle aspirate (FNA)** of a breast mass.  
Each sample describes characteristics of **cell nuclei** in the image.  

There are **30 numeric features**, such as:  
`radius_mean`, `texture_mean`, `perimeter_mean`, `area_mean`, `smoothness_mean`, etc.

### Target Variable
- `0` → Malignant (cancerous)  
- `1` → Benign (non-cancerous)

### Class Distribution
- 357 benign samples  
- 212 malignant samples  

Slight class imbalance exists, but **Random Forest handles it well**.

### References
- [UCI Machine Learning Repository: Breast Cancer Wisconsin (Diagnostic)](https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+(Diagnostic))  
- [Scikit-learn Dataset Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_breast_cancer.html)

---

## Methodology

1. **Data Preprocessing**  
   - Load dataset  
   - Split into train and test sets  
   - Standardize features if needed

2. **Model Training**  
   - Use `RandomForestClassifier`  
   - Apply `GridSearchCV` to tune hyperparameters  

3. **Evaluation**  
   - Test accuracy  
   - Confusion matrix  
   - Feature importance analysis

---

## Results

- GridSearchCV finds the **best hyperparameters** for the Random Forest model.  
- **Test accuracy** is usually above **95%**.  
- **Confusion matrix** and **feature importance plots** help interpret the model.
