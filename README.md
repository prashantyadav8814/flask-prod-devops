# 🚀 Production-Ready DevOps Project (Flask + MySQL + CI/CD on Azure)

## 📌 Project Overview
This project demonstrates a **production-grade DevOps pipeline** for deploying a Flask web application with a MySQL database on Azure using modern DevOps practices.

---

## 🏗️ Architecture
- **Frontend**: Flask (Python)
- **Backend**: MySQL (Azure Database)
- **Containerization**: Docker
- **CI/CD**: Jenkins
- **Reverse Proxy**: Nginx
- **Cloud**: Azure VM
- **Infrastructure as Code**: Terraform

---

## ⚙️ Tech Stack
- Python (Flask)
- Docker & Docker Compose
- Jenkins (CI/CD)
- Nginx
- Azure Cloud
- Git & GitHub

---

## 🔄 CI/CD Workflow
1. Code pushed to GitHub
2. Jenkins pipeline triggers automatically
3. Docker image is built
4. Image pushed to Azure Container Registry
5. Application deployed on Azure VM

---

## 📁 Project Structure
app/        → Flask application
docker/     → Docker configuration
nginx/      → Reverse proxy config
jenkins/    → CI/CD pipeline

---

## 🚀 How to Run Locally

### Step 1: Clone repo
git clone https://github.com/prashantyadav8814/flask-prod-devops.git  
cd flask-prod-devops  

### Step 2: Run application
docker-compose -f docker/docker-compose.prod.yml up --build  

### Step 3: Open in browser
http://localhost:5000  

---

## 👨‍💻 Author
Prashant Yadav
