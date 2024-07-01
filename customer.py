import sqlite3

class Customer:
    def __init__(self, name, city, age):
        self.name = name
        self.city = city
        self.age = age

    @staticmethod
    def add_customer(name, city, age):
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO Customers (Name, City, Age) 
                          VALUES (?, ?, ?)''', (name, city, age))
        conn.commit()
        conn.close()

    @staticmethod
    def get_all_customers():
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Customers')
        customers = cursor.fetchall()
        conn.close()
        return customers

    @staticmethod
    def find_customer_by_name(name):
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Customers WHERE Name LIKE ?', ('%' + name + '%',))
        customers = cursor.fetchall()
        conn.close()
        return customers

    @staticmethod
    def remove_customer(customer_id):
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM Customers WHERE Id = ?', (customer_id,))
        conn.commit()
        conn.close()
