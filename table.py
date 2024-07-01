import sqlite3

def create_tables():
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()

    # Create Books table
    cursor.execute('''CREATE TABLE IF NOT EXISTS Books (
                        Id INTEGER PRIMARY KEY AUTOINCREMENT,
                        Name TEXT NOT NULL,
                        Author TEXT NOT NULL,
                        YearPublished INTEGER NOT NULL,
                        Type INTEGER NOT NULL
                      )''')

    # Create Customers table
    cursor.execute('''CREATE TABLE IF NOT EXISTS Customers (
                        Id INTEGER PRIMARY KEY AUTOINCREMENT,
                        Name TEXT NOT NULL,
                        City TEXT NOT NULL,
                        Age INTEGER NOT NULL
                      )''')

    # Create Loans table
    cursor.execute('''CREATE TABLE IF NOT EXISTS Loans (
                        CustID INTEGER NOT NULL,
                        BookID INTEGER NOT NULL,
                        LoanDate TEXT NOT NULL,
                        ReturnDate TEXT,
                        FOREIGN KEY (CustID) REFERENCES Customers(Id),
                        FOREIGN KEY (BookID) REFERENCES Books(Id)
                      )''')

    conn.commit()
    conn.close()

create_tables()
