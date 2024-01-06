# Clinic-Management-System

Patient Information Management System

Overview

This Python application offers a user-friendly interface for managing patient information. It enables admins to perform various tasks, including:

Creating new patient accounts
Viewing patient details
Updating patient information
Deleting patient records
Generating a graph to visualize patient distribution by gender
Key Features

Stores patient data in CSV files for easy access and management
Leverages pandas for efficient data manipulation
Utilizes matplotlib for creating informative graphs
Provides a clear menu-driven interface for user interaction
Requirements

Python 3.x
pandas library
matplotlib library
Getting Started

Install the required libraries:
Bash
pip install pandas matplotlib
Use code with caution. Learn more
Run the application:
Bash
python main.py
Use code with caution. Learn more
Usage

Upon launch, the application prompts for admin login.
After successful login, the main menu presents the following options:
Create Patient Account
Patient Details
Update Patient Account
Delete Patient Details
Graph
Exit
Select the desired option and follow the prompts to execute the corresponding action.
CSV Files

Patients_Details.csv: Stores patient information, including ID, name, gender, date of birth, contact details, email, allergies, and registration date.
Admin_Details.csv: Stores admin login credentials.
Code Structure

import: Imports necessary libraries (pandas, matplotlib, and datetime).
DataFrame Creation: Reads CSV files into pandas DataFrames for patient and admin details.
Functions: Defines functions for various tasks: - create_patient_account(): Creates a new patient account. - update_patient_details(): Updates existing patient information. - patient_details(): Displays patient details based on email and password. - patient_delete(): Deletes a patient record. - graph(): Generates a bar graph showing patient distribution by gender. - menu(): Provides the main user interface with options for actions. - admin_login(): Handles admin login and initiates the main menu.
Main Execution: Starts with admin_login() to prompt for credentials and begin the application flow.
Additional Notes

Ensure CSV files are present in the CSV subdirectory.
Passwords are stored in plain text in CSV files; consider more secure methods for production environments.
Further enhancements could include:
Error handling
Data validation
Additional features (e.g., searching, filtering, reporting)
