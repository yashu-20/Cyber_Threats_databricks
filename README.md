#Cyber Threat Analysis & Prediction using PySpark on Databricks

This project explores global cyber threat incidents from 2015 to 2024 using a real-world structured dataset. The goal is to analyze trends in attack types, affected industries, and resolution performance — and to build a predictive model that classifies whether an incident will have a long resolution time based on key features.

The entire pipeline was implemented using **PySpark on Databricks**, covering data ingestion, SQL-based exploration, feature engineering, classification modeling, and performance evaluation.

---

##Dataset Overview

- **Source**: Synthetic dataset containing 3,000 cyber incident records
- **Fields Include**:
  - `Country`, `Year`, `Attack Type`, `Target Industry`
  - `Financial Loss (in Million $)`, `Number of Affected Users`
  - `Security Vulnerability Type`, `Defense Mechanism Used`
  - `Incident Resolution Time (in Hours)`

The dataset represents threats across various industries and geographies, offering insight into patterns over time.

---

##Objectives

- Identify high-risk attack types and industries using SQL queries
- Visualize loss trends and resolution times
- Engineer new features (`Users_Per_Year`, `User_Impact_Index`, `Long_Resolution`)
- Build a classification model to predict `Long_Resolution` (binary target)
- Evaluate performance using AUC ROC, accuracy, precision, recall, and F1 score

---

## Technologies Used

- **Databricks Community Edition** (runtime environment)
- **Apache Spark (PySpark)** for data processing
- **Spark SQL** for querying and EDA
- **MLlib (GBTClassifier)** for model training
- **Pandas** for CSV export
- **GitHub** for publishing

---

## Process Overview

### 1. Data Ingestion
Loaded the dataset into a Spark DataFrame with schema inference.

### 2. SQL-Based Exploration
Used Spark SQL to analyze:
- Top attack types by frequency
- Year-wise financial loss
- Distribution of resolution time

### 3. Feature Engineering
- Created `Long_Resolution`: 1 if resolution time > median (36 hrs), else 0
- Created `Users_Per_Year` and `User_Impact_Index`
- Indexed categorical columns: Country, Attack Type, Industry, etc.

### 4. Model Training
- Used `GBTClassifier` with indexed + numeric features
- Split data 80/20 for train/test
- Built pipeline using Spark ML

### 5. Evaluation
- **AUC ROC**: 0.4779
- **Accuracy, Precision, Recall, F1 Score**: 0.4736
- Feature importance revealed most impact from `Country`, `Attack Type`, and `Defense Mechanism`

---

## Final Outputs

| Metric        | Score   |
|---------------|---------|
| AUC ROC       | 0.4779  |
| Accuracy      | 0.4736  |
| Precision     | 0.4736  |
| Recall        | 0.4736  |
| F1 Score      | 0.4736  |

A confusion matrix and feature importance ranking are included in the notebook.

---

## Repository Contents

| File | Description |
|------|-------------|
| `CyberThreat_Analysis.ipynb` | Full Databricks notebook (code + comments) |
| `CyberThreat_Analysis.html` | Visual read-only version |
| `Global_Cybersecurity_Threats_2015-2024.csv` | Dataset |
| `README.md` | This file |

---

## How to Run

> Designed for Databricks Community Edition

1. Upload the dataset to `/FileStore/tables` in Databricks
2. Import or open the notebook
3. Attach to a cluster and run all cells
4. Export CSV and notebook results for sharing

---

## Key Learnings

- Built an end-to-end Spark ML pipeline using real-world cybersecurity data
- Gained hands-on experience with feature engineering, SQL exploration, and classification modeling in PySpark
- Practiced exporting and sharing results for reproducibility via GitHub
