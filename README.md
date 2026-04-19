# Starbucks Nutrition API

**XJCO3011 Web Services and Web Data - Coursework 1**

## Project Overview
This project is a fully functional data-driven RESTful Web API built with **Django** and **Django REST Framework (DRF)**. It provides comprehensive CRUD (Create, Read, Update, Delete) operations for a Starbucks Menu Nutrition dataset. The API allows users to query, add, modify, and delete beverage nutritional information (such as calories, fat, sugar, and caffeine) systematically.

## Key Features
* **Complete CRUD Functionality**: Fully implements RESTful principles for managing beverage data.
* **Interactive API Documentation**: Integrated with Swagger UI for seamless endpoint exploration and testing.
* **Automated Data Import**: Includes a Python script to populate the SQLite database from a raw CSV dataset.

##  API Documentation
The comprehensive API documentation details all available endpoints, parameters, and expected JSON responses. 
**Please refer to the attached PDF file for the full documentation:**  [`API_Documentation.pdf`](./API_Documentation.pdf)

## Setup and Installation Instructions

Follow these steps to run the API locally on your machine:

**1. Clone the repository**
> git clonehttps://github.com/planeboom/XJCO3011.git
> cd XJCO3011

**2. Set up a virtual environment (Optional but recommended)**
> python -m venv venv
> venv\Scripts\activate

**3. Install dependencies**
> pip install django djangorestframework drf-yasg pandas

**4. Run database migrations**
> python manage.py makemigrations
> python manage.py migrate

**5. Import the Starbucks dataset**
Ensure `starbucks.csv` is in the root directory, then run:
> python import_data.py

**6. Start the development server**
> python manage.py runserver

**7. Access the API**
* Open your browser and navigate to: `http://127.0.0.1:8000/` (This will automatically redirect to the interactive Swagger API documentation).
* To access the raw data endpoints directly, visit: `http://127.0.0.1:8000/api/beverages/`