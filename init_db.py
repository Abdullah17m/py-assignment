import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('submissions.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create a table to store form submissions
cursor.execute('''
CREATE TABLE IF NOT EXISTS submissions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
)
''')

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database initialized and 'submissions' table created.")
