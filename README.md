# Django Expense Tracker Project

## Project Overview
This project is an expense tracker application built using Django. It allows users to create and manage their expenses, track contributions from multiple users, and generate balance sheets. The application supports various expense splitting methods, including equal sharing, exact amounts, and percentage splits.

## Project Setup

### Prerequisites
* Python 3.10
* Conda package manager
* MySQL (or another supported database)

### Environment Setup
1. Clone the repository:
```bash
git clone https://github.com/Prajjawal12/Shared-Expenses-API.git
cd Shared-Expenses-API
```

2. Create and activate a Conda environment:
```bash
conda create -n expense-tracker python=3.8
conda activate expense-tracker
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

### Database Configuration
1. Create a new MySQL database for the project
2. Update database settings in `settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### Running the Project
1. Apply migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

2. Create a superuser (optional):
```bash
python manage.py createsuperuser
```

3. Start the development server:
```bash
python manage.py runserver
```

The API will be available at `http://localhost:8000/`

## Functionalities Implemented
* User registration and management
* Creation and retrieval of expenses
* Support for multiple users associated with each expense
* Various expense splitting methods: equal, exact, and percentage
* Viewing and downloading a balance sheet of expenses in CSV format

## Tech Stack Used
* **Backend:** Django, Django REST Framework
* **Database:** MySQL (or any other database supported by Django)

## Endpoints Description

### User Endpoints

#### Create User
* **Endpoint:** `POST /users/`
* **Description:** This endpoint allows the creation of a new user. It expects user details like email, name, and mobile number in the request body.
* **Response:** A confirmation response with the created user's ID, email, name, and mobile number.

#### Get User Details
* **Endpoint:** `GET /users/<int:pk>/`
* **Description:** Retrieves the details of a specific user by their ID.
* **Response:** User details including contributions towards expenses.

### Expense Endpoints

#### List Expenses
* **Endpoint:** `GET /expenses/`
* **Description:** This endpoint returns a list of all expenses recorded in the application.
* **Response:** A list of expenses with details such as title, amount, users involved, and splitting meth
