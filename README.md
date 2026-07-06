# Explainable AI Mini Project

## Overview

This project was developed as part of the **Explainable AI** course. The objective is to build an interpretable machine learning pipeline for an RDF Knowledge Graph by transforming graph-structured data into a tabular representation, training classification models, and explaining the resulting predictions using multiple Explainable AI (XAI) techniques.

The project uses the **AIFB RDF dataset**, where the task is to predict the research group affiliation of persons based on information extracted from the RDF knowledge graph.

---

# Project Workflow

The complete workflow consists of four stages:

```
RDF Knowledge Graph
        │
        ▼
Data Exploration
        │
        ▼
Feature Engineering
        │
        ▼
Machine Learning
        │
        ▼
Explainable AI
```

---

# Repository Structure

```
Explainable-AI-Mini-Project/
│
├── data/
│   └── aifb-hetero/
│
├── models/
│   ├── random_forest_model.pkl
│   ├── logistic_regression_model.pkl
│   └── label_encoder.pkl
│
├── notebooks/
│   ├── 01_Data_Exploration.ipynb
│   ├── 02_Feature_Engineering.ipynb
│   ├── 03_Model_Training.ipynb
│   └── 04_Explainable_AI.ipynb
│
├── outputs/
│   ├── figures/
│   ├── tables/
│   ├── feature_matrix.csv
│   └── feature_matrix.pkl
│
├── report/
│
├── utils/
│   ├── helper_functions.py
│   ├── paths.py
│   └── __init__.py
│
├── requirements.txt
└── README.md
```

---

# Dataset

**Dataset:** AIFB RDF Knowledge Graph

The project uses:

- RDF Knowledge Graph (`aifbfixed_complete.n3`)
- Training dataset
- Testing dataset
- Complete labelled dataset

The prediction task is to classify a person into one of four research groups.

---

# Notebook Description

## 01 – Data Exploration

This notebook explores the RDF graph and the machine learning datasets.

Main tasks:

- Load RDF graph
- Explore graph statistics
- Convert RDF URIs into human-readable names
- Analyze entities, predicates and node types
- Explore the training and testing datasets

---

## 02 – Feature Engineering

This notebook converts the RDF graph into a structured feature matrix.

Main tasks:

- Explore neighbourhoods of labelled persons
- Analyze informative predicates
- Select candidate features
- Evaluate feature leakage
- Design feature encodings
- Generate the final feature matrix

---

## 03 – Model Training

This notebook trains and evaluates multiple classification models.

Models evaluated:

- Logistic Regression
- Decision Tree
- Random Forest
- XGBoost (optional)

Evaluation metrics:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix
- Classification Report

The best-performing model is saved for Explainable AI analysis.

---

## 04 – Explainable AI

This notebook explains the trained Random Forest model using both global and local explanation methods.

Methods implemented:

### Global Explanations

- Built-in Feature Importance
- Permutation Feature Importance
- Partial Dependence Plots (PDP)

### Local + Global Explanations

- Individual Conditional Expectation (ICE)

### SHAP Explanations

- SHAP Global Feature Importance
- SHAP Beeswarm Plot
- SHAP Waterfall Plot
- SHAP Force Plot

---

# Model Performance

| Model | Test Accuracy | Macro F1 |
|--------|--------------:|---------:|
| Logistic Regression | 0.75 | 0.648 |
| Random Forest | 0.75 | 0.623 |
| Decision Tree | 0.722 | 0.598 |
| XGBoost | 0.722 | 0.549 |

The **Random Forest** classifier was selected for Explainable AI because it achieved competitive performance while providing robust feature importance estimates and is well supported by SHAP.

---

# Key Features Identified

Across the different explanation methods, the following features consistently appeared among the most influential:

- Publication Year
- Publication Count
- WorksAtProject Count
- Topic: Semantic Web
- Topic: Ontology Engineering
- Homepage
- Number of Projects
- Knowledge Management related research topics

These findings indicate that publication activity, research interests, and project involvement contribute significantly to predicting research group affiliation.

---

# Requirements

Install all dependencies using:

```bash
pip install -r requirements.txt
```

---

# Running the Project

Run the notebooks sequentially:

```
01_Data_Exploration.ipynb
        ↓
02_Feature_Engineering.ipynb
        ↓
03_Model_Training.ipynb
        ↓
04_Explainable_AI.ipynb
```

Each notebook generates the required outputs for the subsequent notebook.

---

# Output Files

The project generates:

- Engineered feature matrix
- Trained machine learning models
- Label encoder
- Feature engineering tables
- Model comparison tables
- Explainable AI figures
- SHAP visualizations

---

# Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- RDFLib
- Scikit-learn
- SHAP
- XGBoost
- Joblib
- Jupyter Notebook

---

# Author

**Manoj Billur Nagendra Prasad**  

**Steffi Stephen**

University of Paderborn
