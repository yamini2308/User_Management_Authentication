<<<<<<< HEAD
# Authentication System(Flask)

## Description
This Project is a simple user authentication system built usung Flask.

## Features

- Regester
- Login
- Logout
- Dashboard
- Password hashing
- Session Handling

## Technologies

- Python
- Flask
- SQLite
- HTML
- CSS

## Application Flow

1.User opens the application in the browser.

2.User is redirected to login page.

3.If User is new:

   - Clicks on Register
   - Enters username,email,password
   - Data is Stored in SQLite database

4.User logs in:
   - Enters username and password
   - System checks credentials with database
   - If correct --login Success
   - If Wrong --Error Message

5. After login:

   - User id redirected to dashboard
   - Dashboard shows "Welcome username"

6.Session Handling:

   - User seesion is created after login
   - Only logged -in users can access Dashboard

7.Logout:

   - User clicks logout
   - session is cleared
   - Redirected to login page

## Run

1.pip install flask 

2.python app.py

3.Open http://127.0.0.1:5000


=======
# User_Management_Authentication
>>>>>>> ddabb9407748cfd3670b8f1e597b17c58b6fd55a
