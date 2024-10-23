# Django Expense Tracker Project
**Author:** Prajjawal Deep Yadav  
**Date:** Today

## Project Overview
This project is an expense tracker application built using Django. It allows users to create and manage their expenses, track contributions from multiple users, and generate balance sheets. The application supports various expense splitting methods, including equal sharing, exact amounts, and percentage splits.

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
* **Response:** A list of expenses with details such as title, amount, users involved, and splitting method.

#### Create Expense
* **Endpoint:** `POST /expenses/create/`
* **Description:** Allows the creation of a new expense. It expects details such as title, amount, users involved, and the splitting method.
* **Response:** Confirmation response with details of the created expense.

#### Get Expense Details
* **Endpoint:** `GET /expenses/<int:pk>/`
* **Description:** Retrieves details of a specific expense by its ID.
* **Response:** Expense details including title, amount, users involved, and splitting method.

### Balance Sheet Endpoints

#### View Balance Sheet
* **Endpoint:** `GET /balance_sheet/`
* **Description:** This endpoint provides an overview of all expenses and their details.
* **Response:** A list of expenses with relevant details.

#### Download Balance Sheet
* **Endpoint:** `GET /balance_sheet/download/`
* **Description:** This endpoint allows users to download their balance sheet in CSV format.
* **Response:** A CSV file containing the balance sheet data, including expense titles, amounts, and splitting details.

## User Contributions
Each user can view their contributions towards different expenses. The contributions are returned as part of the user details, showing how much they have contributed to various expenses along with the expense details.
