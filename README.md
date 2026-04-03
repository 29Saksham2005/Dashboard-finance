# 💰 Finance Dashboard Backend

## 🚀 Project Overview

This project is a **backend API for a finance dashboard application**. It provides secure authentication, role-based access control, financial record management, and dashboard analytics.

The system is designed to simulate a real-world backend where users can:

* manage financial transactions
* view summarized insights (income, expenses, trends)
* access features based on their roles (Admin, Analyst, Viewer)

---

## 🧠 Key Features

### 🔐 Authentication & Security

* JWT-based authentication
* Secure password hashing using bcrypt
* Token-based protected routes

### 👥 Role-Based Access Control (RBAC)

* **Admin**

  * Full access (users, records, dashboard)
* **Analyst**

  * Read-only access to records and dashboard
* **Viewer**

  * Dashboard-only access

### 👤 User Management (Admin Only)

* Create users
* List users
* Update user roles and status
* Activate/Deactivate users

### 📊 Financial Records

* Create, read, update, delete (soft delete)
* Filtering by:

  * type (INCOME / EXPENSE)
  * category (case-insensitive search)
  * date range
* Pagination support

### 📈 Dashboard Analytics

* Total income
* Total expenses
* Net balance
* Record count
* Category-wise breakdown
* Monthly trends
* Recent activity

---

## 🛠️ Tech Stack

* **Backend Framework:** FastAPI
* **Database:** PostgreSQL
* **ORM:** SQLAlchemy
* **Validation:** Pydantic
* **Authentication:** JWT (python-jose)
* **Password Hashing:** Passlib (bcrypt)
* **Server:** Uvicorn

---

## 📂 Project Structure

```
finance-dashboard-backend/
│
├── app/
│   ├── api/
│   │   ├── routes/
│   │   │   ├── auth.py
│   │   │   ├── dashboard.py
│   │   │   ├── health.py
│   │   │   ├── records.py
│   │   │   └── users.py
│   │   └── deps.py
│   │
│   ├── core/
│   │   ├── config.py
│   │   ├── database.py
│   │   ├── exceptions.py
│   │   └── security.py
│   │
│   ├── models/
│   │   ├── user.py
│   │   ├── record.py
│   │   ├── enums.py
│   │   └── __init__.py
│   │
│   ├── schemas/
│   │   ├── user.py
│   │   ├── record.py
│   │   ├── record_query.py
│   │   ├── dashboard.py
│   │   └── auth.py
│   │
│   ├── services/
│   │   ├── auth_service.py
│   │   ├── user_service.py
│   │   ├── record_service.py
│   │   └── dashboard_service.py
│   │
│   ├── main.py
│   └── seed.py
│
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```
git clone <your-repo-url>
cd finance-dashboard-backend
```

### 2. Create virtual environment

```
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Setup environment variables

Create a `.env` file based on `.env.example`:

```
DATABASE_URL=postgresql://postgres:password@localhost:5432/finance_dashboard
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
```

---

### 5. Setup database

Create a PostgreSQL database:

```
finance_dashboard
```

---

### 6. Run the server

```
uvicorn app.main:app --reload
```

Open Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

### 7. Seed default users

```
python -m app.seed
```

---

## 🔑 Default Users

| Role    | Email                                             | Password   |
| ------- | ------------------------------------------------- | ---------- |
| Admin   | [admin@example.com](mailto:admin@example.com)     | Admin123   |
| Analyst | [analyst@example.com](mailto:analyst@example.com) | Analyst123 |
| Viewer  | [viewer@example.com](mailto:viewer@example.com)   | Viewer123  |

---

## 🔐 Authentication Flow

1. Login via `/api/auth/login`
2. Receive JWT token
3. Use token via Swagger **Authorize**
4. Access protected routes

---

## 📌 API Modules

### Auth APIs

* `/api/auth/login`
* `/api/auth/me`

### User APIs (Admin Only)

* `/api/users/`
* `/api/users/{id}`

### Record APIs

* `/api/records/`
* Filtering + pagination

### Dashboard APIs

* `/api/dashboard/summary`
* `/api/dashboard/category-breakdown`
* `/api/dashboard/monthly-trends`
* `/api/dashboard/recent-activity`

---

## 🔐 Role Access Summary

| Feature        | Admin | Analyst | Viewer |
| -------------- | ----- | ------- | ------ |
| Users          | ✅     | ❌       | ❌      |
| Records (CRUD) | ✅     | ❌       | ❌      |
| Records (Read) | ✅     | ✅       | ❌      |
| Dashboard      | ✅     | ✅       | ✅      |

---

## 🧪 Example API Usage

### Create Record

```json
{
  "amount": 5000,
  "type": "EXPENSE",
  "category": "Food",
  "date": "2026-04-03",
  "notes": "Dinner"
}
```

---

## ⚙️ Optional Enhancements Implemented

This project includes several optional backend improvements:

* JWT-based authentication
* Role-based protected routes
* Pagination for record listing
* Search/filter support for records
* Soft delete functionality
* Interactive API documentation (Swagger/OpenAPI)

These enhancements improve usability and backend design without unnecessary complexity.

---

## ⚖️ Assumptions and Tradeoffs

* The system is designed for **assessment purposes**, not production deployment.
* Role permissions are intentionally simple and clearly defined.
* Soft delete is used to ensure safety and recoverability of records.
* JWT authentication is chosen for simplicity and stateless API design.
* Pagination is implemented to support scalability.
* Dashboard analytics are computed in the backend for consistency and performance.
* Features like rate limiting and automated testing were intentionally omitted to keep the solution focused and clean.

---

## 📊 How This Project Addresses the Evaluation Criteria

### 1. Backend Design

Clear separation of:

* Routes
* Services
* Models
* Schemas
* Core utilities

### 2. Logical Thinking

* Role-based access control
* Business rule enforcement
* Filtering and analytics design

### 3. Functionality

* Authentication
* User management
* Records CRUD
* Filtering + pagination
* Dashboard analytics

### 4. Code Quality

* Modular structure
* Clean naming conventions
* Reusable services
* Maintainable code

### 5. Database and Data Modeling

* Proper relational modeling
* Role support
* Soft delete
* Timestamp tracking

### 6. Validation and Reliability

* Pydantic validation
* Enum constraints
* Exception handling
* Access control checks

### 7. Documentation

* Clear setup instructions
* API overview
* Default users
* Assumptions and tradeoffs

### 8. Additional Thoughtfulness

* Dashboard aggregation APIs
* Search + filtering
* Pagination
* Structured backend design

---

## 📈 Future Improvements

* Frontend integration (React dashboard)
* Export reports (CSV/PDF)
* Advanced analytics
* Role-based record ownership
* Docker deployment

---

## 👨‍💻 Author

Developed as part of a backend engineering assignment using FastAPI.

---

## ⭐ Final Note

This project focuses on **clarity, structure, and backend design thinking** rather than unnecessary complexity. It demonstrates how to build a clean, scalable backend with authentication, role-based access control, and data-driven APIs.
