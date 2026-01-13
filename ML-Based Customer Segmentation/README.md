# Customer Segmentation using K-Means Clustering

## Overview
This project performs customer segmentation using **K-Means Clustering**, an unsupervised machine learning algorithm.  
The goal is to group customers based on their **Annual Income** and **Spending Score**, which helps identify different customer types for marketing strategies.

---

## Dataset

### Dataset Link
I downloaded the dataset from Kaggle:  
https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial-in-python

The dataset contains the following columns:

- CustomerID
- Gender
- Age
- Annual Income (k$)
- Spending Score (1-100)

There are **no missing values** in the dataset.

---

## Methodology

1. **Data Loading & Preprocessing**  
2. **Feature Selection:**  
   Used `Annual Income (k$)` and `Spending Score (1-100)`  
3. **Feature Scaling:**  
   Standardized features using `StandardScaler`  
4. **Elbow Method:**  
   Determined optimal clusters → **k = 5**  
5. **K-Means Training**  
6. **Visualization of Segments**  
7. **Save Results to CSV**

---

## Results
- The **Elbow Method** showed a bend at **k = 5**, meaning **5 clusters** provide the best balance.
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/3a178f2a-6fbd-497d-815d-eba1786c30bc" />
 - Clustered data is saved as:  
  `customer_segments.csv`
  
## Final Clusters Visualization
The final K-Means clustering result visually shows how customers are grouped based on their annual income and spending score.
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/39d9c874-8869-441d-bb30-2fd57f3ec5b9" />



### Example Cluster Interpretation:
- Low income, low spending  
- High income, high spending  
- Average customers, etc.

---

## Output Files
- `customer_segments.csv` → Final dataset with cluster labels  

---

