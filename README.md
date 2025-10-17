
# 🌍 TravellersXperience

**TravellersXperience** is a Django-based travel platform designed to connect travelers with unique experiences, destinations, reviews, etc. The project is being developed as part of the ALX Django Learning Lab Capstone.


## 🚀 Project Overview

This project aims to provide a RESTful API that allows users to:
- Register and log in as travelers.
- View, create, and manage travel experiences.
- Post and read reviews from other travelers.
- Handle bookings and payments (future feature).

It’s built using the Django REST Framework, following clean and modular design principles.

---

## 🧱 Tech Stack

- **Backend:** Django 5 + Django REST Framework  
- **Authentication:** JWT (using `djangorestframework-simplejwt`)  
- **Database:** SQLite (development)  
- **Version Control:** Git & GitHub  
- **Environment:** Virtualenv + VS Code  

---

## 📁 Project Structure


## 🏝️ TravellersXperience.com Project Flowchart


👉 [View the full interactive diagram on Figma] (https://www.figma.com/board/THXM3MguFA7gHqlh1wIrVC/TravellersXperience-Logo-Flow?node-id=0-1)

![TravellersXperience Diagram] (https://figma.com/file/THXM3MguFA7gHqlh1wIrVC/preview.png)


TravellersXperience/
├── manage.py
├── TravellersXperience/ # Main project configuration
├── users/ # Custom user model & auth endpoints
├── payments/ # Payment handling (coming soon)
├── reviews/ # Travel experience reviews
├── static/ # Static files directory
└── venv/ # Virtual environment



## ⚙️ Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Freddanjuma/TravellersXperience.git
   cd TravellersXperience


Create & activate a virtual environment:

python -m venv venv
venv\Scripts\activate


Install dependencies:

pip install -r requirements.txt


Run migrations:

python manage.py makemigrations
python manage.py migrate


Start the development server:

python manage.py runserver

🔐 Authentication Endpoints
Endpoint	Method	Description
/api/register/	POST	Register a new user
/api/token/	POST	Obtain JWT token
/api/token/refresh/	POST	Refresh JWT token


💡 Next Steps

Implement reviews and payments apps.

Add booking and destination models.

Write automated unit tests for API endpoints.

Deploy on Render or Railway for live demo.


🧑‍💻 Author

Developer: Fred Danjuma
GitHub: https://github.com/Freddanjuma


Project Repo: TravellersXperience


📜 License

This project is part of the ALX Django Learning Lab Capstone Project and is for educational purposes.

