# Bank-Application
Banking System is a Python-based application that simulates basic banking operations such as account creation, depositing, withdrawing, balance checking, and transfers. The system is implemented using classes to model the individual BankAccount and Bank classes. This project demonstrates key object-oriented principles like classes, methods, and error handling.

Features
BankAccount Class: Manages individual bank accounts with methods for:

Depositing: Add money to the account with error handling for invalid input types.
Withdrawing: Subtract money from the account, with checks for sufficient funds.
Check Balance: Display the current balance of the account.
Display Account Info: Show account number and current balance.
Bank Class: Manages a list of bank accounts and provides functionalities like:

Create Account: Allows the creation of a new account with an initial deposit greater than $300.
Get Account: Retrieve details of a specific account by entering the account number.
Deposit: Deposit money into a specific account.
Withdraw: Withdraw money from an account, ensuring sufficient balance.
Transfer: Transfer money between two accounts.
Bank Balance: Display the balance of an account after validation.
Error Handling
The system includes robust error handling using try and except to catch invalid input types and ensure operations are performed correctly.
If invalid account numbers or insufficient funds are encountered, the user is prompted with an error message and directed to the appropriate action.
Technologies Used
Python: Core language for implementing the banking logic.
Random: Used for generating random account numbers (for demonstration purposes).
Project Structure
BankAccount Class: Models individual bank accounts with attributes for account number and balance.
Bank Class: Manages multiple bank accounts and provides methods for various banking operations.
Menu Function: Displays a list of available operations.
Executive Choice: Processes user input and performs the requested operation.
Continution Operation Function: Recursively loops through operations to allow users to perform multiple actions in a single session.
