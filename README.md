# <Project Title>

Machine Learning — Course Project Repository

---

## Course Information
- **Course Name:** Machine Learning
- **Course Code:** CO3117
- **Semester:** 252
- **Academic Year:** 2025-2026

---

## Instructor Information
- **Instructor (GVHD):** TS. Trương Vĩnh Lân
- **Email:** lantv@hcmut.edu.vn

---

## Team Members

| Full Name | Student ID | Email |
|---|---|---|
| Nguyễn Hồ Nguyên Khôi | 2420020 | khoi.nguyen2420020@hcmut.edu.vn |
| Nguyễn Võ Anh Quân | 2312847 | quan.nguyencunne2005@hcmut.edu.vn |
| Bùi Nhật Quí | 2312864 | qui.bui011105@hcmut.edu.vn |
| Trần Kiến Quốc | 2312878 | quoc.tran522005@hcmut.edu.vn |
| Phạm Thành Trí | 2313621 | tri.phamyeungoc@hcmut.edu.vn |

---

# Project Overview

This project focuses on predicting apartment rental prices in Germany using both traditional machine learning and modern deep learning approaches on the **Apartment Rental Offers in Germany** dataset.

The study explores how apartment characteristics such as area, number of rooms, location, furnishing condition, construction year, and rental-related costs affect apartment prices. The project includes both:

- **Regression tasks** for predicting exact rental prices.
- **Classification tasks** for predicting rental price segments.

In addition to traditional machine learning models, the project also investigates modern tabular learning architectures including deep learning and gradient boosting methods.

---

## Objective

The main objective of this project is to:

- Apply machine learning techniques to a real-world real-estate dataset.
- Build predictive models for apartment rental prices.
- Compare traditional machine learning methods with modern deep learning approaches.
- Analyze important factors affecting apartment rental prices.
- Evaluate model performance using multiple regression and classification metrics.

---

## Problem Statement

Apartment rental pricing is a complex problem influenced by many interconnected factors such as:

- Apartment size
- Number of rooms
- Geographic location
- Furnishing quality
- Building age
- Base rent
- Additional costs and utilities

Because rental prices depend on nonlinear interactions between multiple variables, traditional pricing methods are often insufficient for accurate estimation.

This project aims to solve the problem by applying both machine learning and deep learning models to predict:
- The exact rental price of an apartment.
- The rental price category (budget, mid-range, premium).

The project also evaluates how different learning paradigms perform on structured tabular data.

---

## Models Used

### Traditional Machine Learning Models

#### Regression
- Linear Regression
- Support Vector Regression (SVR)
- k-Nearest Neighbors Regression (k-NN)
- Random Forest Regressor

#### Classification
- Logistic Regression
- Naive Bayes

---

### Deep Learning / Modern Models

- Multi-Layer Perceptron (MLP)
- LightGBM
- TabNet

These models are used to explore:
- Nonlinear feature interactions
- Representation learning
- Modern tabular learning techniques

---


## Dataset
- **Dataset Name:** Apartment rental offers in Germany
- **Source:** [here](https://www.kaggle.com/datasets/corrieaar/apartment-rental-offers-in-germany)
- **Description:** The data was scraped from Immoscout24, the biggest real estate platform in Germany. Immoscout24 has listings for both rental properties and homes for sale, however, the data only contains offers for rental properties.
- **Number of Samples:** 268,850
- **Features:** 49

---

# Project Structure

```text
└── 📁Project
    └── 📁features
        └── 📁processed
            ├── test.csv
            ├── train.csv
            ├── val.csv
        └── 📁raw
            ├── immo_data.csv
    └── 📁modules
        ├── preprocessing.py
        ├── utils.py
    └── 📁notebooks
        ├── eda_and_prep.ipynb
        ├── logistic_model.ipynb
        ├── model_comp.ipynb
        ├── Naive_Bayes_model.ipynb
        ├── regression.ipynb
        ├── svm_model.ipynb
    └── 📁reports
        └── 📁figures
    ├── .gitignore
    ├── download.py
    ├── README.md
    └── requirements.txt