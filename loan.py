import sqlite3
from datetime import datetime, timedelta

class Loan:
    @staticmethod
    def loan_book(cust_id, book_id):
        loan_date = datetime.now().strftime('%Y-%m-%d')
        return_date = None

        # Get book type to determine max loan time
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        cursor.execute('SELECT Type FROM Books WHERE Id = ?', (book_id,))
        book_type = cursor.fetchone()[0]
        conn.close()

        if book_type == 1:
            return_date = (datetime.now() + timedelta(days=10)).strftime('%Y-%m-%d')
        elif book_type == 2:
            return_date = (datetime.now() + timedelta(days=5)).strftime('%Y-%m-%d')
        elif book_type == 3:
            return_date = (datetime.now() + timedelta(days=2)).strftime('%Y-%m-%d')

        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO Loans (CustID, BookID, LoanDate, ReturnDate) 
                          VALUES (?, ?, ?, ?)''', (cust_id, book_id, loan_date, return_date))
        conn.commit()
        conn.close()

    @staticmethod
    def return_book(cust_id, book_id):
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM Loans WHERE CustID = ? AND BookID = ?', (cust_id, book_id))
        conn.commit()
        conn.close()

    @staticmethod
    def get_all_loans():
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Loans')
        loans = cursor.fetchall()
        conn.close()
        return loans

    @staticmethod
    def get_late_loans():
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Loans WHERE ReturnDate < ?', (datetime.now().strftime('%Y-%m-%d'),))
        late_loans = cursor.fetchall()
        conn.close()
        return late_loans
