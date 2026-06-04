# Build-a-REST-API-with-Flask.py
A lightweight RESTful CRUD API built with Python and Flask for managing user data via standard HTTP methods (GET, POST, PUT, DELETE).
# Task 4: REST API Development with Flask

A lightweight, fully functional RESTful API built using Python and the Flask framework. This project demonstrates the fundamentals of API development, handling standard HTTP CRUD operations (Create, Read, Update, Delete) using an in-memory dictionary database.

## 🚀 Features & Endpoints

The API manages a collection of `user` data resources with the following endpoints:

| Method | Endpoint | Description | Status Code |
| :--- | :--- | :--- | :--- |
| **GET** | `/users` | Fetch all users in the database | `200 OK` |
| **GET** | `/users/<id>` | Fetch details of a specific user | `200 OK` / `404 Not Found` |
| **POST** | `/users` | Create and add a new user | `201 Created` / `400 Bad Request` |
| **PUT** | `/users/<id>` | Update an entire user's details | `200 OK` / `404 Not Found` |
| **DELETE**| `/users/<id>` | Remove a user from the system | `200 OK` / `404 Not Found` |

---

## 💻 Tech Stack & Tools Used
* **Backend Framework:** Python (Flask)
* **Testing Tools:** Curl / Postman
* **Version Control:** Git & GitHub

---
Install Flask:
pip install flask.
Run the Application:
python app.py
