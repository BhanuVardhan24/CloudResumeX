Deploy Flask Resume Web App on Azure App Service via GitHub Actions

This project contains a simple **Flask-based resume website** deployed on **Azure App Service** using **GitHub Actions CI/CD**.

It is part of **Project A: CloudResumeX**, focused on learning and practicing real-world Azure deployments.

---

## 📌 What This Project Does

- Hosts a **dynamic Python (Flask)** web application on Azure
- Serves a static HTML resume file (`index.html`)
- Uses **GitHub Actions** for automatic deployment on every push to `main`
- Runs in **Azure App Service (Linux)** with **Python 3.10**
- Production server is **gunicorn**

---

## 🛠️ Tech Stack

| Component     | Tool/Service Used             |
|---------------|-------------------------------|
| Backend       | Python + Flask                |
| Web Server    | gunicorn                      |
| Hosting       | Azure App Service (Linux)     |
| CI/CD         | GitHub Actions                |
| Deployment    | Azure Publish Profile         |

---

## 📁 Project Structure

.
├── app.py # Flask app that serves index.html
├── index.html # Your resume (static HTML)
├── requirements.txt # Dependencies (Flask + gunicorn)
└── .github/
└── workflows/
└── deploy.yml # GitHub Actions CI/CD pipeline

