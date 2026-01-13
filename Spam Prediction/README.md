# Spam Mail Detection using SVM & GridSearchCV

## Overview
This project focuses on classifying email messages as **Spam** or **Ham (Not Spam)** using Machine Learning.  
We use **TF-IDF** for text feature extraction and **Support Vector Machine (SVM)** for classification.  
To improve performance, **GridSearchCV** is applied for hyperparameter tuning.

---

### Dataset Format

The dataset should contain:

| Column   | Description                          |
|----------|--------------------------------------|
| Category | Label (`ham` or `spam`)              |
| Message  | Text content of the SMS or email     |

---

### Label Conversion
Before model training, labels are converted to numeric form:

```
ham  →  1  (Not Spam)
spam →  0  (Spam)
```

This allows the ML model to process categorical labels correctly.

---

## Methodology

### **1. Data Preprocessing**
✔ Load dataset  
✔ Check & handle missing values (if any)  
✔ Convert label categories to numeric form  

---

### **2. Text Vectorization using TF-IDF**
TF-IDF (Term Frequency - Inverse Document Frequency) converts text messages into numerical feature vectors, giving more importance to rare but meaningful words.

---

### **3. Train-Test Split**
The dataset is split into training and testing to evaluate real-world performance.

---

### **4. Model Training using SVM**
SVM (Support Vector Machine) is selected due to its strong performance on high-dimensional text data.

---

### **5. Hyperparameter Tuning**
**GridSearchCV** is used to:
- Search best hyperparameters for SVM
- Perform cross-validation
- Improve model performance

---

### **6. Model Evaluation**
Model evaluation uses the following metrics:
- Accuracy
- Confusion Matrix
- Classification Report (Precision, Recall, F1-score)




