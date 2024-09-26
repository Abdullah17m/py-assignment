# Flask Web Application with Form Handling and SQLite Database

This is a simple web application built using Flask that allows users to submit their details (name and email) via a form. It also fetches weather information from the OpenWeatherMap API and stores submitted form data in an SQLite database.

## Table of Contents

1. [Installation](#installation)
2. [Database Initialization](#database-initialization)
3. [Project Structure](#project-structure)
4. [Running the Application](#running-the-application)
5. [Routes Explanation](#routes-explanation)


## Installation

### Step 1: Clone the repository

```bash
git clone https://github.com/yourusername/flask-web-app.git
cd flask-web-app
```

### Step 2: Install the required dependencies

Install the required Python libraries using `pip`:

```bash
pip install Flask requests python-dotenv
```

### Step 3: Initialize the database

Run the `init_db.py` script to create the `submissions` table in the SQLite database.

```bash
py init_db.py
```

### Project Structure
```bash
.
├── app.py                # Main Flask application
├── init_db.py            # Script to initialize the SQLite database
├── submissions.db         # SQLite database (created after running init_db.py)
├── templates
│   ├── index.html         # Home page template
│   └── submissions.html   # Page to display all form submissions
├── static
│   └── styles.css         # Basic CSS styles for the web pages
├── .env                   # Environment file for storing sensitive keys
└── README.md              # Project documentation
```

### Running The Application

After initializing the database, you can run the Flask web server to start the application:

```bash
py app.py
```

### Routes Explanation

`/` - Home Page
Method: `GET`
Description: Displays the home page with the form for submitting user details (name and email) and dynamic content such as the current date/time and weather information.
Features:
- Displays weather information fetched from OpenWeatherMap API.
- Shows a form to submit user details.
- Displays success or error messages if applicable.


 `/submit` - Form Submission
Method: `POST`
Description: Handles the form submission. It validates the form data and attempts to insert it into the SQLite database. If the email already exists (unique constraint), an error message will be shown.
Features:
- Inserts user details (name and email) into the database.
- Handles duplicate email submission errors and shows appropriate messages.


`/submissions` - View Submitted Data
Method: `GET`
Description: Displays a list of all form submissions from the SQLite database.
Features:
- Retrieves and displays all user submissions from the database in a tabular format.


