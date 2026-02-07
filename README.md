# Student-Placement-predictor-model

live model application link : https://student-placement-predictor-model-2wezxm4hdlwrhmhhttqrlo.streamlit.app/


To help you create a professional GitHub repository for your machine learning project, here is a structured and comprehensive **README.md** content. It highlights the technical details extracted from your `model.pkl` file, such as the feature names and the specific algorithm used.

---

# 🎓 Student Placement Prediction System

This project is a machine learning application designed to predict the likelihood of a student being placed during campus recruitments. By analyzing academic performance and demographic data, it provides real-time predictions via a user-friendly Streamlit web interface.

## 🚀 Overview

The core of this project is a **K-Nearest Neighbors (KNN)** classification model that categorizes students as either **"Placed"** or **"Not Placed"** based on their profile.

## 🛠️ Technical Stack

* 
**Algorithm:** KNeighborsClassifier (`n_neighbors=5`, `metric='minkowski'`) 


* **Web Framework:** Streamlit
* 
**Data Manipulation:** NumPy, Pandas 


* 
**Model Serialization:** Pickle 


* 
**Version:** Scikit-learn 1.6.1 



## 📊 Features & Input Data

The model processes 6 key features to determine the placement outcome:

| Feature | Description | Type |
| --- | --- | --- |
| **gender** | Gender of the student (Male/Female) | Categorical 

 |
| **ssc_p** | 10th Standard (Secondary) percentage | Continuous 

 |
| **hsc_p** | 12th Standard (Higher Secondary) percentage | Continuous 

 |
| **hsc_s** | 12th Standard specialization (Science/Commerce/Arts) | Categorical 

 |
| **degree_p** | Undergraduate degree percentage | Continuous 

 |
| **mba_p** | MBA degree percentage | Continuous 

 |

## 🏗️ Project Structure

```text
├── app.py              # Streamlit web application code
[cite_start]├── model.pkl           # Pre-trained KNN model [cite: 1]
├── requirements.txt    # List of dependencies
└── README.md           # Project documentation

```

## ⚙️ Installation & Usage

1. **Clone the repository:**
```bash
git clone https://github.com/your-username/placement-predictor.git
cd placement-predictor

```


2. **Install dependencies:**
```bash
pip install -r requirements.txt

```


3. **Run the application:**
```bash
streamlit run app.py

```



## 🧠 Model Details

The model was trained using the `KDTree` algorithm for efficient neighbor searching. It uses the Euclidean distance metric (Minkowski with `p=2`) to calculate similarity between student profiles.

---
