# 🌾 Agri Platform – Django Backend Project

**Agri Platform** is a backend-focused web application built with **Django**. It aims to simplify agricultural operations by enabling farmers or stakeholders to manage crop data, monitor production, and interact through a central system. This project focuses on **core logic, database models, and admin management** — with minimal frontend.

---

## 📌 Features

- 🧾 Add and manage crop or product data
- 🔐 User authentication (login/register system)
- 📊 Built-in Django admin panel to manage all records
- 🛠️ Easily extendable backend logic for market data, weather integration, etc.
- 🧠 Designed for backend learning and model-view control

---

## 🛠️ Tech Stack

- **Backend Framework:** Django (Python)
- **Frontend:** Minimal HTML via Django templates
- **Database:** SQLite (default)
- **Tools:** Django Admin, CSRF security, Form handling

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Baumendhra/agri_platform.git
cd agri_platform

2. Set Up Virtual Environment

python -m venv venv
# Activate:
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

3. Install Dependencies

pip install -r requirements.txt

4. Apply Migrations

python manage.py makemigrations
python manage.py migrate

5. Run the Server

python manage.py runserver

Go to: http://127.0.0.1:8000


---

📂 Project Structure (Backend Focus)

agri_platform/
├── agri_platform/           # Main project config (settings, urls, wsgi)
├── agriapp/                 # Core app for models, views, admin, forms
│   ├── models.py            # Crop/Product data models
│   ├── views.py             # Backend logic and views
│   ├── admin.py             # Django admin setup
│   ├── forms.py             # Django form handling
│   ├── templates/           # Minimal frontend (optional)
│   └── static/              # Optional styling/js
├── db.sqlite3               # Local database
├── manage.py
└── requirements.txt

> Replace agriapp/ with your actual app name.




---

🛡️ Admin Panel

URL: http://127.0.0.1:8000/admin

Use a superuser to manage crops, users, and models visually.


To create a superuser:

python manage.py createsuperuser


---

🙋‍♂️ Author

Baumendhra K
🎓 Backend-Focused Developer
📧 baumendhra@gmail.com
🔗 GitHub • LinkedIn


---

📄 License

This project is licensed under the MIT License


---

✅ Note: Frontend is intentionally kept minimal to highlight backend logic. You are encouraged to expand it with React, Vue, or Django Templates later.

⭐ If you find this helpful, give it a star on GitHub!