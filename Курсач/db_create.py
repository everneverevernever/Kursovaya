import sqlite3

# Connect to the database (creates a new file if not exists)
conn = sqlite3.connect('telecom_database.db')
cursor = conn.cursor()

# Execute the SQL queries to create tables
cursor.execute('''
    CREATE TABLE Clients (
        id INTEGER PRIMARY KEY,
        contract_number TEXT,
        full_name TEXT,
        balance REAL,
        phone_number TEXT,
        email TEXT,
        address TEXT
    )
''')

cursor.execute('''
    CREATE TABLE ServiceTypes (
        id INTEGER PRIMARY KEY,
        service_type TEXT
    )
''')

cursor.execute('''
    CREATE TABLE Services (
        id INTEGER PRIMARY KEY,
        service_type_id INTEGER,
        description TEXT,
        price REAL,
        FOREIGN KEY (service_type_id) REFERENCES ServiceTypes(id)
    )
''')

cursor.execute('''
    CREATE TABLE Agreements (
        id INTEGER PRIMARY KEY,
        client_id INTEGER,
        service_id INTEGER,
        agreement_date DATE,
        FOREIGN KEY (client_id) REFERENCES Clients(id),
        FOREIGN KEY (service_id) REFERENCES Services(id)
    )
''')

cursor.execute('''
    CREATE TABLE Staff (
        id INTEGER PRIMARY KEY,
        username TEXT,
        full_name TEXT,
        mail TEXT,
        password TEXT,
        access_level INTEGER DEFAULT 1
    )
''')

cursor.execute('''
INSERT INTO Staff (username, full_name, mail, password, access_level)
VALUES ('gleb_zaytsev', 'Глеб Зайцев Владиславович', 'gleb.zaytsev@example.com', 'password123', 3);
''')

# Commit the changes and close the connection
conn.commit()
conn.close()
