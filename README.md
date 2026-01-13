---

# CSV to SQLite Importer

---

## Features

* Reads user data from a CSV file
* Creates an SQLite database and table if they don’t exist
* Inserts or replaces records using a primary key
* Uses only Python standard libraries

---

## Requirements

* Python 3.x
* No external dependencies

---

## Project Structure

```text
.
├── users.csv
├── import_csv_to_sqlite.py
└── README.md
```

---

## CSV Format

The CSV file **must** be named `users.csv` and include the following headers:

```csv
ID,FirstName,LastName,Email,Gender
```

Example:

```csv
1,John,Doe,john.doe@example.com,Male
2,Jane,Smith,jane.smith@example.com,Female
```

---

## Database Schema

The script creates the following table:

```sql
CREATE TABLE users (
    ID TEXT PRIMARY KEY,
    FirstName TEXT,
    LastName TEXT,
    Email TEXT,
    Gender TEXT
);
```

---

## Usage

1. Place `users.csv` in the same directory as the script
2. Run the script:

```bash
python csvtosqlite.py
```

3. When prompted, enter the SQLite database name:

```text
Enter SQLite database name (with .db extension): users.db
```

---

## Output

* A new SQLite database file (e.g., `users.db`) is created
---
