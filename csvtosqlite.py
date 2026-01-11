import csv
import sqlite3

CSV_FILE = "users.csv"
DB_FILE = input("Enter SQLite database name (with .db extension): ")

# Connect to SQLite
conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    ID TEXT PRIMARY KEY,
    FirstName TEXT,
    LastName TEXT,
    Email TEXT,
    Gender TEXT
);
""")
conn.commit()

# Read CSV and insert data
with open(CSV_FILE, newline='', encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        cursor.execute("""
        INSERT OR REPLACE INTO users (ID, FirstName, LastName, Email, Gender)
        VALUES (?, ?, ?, ?, ?)
        """, (
            row["ID"],
            row["FirstName"],
            row["LastName"],
            row["Email"],
            row["Gender"]
        ))

conn.commit()
conn.close()

print(f"CSV data successfully imported into SQLite database: {DB_FILE}")