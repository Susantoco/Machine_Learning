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
| Nguyễn Hồ Nguyên Khôi | 2420020 | <Email> |
| Nguyễn Võ Anh Quân | 2312847 | quan.nguyencunne2005@hcmut.edu.vn |
| Bùi Nhật Quí | 2312864 | qui.bui011105@hcmut.edu.vn |
| Trần Kiến Quốc | 2312878 | quoc.tran522005@hcmut.edu.vn |
| Phạm Thành Trí | 2313621 | tri.phamyeungoc@hcmut.edu.vn |

---

# Project Overview

## Objective
Briefly describe the goal of the project.

Example:
> The objective of this project is to apply machine learning techniques to solve a real-world problem, including data preprocessing, model training, evaluation, and analysis of results.

---

## Problem Statement
Describe:
- What problem your project aims to solve
- Why the problem is important
- Expected outcomes

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