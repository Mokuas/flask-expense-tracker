# flask-expense-tracker
Flask Expense Tracker is a simple and lightweight web application built with Flask that helps users manage their personal expenses and categories. The project demonstrates essential CRUD operations, database management using SQLAlchemy, and a clean frontend styled with SCSS. It is designed to be easy to run locally while maintaining professional coding practices, including testing and continuous integration.

The main features of this application include the ability to add, edit, and delete expense categories, as well as record expenses with descriptions, dates, and amounts. The interface is simple, clean, and responsive, styled with SCSS for better readability and modern aesthetics. The application uses an SQLite database for simplicity, making it ideal for small projects or personal finance tracking.

From a technical perspective, Flask Expense Tracker is built using Python 3.11, Flask, Flask-SQLAlchemy, and Flask-Scss. It includes a complete test suite using pytest to ensure stability and reliability. Every push or pull request automatically triggers the test suite through GitHub Actions, ensuring that the application remains functional and bug-free during future development.

To run the project locally, clone the repository using the command git clone https://github.com/Mokuas/flask-expense-tracker.git and navigate to the project directory. Then, create a virtual environment with python -m venv .venv and activate it. After activation, install the dependencies listed in requirements-dev.txt using pip install -r requirements-dev.txt. Once the setup is complete, you can start the Flask server by running python app.py.

Testing is fully integrated into the development process. You can run all tests locally by executing the command pytest. The tests validate core functionalities such as category creation, expense addition, and proper form validation. The CI workflow configured with GitHub Actions ensures that these tests are executed automatically for every commit or pull request, providing immediate feedback on the code quality.

The project structure is organized into logical folders, including templates for HTML files, static for styles, tests for pytest files, and .github/workflows for CI configurations. This separation enhances maintainability and scalability, making it easy to extend the app with new features.

Future improvements planned for Flask Expense Tracker include adding monthly summaries and visual charts, exporting expenses to CSV or Excel files, implementing user authentication, and enhancing the SCSS theme system for customization.

This project is licensed under the MIT License, allowing free use, modification, and distribution with proper attribution. Flask Expense Tracker aims to serve as a clean, minimalistic, and well-tested example of how to build a professional Flask web application from scratch, complete with testing and continuous integration.
