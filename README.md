# 🚀 Product Trac – Full Stack Inventory App

A full-stack product management application built using **FastAPI**, **MySQL**, and **React**.

---

## ✨ Features

- Add new products
- View all products
- Update product details
- Delete products
- Search products
- FastAPI backend with MySQL
- React frontend UI

---

## 🛠️ Tech Stack

**Backend**

- FastAPI
- SQLAlchemy
- MySQL
- Pydantic

**Frontend**

- React
- CSS

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
