import sqlite3

class Book:
    def __init__(self, name, author, year_published, book_type):
        self.name = name
        self.author = author
        self.year_published = year_published
        self.book_type = book_type

    @staticmethod
    def add_book(name, author, year_published, book_type):
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO Books (Name, Author, YearPublished, Type) 
                          VALUES (?, ?, ?, ?)''', (name, author, year_published, book_type))
        conn.commit()
        conn.close()

    @staticmethod
    def get_all_books():
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Books')
        books = cursor.fetchall()
        conn.close()
        return books

    @staticmethod
    def find_book_by_name(name):
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Books WHERE Name LIKE ?', ('%' + name + '%',))
        books = cursor.fetchall()
        conn.close()
        return books

    @staticmethod
    def remove_book(book_id):
        conn = sqlite3.connect('library.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM Books WHERE Id = ?', (book_id,))
        conn.commit()
        conn.close()
