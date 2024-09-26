from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
import os
from datetime import datetime
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Required for flashing messages

# Connect to the SQLite database
DATABASE = 'submissions.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# Function to fetch weather data from OpenWeatherMap API
def get_weather():
    api_key = os.getenv('OPENWEATHER_API_KEY')   # Replace with your OpenWeatherMap API key
    url = f"http://api.openweathermap.org/data/2.5/weather?q=london&appid={api_key}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        weather = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"]
        }
        return weather
    else:
        return None

# Home route - Index page
@app.route('/')
def index():
    # Fetch weather information (dummy data or API can be used)
    weather = get_weather()

    # Current date and time
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return render_template('index.html', current_time=current_time, weather=weather)

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']

    # Insert data into the SQLite database
    conn = get_db_connection()
    try:
        conn.execute('INSERT INTO submissions (name, email) VALUES (?, ?)', (name, email))
        conn.commit()
        flash('Form submitted successfully!')
    except sqlite3.IntegrityError:
        flash('Error: The email is already registered. Please use a different email.')
    finally:
        conn.close()

    return redirect(url_for('index'))

# Route to display form submissions
@app.route('/submissions')
def submissions():
    conn = get_db_connection()
    submissions = conn.execute('SELECT * FROM submissions').fetchall()
    conn.close()

    return render_template('submissions.html', submissions=submissions)


if __name__ == '__main__':
    app.run(debug=True)
