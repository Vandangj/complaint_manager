# Campus-Management-Portal
# 🏫 Campus Resource Management System

A unified web-based platform designed to streamline campus operations by integrating **Lost & Found**, **Equipment Tracking**, and **Complaint Management** modules.  
This project was built as part of our **DBMS Final Project** using **FastAPI**, **MySQL**, and **Streamlit**.

---

## 🚀 Overview

The Campus Resource Management System helps students and administrators manage essential campus activities:

- 📦 **Lost & Found System** – Report lost items or register found ones. Admins can verify and return items.  
- ⚙️ **Equipment Tracker** – Track equipment usage, borrowing, and returns within the campus.  
- 🧾 **Complaint Management** – Students and staff can file complaints which are then handled by administrators.

All three modules share a **common login system** and a **centralized MySQL database**.

---

## 📸 Preview

### Lost and Found
![t1](./screenshots/1.png)

### Equipment Tracker
![t2](./screenshots/2.png)

### Complaint Management
![t3](./screenshots/3.png)

---

## 🧠 Tech Stack

| Component | Technology |
|------------|-------------|
| **Backend** | [FastAPI](https://fastapi.tiangolo.com/) |
| **Database** | MySQL with SQLAlchemy ORM |
| **Frontend** | Streamlit |
| **Authentication** | JWT-based login system |
| **Server** | Uvicorn |

---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone <repository-url>
cd <repository-folder>
