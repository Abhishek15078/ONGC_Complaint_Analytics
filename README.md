# ONGC Complaint Analytics System

## Overview

The ONGC Complaint Analytics System is an AI-powered complaint management solution developed to automate complaint analysis and support decision-making.

The system predicts:

- Complaint Priority
- SLA Status
- Estimated Resolution Time

using Machine Learning models and provides an interactive web portal along with Power BI analytics dashboards.

---

## Project Architecture

Complaint Submission
↓
HTML/CSS/JavaScript Frontend
↓
FastAPI Backend
↓
Machine Learning Models
↓
Prediction Results
↓
Power BI Dashboard Analytics

---

## Features

### Complaint Analysis Portal

- Submit complaints through a web interface
- Analyze complaint severity
- Predict priority levels
- Predict SLA compliance
- Estimate resolution time

### Machine Learning Models

- Priority Prediction Model
- SLA Prediction / Rule Engine
- Resolution Time Prediction Model
- TF-IDF Vectorization

### Dashboard Analytics

- Complaint Trends
- Priority Distribution
- SLA Analysis
- Department-wise Complaints
- Resolution Time Metrics
- Interactive Power BI Reports

### Deployment

- Frontend hosted on GitHub Pages
- Backend hosted on Render
- Dashboard published via Power BI Service

---

## Technology Stack

### Frontend

- HTML5
- CSS3
- JavaScript

### Backend

- FastAPI
- Uvicorn

### Machine Learning

- Python
- Scikit-Learn
- TF-IDF
- Joblib

### Analytics

- Power BI

### Deployment

- GitHub Pages
- Render

---

## Folder Structure

```text
ONGC_Complaint_Analytics/
│
├── api/
│   ├── main.py
│   ├── schemas.py
│   └── model_loader.py
│
├── models/
│   ├── priority_model.pkl
│   ├── sla_model.pkl
│   ├── resolution_time_model.pkl
│   └── tfidf.pkl
│
├── Images/
│   └── ONGC_Logo.svg.png
│
├── index.html
├── style.css
├── script.js
│
├── requirements.txt
├── render.yaml
└── README.md
```

---

## API Endpoint

### POST /predict-all

Sample Request

```json
{
  "text": "Petrel software license expired and project files are inaccessible",
  "department": "Geoscience",
  "group": "TD",
  "software": "Petrel",
  "hw_flag": 0
}
```

Sample Response

```json
{
  "priority": "Critical",
  "sla_prediction": "Within SLA",
  "estimated_resolution_hours": 18.5
}
```

---

## Local Setup

### Clone Repository

```bash
git clone <repository-url>
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run FastAPI

```bash
uvicorn api.main:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

---

## Live Deployment

### Frontend

GitHub Pages

https://abhishek15078.github.io/ONGC_Complaint_Analytics/

### Backend API

https://ongc-complaint-api.onrender.com

### API Documentation

https://ongc-complaint-api.onrender.com/docs

### Power BI Dashboard

https://app.powerbi.com/groups/7a75b0c2-4f5c-48c8-a835-c5aba49d5786/reports/414e4b06-74a5-41a1-b229-69dfa6009f85/8e2e36ed0aa5ad3dba57?experience=power-bi

---

## Future Enhancements

- User Authentication
- Complaint Tracking System
- Email Notifications
- Automated Ticket Assignment
- Real-Time Dashboard Updates
- LLM-Based Complaint Summarization
- Chatbot Support

---

## Author

Abhishek Kumar Singh

Project: ONGC Complaint Analytics System
