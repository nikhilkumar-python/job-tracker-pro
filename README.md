# Job Tracker Pro 🚀

Job Tracker Pro is a full-stack Flask web application that helps users track and manage their job applications in one place. Users can register, log in, and maintain a personal dashboard to monitor the status of their job applications.

This project demonstrates backend development skills using Python and Flask, including authentication, database management, and CRUD operations.

---

## 🌐 Live Demo

https://job-tracker-pro-0zet.onrender.com

---

## ✨ Features

- User Registration & Login
- Secure Password Hashing
- Session-based Authentication
- Personal Job Dashboard
- Add Job Applications
- Edit Job Applications
- Delete Job Applications
- Search Jobs by Company
- Job Status Tracking (Applied, Interview, Rejected, Offer)
- Dashboard Analytics
- Bootstrap UI

---

## 📊 Dashboard Overview

The dashboard shows:

- Total Applications
- Interviews
- Rejected Applications
- Job Offers

Users can easily track the progress of their job search.

---
## 📸 Screenshots
<img width="1920" height="1080" alt="{B1D252D1-75C4-4F54-B97D-1362645CEE14}" src="https://github.com/user-attachments/assets/a6cd1ba9-b970-48ca-a506-16e2af409456" />

---

## 🛠 Tech Stack

**Backend**
- Python
- Flask
- SQLAlchemy
- Werkzeug (Password Hashing)

**Frontend**
- HTML
- Bootstrap 5
- Jinja2 Templates

**Database**
- SQLite

**Deployment**
- Render

---

## 📂 Project Structure
job-tracker-pro
│
├── app.py
├── requirements.txt
├── Procfile
├── build.sh
│
├── templates
│ ├── base.html
│ ├── dashboard.html
│ ├── login.html
│ ├── register.html
│ ├── add_job.html
│ └── edit_job.html
│
└── instance
└── database.db


---

## ⚙️ Installation

Clone the repository


git clone https://github.com/your-username/job-tracker-pro.git


Navigate to the project folder


cd job-tracker-pro


Create virtual environment


python -m venv venv


Activate virtual environment


venv\Scripts\activate


Install dependencies


pip install -r requirements.txt


Run the application


python app.py


Open in browser


http://127.0.0.1:5000


---

## 🔐 Authentication

Passwords are securely stored using **Werkzeug password hashing**.

Each user can only access their own job applications using session-based authentication.

---

## 🚀 Future Improvements

- Email notifications for interview updates
- Job analytics charts
- Resume upload feature
- REST API support
- PostgreSQL database

---

## 👨‍💻 Author

**Nikhil Kumar**

Python Developer | Backend Enthusiast

GitHub:  
https://github.com/nikhilkumar-python

LinkedIn:  
(www.linkedin.com/in/nikhil-kumar-32523a3a9)

---

## ⭐ If you like this project

Please consider giving it a **star on GitHub**.
