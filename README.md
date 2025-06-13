Airline Management System
This is a simple command-line Airline Management System built with Python and SQLite3. It allows users to log in, sign up, and provides different functionalities for administrators and regular users.

Features
User Authentication:
Login: Existing users can log in using their ID and email.
Sign Up: New users can create an account by providing their name, ID, and email.
Role-Based Access:
Admin Access: Users with specific email addresses (defined in admin_emails) are granted administrator privileges.
User Access: Regular users have access to standard flight management features.
Admin Dashboard (Placeholders):
Carrier management
Flight management
User management
Booking management
User Dashboard (Placeholders):
View Flights
Book Flights
Cancel Booking
Getting Started
Prerequisites
Python 3.x installed on your system.
Installation
Save the code: Save the provided Python code as a .py file (e.g., airline_management.py).
Running the Application
Open a terminal or command prompt.

Navigate to the directory where you saved the airline_management.py file.

Run the script using the Python interpreter:

Bash

python airline_management.py
How to Use
Upon running the application, you'll be presented with the main menu:

Welcome to Airline Management
---------------------------------------------
1. Log in
2. Sign up
3. Exit Airlines
---------------------------------------------
1. Sign Up
Select option 2 from the main menu.
Enter your desired name, ID, and email.
A new user account will be created.
2. Log In
Select option 1 from the main menu.
Enter your registered ID and email.
If your credentials are valid:
If your email is one of the admin_emails (currently arunsan2012@gmail.com or arunsan.v@tcs.com), you will access the Admin Menu.
Otherwise, you will access the User Menu.
3. Exiting the Application
Select option 3 from the main menu to exit the application.
Database
The system uses an SQLite3 database named usad.db.
A table named user is created automatically if it doesn't exist, with the following columns:

name (TEXT, not null)
idn (INTEGER, not null)
email (TEXT, not null, unique)
Future Enhancements
The current system provides a basic framework. Here are some potential areas for improvement:

Implement the actual functionalities for "Carrier management," "Flight management," "User Management," and "booking management" in the admin section.
Implement "View Flights," "Book Flights," and "Cancel Booking" functionalities for regular users.
Add more robust error handling and input validation.
Implement password hashing for user security.
Develop a more comprehensive user interface (e.g., using a GUI library).
Add features for flight search, filtering, and sorting.
Include seat selection and payment processing.

------------------------------------------------------------------------------------------------------------------------------------------------------------------

Feel free to contribute or suggest further improvements!

