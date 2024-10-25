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

2. Start the development server:
```bash
python manage.py runserver
```
The API will be available at `http://127.0.0.1:8000/`

## Functionalities Implemented
* User registration and management
* Creation and retrieval of expenses
* Support for multiple users associated with each expense
* Various expense splitting methods: equal, exact, and percentage
* Viewing and downloading a balance sheet of expenses in CSV format

## Tech Stack Used
* **Backend:** Django, Django REST Framework
* **Database:** MySQL (or any other database supported by Django)

## API Endpoints

### User Management
| Endpoint | Method | URL | Description |
|----------|--------|-----|-------------|
| Create User | POST | `/users/` | Create a new user with email, name, and mobile number |
| Get User Details | GET | `/users/<int:pk>/` | Retrieve details of a specific user by ID |

### Expense Management
| Endpoint | Method | URL | Description |
|----------|--------|-----|-------------|
| List All Expenses | GET | `/expenses/` | Get a list of all expenses |
| Create Expense | POST | `/expenses/create/` | Create a new expense |
| Get Expense Details | GET | `/expenses/<int:pk>/` | Get details of a specific expense |

### Balance Sheet
| Endpoint | Method | URL | Description |
|----------|--------|-----|-------------|
| Download Balance Sheet | GET | `/balance_sheet/download/` | Download balance sheet as CSV |

### Detailed Endpoint Specifications

#### User Endpoints

##### Create User
* **URL:** `/users/`
* **Method:** `POST`
* **Request Body:**
```json
{
    "email": "user@example.com",
    "name": "John Doe",
    "mobile_number": "1234567890"
}
```
* **Success Response:** Returns created user details with ID

##### Get User Details
* **URL:** `/users/<int:pk>/`
* **Method:** `GET`
* **URL Parameters:** `pk=[integer]` where `pk` is the user's ID
* **Success Response:** Returns user details with their expense contributions

#### Expense Endpoints

##### List Expenses
* **URL:** `/expenses/`
* **Method:** `GET`
* **Success Response:** Returns list of all expenses with details

##### Create Expense
* **URL:** `/expenses/create/`
* **Method:** `POST`
* **Request Body:**
```json
{
    "title": "Dinner",
    "amount": 100.00,
    "split_type": "EQUAL",
    "users": [1, 2, 3],
    "splits": []
}
```
* **Success Response:** Returns created expense details

##### Get Expense Details
* **URL:** `/expenses/<int:pk>/`
* **Method:** `GET`
* **URL Parameters:** `pk=[integer]` where `pk` is the expense ID
* **Success Response:** Returns specific expense details

#### Balance Sheet Endpoints

##### View Balance Sheet
* **URL:** `/balance_sheet/`
* **Method:** `GET`
* **Success Response:** Returns complete balance sheet with all expenses

##### Download Balance Sheet
* **URL:** `/balance_sheet/download/`
* **Method:** `GET`
* **Success Response:** Returns CSV file with balance sheet data

## User Contributions
Each user can view their contributions towards different expenses. The contributions are returned as part of the user details, showing how much they have contributed to various expenses along with the expense details.
