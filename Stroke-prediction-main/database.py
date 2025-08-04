import sqlite3
def get_db_connection():
    """Establish and return a database connection."""
    return sqlite3.connect('history.db')

def init_db():
    """Initialize the database and create the prediction_history table if it doesn't exist."""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS prediction_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                age INTEGER,
                maritalstatus TEXT,
                worktype TEXT,
                residence TEXT,
                gender TEXT,
                bmi REAL,
                gluclevel INTEGER,
                smoke TEXT,
                hypertension TEXT,
                heartdisease TEXT,
                prediction_result TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()
        print("Database initialized successfully.")
    except sqlite3.Error as e:
        print("Error initializing database:", e)
    finally:
        conn.close()

def insert_history(name, age, maritalstatus, worktype, residence, gender, bmi, gluclevel, smoke, hypertension, heartdisease, prediction_result):
    """Insert a new record into the prediction_history table."""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO prediction_history (
                name, age, maritalstatus, worktype, residence, gender, bmi, gluclevel, smoke, hypertension, heartdisease, prediction_result
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (name, age, maritalstatus, worktype, residence, gender, bmi, gluclevel, smoke, hypertension, heartdisease, prediction_result))
        conn.commit()
        print("Record inserted successfully.")
    except sqlite3.Error as e:
        print("Error inserting record:", e)
    finally:
        conn.close()

# Initialize the database (call this once)
init_db()





















# import sqlite3
#
#
# def init_db():
#     conn = sqlite3.connect('history.db')  # Connect to SQLite database
#     cursor = conn.cursor()
#
#     # Create a table to store user predictions
#     cursor.execute('''
#     CREATE TABLE IF NOT EXISTS prediction_history (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT,
#         age INTEGER,
#         maritalstatus TEXT,
#         worktype TEXT,
#         residence TEXT,
#         gender TEXT,
#         bmi REAL,
#         gluclevel INTEGER,
#         smoke TEXT,
#         hypertension TEXT,
#         heartdisease TEXT,
#         prediction_result TEXT,
#         timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
#     )
#     ''')
#
#     conn.commit()
#     conn.close()
#
#
# def insert_history(name, age, maritalstatus, worktype, residence, gender, bmi, gluclevel, smoke, hypertension,
#                    heartdisease, prediction_result):
#     conn = sqlite3.connect('history.db')
#     cursor = conn.cursor()
#
#     cursor.execute('''
#     INSERT INTO prediction_history (name, age, maritalstatus, worktype, residence, gender, bmi, gluclevel, smoke, hypertension, heartdisease, prediction_result)
#     VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
#                    (name, age, maritalstatus, worktype, residence, gender, bmi, gluclevel, smoke, hypertension,
#                     heartdisease, prediction_result))
#
#     conn.commit()
#     conn.close()
#
#
# # Initialize the database (call this function once)
# init_db()
