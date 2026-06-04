# MockingBird - Campaign Analytics Dashboard

## Overview

MockingBird is an interactive analytics dashboard built using Streamlit, SQLAlchemy, and PostgreSQL. The application provides role-based access to campaign performance reports, customer segmentation insights, and customer affinity analysis.

The project demonstrates end-to-end application development including authentication, authorization, reporting, logging, and data visualization, with future support planned for machine learning-based campaign predictions.

---

## Features

### Authentication & User Management

* User registration
* Secure login using bcrypt password hashing
* Session management using Streamlit Session State
* User profile page
* Role-based access control (RBAC)

### Access Control

* Admin, Sales, Research, and User roles
* View permissions for reports
* Download permissions for reports
* Dynamic dashboard rendering based on user permissions

### Analytics Reports

#### Campaign Overview

* Campaign distribution analysis
* Success and failure rates
* Data coverage metrics

#### Customer Segmentation

* Customer demographic insights
* Income and salary distribution
* Job, marital, and campaign segmentation

#### Campaign Effectiveness

* Conversion analysis
* Success vs failure tracking
* Campaign performance leaderboard

#### Campaign Customer Affinity

* Customer-to-campaign relationship analysis
* Responsive customer segments
* Campaign targeting insights

### Logging

* Login activity logging
* Logout activity logging
* Report access tracking
* Report download tracking

---

## Technology Stack

### Frontend

* Streamlit

### Backend

* Python
* SQLAlchemy ORM

### Database

* PostgreSQL

### Security

* bcrypt password hashing

### Data Visualization

* Plotly
* Streamlit Charts

---

## Project Structure

```text
MockingBird/
│
├── app.py
├── pages/
│   ├── 1_profile.py
│   ├── 2_dashboard.py
│   ├── 3_register.py
│   ├── campaign_overview.py
│   ├── customer_segmentation.py
│   ├── campaign_effectiveness.py
│   └── cpg_cus_affinity.py
│
├── database/
│   ├── auth.py
│   ├── crud.py
│   └── db.py
│
├── report_service/
│
├── utils/
│   ├── logger.py
│   └── styling.py
│
└── logs/
```

---

## Role-Based Access Model

| Role     | View Reports | Download Reports |
| -------- | ------------ | ---------------- |
| Admin    | All Reports  | All Reports      |
| Sales    | Configurable | Configurable     |
| Research | Configurable | Configurable     |
| User     | Configurable | Configurable     |

Permissions are maintained through database-driven access control tables.

---

## Installation

### Clone Repository

```bash
git clone https://github.com/<your-username>/MockingBird.git
cd MockingBird
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---

## Future Enhancements

* Machine Learning Prediction Module
* Audit Log Dashboard
* User Activity Monitoring
* Model Performance Tracking
* Scheduled Report Generation
* Email Notifications
* Export to Excel and PDF

---

## Learning Outcomes

This project demonstrates practical experience in:

* Python Application Development
* Object Relational Mapping (ORM)
* Authentication & Authorization
* Role-Based Access Control
* Data Visualization
* Logging and Monitoring
* Dashboard Development
* Software Design and Architecture

---

## Author

Built by Sriparna as part of a hands-on journey into analytics engineering, dashboard development, and machine learning applications.
