# 🚀 Product Trac – Full Stack Inventory App

**Product Trac** is a full-stack web application designed to manage product inventory efficiently. It allows users to perform complete CRUD (Create, Read, Update, Delete) operations on products through a clean UI and a RESTful backend API.

The backend is built using **FastAPI**, providing high-performance API endpoints, while the frontend delivers a simple and intuitive interface for interacting with the system. The application uses **MySQL** as the database and integrates **SQLAlchemy ORM** for seamless database operations.

This project demonstrates core backend development concepts such as API design, request validation, database integration, and deployment, along with frontend-backend communication in a real-world setup.

---

## 🚀 Key Features

- 📦 Add new products with details like name, price, description, and quantity  
- 📋 View all available products  
- 🔍 Fetch individual product details by ID  
- ✏️ Update product information (partial updates supported)  
- 🗑️ Delete products from the database  
- 🔗 Fully integrated frontend and backend  

---

## 🛠️ Tech Stack

- **Backend:** FastAPI, Python  
- **Frontend:** HTML, CSS, JavaScript  
- **Database:** MySQL (Railway hosted)  
- **ORM:** SQLAlchemy  
- **Validation:** Pydantic  
- **Server:** Uvicorn  

---
## 🎯 Purpose of the Project

This project was built to:
- Strengthen backend development skills using FastAPI  
- Understand database integration with SQLAlchemy  
- Learn full-stack communication between frontend and backend  
- Gain hands-on experience in deploying real-world applications  

---


## ⚙️ Quick Setup

### 🔹 Backend

```bash
python -m venv myenv
myenv\Scripts\activate      # Windows
pip install fastapi uvicorn sqlalchemy pymysql python-dotenv
uvicorn main:app --reload
```

Backend runs at:

```
http://127.0.0.1:8000
```

---

### 🔹 Database (MySQL)

```sql
CREATE DATABASE Product_FastAPI;
```

Create `.env` file:

```
db_url = mysql+pymysql://USERNAME:PASSWORD@localhost:3306/Product_FastAPI
```

---

### 🔹 Frontend (React)

```bash
cd frontend
npm install
npm start
```

Frontend runs at:

```
http://localhost:3000
```

---

## 🔗 API Endpoints

| Method | Endpoint       | Description       |
| ------ | -------------- | ----------------- |
| GET    | /products      | Get all products  |
| GET    | /products/{id} | Get product by ID |
| POST   | /products      | Add new product   |
| PUT    | /products/{id} | Update product    |
| DELETE | /products/{id} | Delete product    |

---

## 🧠 Learning Highlights

- Built REST APIs using FastAPI
- Learned SQLAlchemy ORM
- Integrated MySQL with Python backend
- Connected frontend with backend APIs
- Implemented full CRUD operations

---

## ⚠️ Notes

- Make sure MySQL server is running
- Backend must be running before frontend
- `.env` file should not be pushed to GitHub

---

## 🚀 Future Improvements

- Add authentication (JWT)
- Pagination & filtering
- Deploy backend + frontend
- Add image upload for products

---

## 👨‍💻 Author

SRINITHYA

---

⭐ If you like this project, give it a star!
