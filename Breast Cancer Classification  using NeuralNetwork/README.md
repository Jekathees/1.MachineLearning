# Breast Cancer Classification using Artificial Neural Networks (ANN)

## Overview
This project builds an **Artificial Neural Network (ANN)** to classify breast tumors as **Malignant (Cancerous)** or **Benign (Non-Cancerous)** using the **Breast Cancer Wisconsin Diagnostic Dataset**.  

The model is trained using **TensorFlow & Keras**, with standardized numerical features and a **binary output** using a sigmoid activation.

---

## Dataset Description

### Source
Dataset used: **Breast Cancer Wisconsin (Diagnostic)**  
Available from:
- Scikit-Learn built-in dataset: `load_breast_cancer()`
- UCI ML Repository
- Or CSV dataset: e.g., `breast_cancer_data.csv`

### Attributes
The dataset contains **32 columns**, including extra columns that need preprocessing:

- `id` → Identifier (dropped for modeling)  
- `Unnamed: 32` → Empty column (dropped)  
- `diagnosis` → Target column (M/B)  
- 30 numeric features describing cell nuclei, such as:
  - `radius_mean`, `texture_mean`, `perimeter_mean`, `area_mean`, `smoothness_mean`, …  

After preprocessing, we keep **30 numeric features** for ANN input and **1 target column**.

### Target Labels
We apply **label encoding** to convert the `diagnosis` column:

| Original | Encoded | Meaning |
|----------|---------|---------|
| B        | 1       | Benign (Non-Cancer) |
| M        | 0       | Malignant (Cancer) |

### Class Distribution
The dataset is slightly imbalanced but acceptable:

### Evaluation Metrics
Validation Accuracy: 0.9783
Test Accuracy: 0.9737 (~97.37%)

