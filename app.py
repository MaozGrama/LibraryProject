from flask import Flask, render_template, request, redirect, url_for
from book import Book
from customer import Customer
from loan import Loan

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_customer', methods=['GET', 'POST'])
def add_customer():
    if request.method == 'POST':
        name = request.form['name']
        city = request.form['city']
        age = int(request.form['age'])
        Customer.add_customer(name, city, age)
        return redirect(url_for('index'))
    return render_template('add_customer.html')

@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        name = request.form['name']
        author = request.form['author']
        year_published = int(request.form['year_published'])
        book_type = int(request.form['book_type'])
        Book.add_book(name, author, year_published, book_type)
        return redirect(url_for('index'))
    return render_template('add_book.html')

@app.route('/loan_book', methods=['GET', 'POST'])
def loan_book():
    if request.method == 'POST':
        cust_id = int(request.form['cust_id'])
        book_id = int(request.form['book_id'])
        Loan.loan_book(cust_id, book_id)
        return redirect(url_for('index'))
    return render_template('loan_book.html')

@app.route('/return_book', methods=['GET', 'POST'])
def return_book():
    if request.method == 'POST':
        cust_id = int(request.form['cust_id'])
        book_id = int(request.form['book_id'])
        Loan.return_book(cust_id, book_id)
        return redirect(url_for('index'))
    return render_template('return_book.html')

@app.route('/view_books')
def view_books():
    books = Book.get_all_books()
    return render_template('view_books.html', books=books)

@app.route('/view_customers')
def view_customers():
    customers = Customer.get_all_customers()
    return render_template('view_customers.html', customers=customers)

@app.route('/view_loans')
def view_loans():
    loans = Loan.get_all_loans()
    return render_template('view_loans.html', loans=loans)

@app.route('/view_late_loans')
def view_late_loans():
    late_loans = Loan.get_late_loans()
    return render_template('view_late_loans.html', late_loans=late_loans)

@app.route('/find_book', methods=['GET', 'POST'])
def find_book():
    if request.method == 'POST':
        name = request.form['name']
        books = Book.find_book_by_name(name)
        return render_template('view_books.html', books=books)
    return render_template('find_book.html')

@app.route('/find_customer', methods=['GET', 'POST'])
def find_customer():
    if request.method == 'POST':
        name = request.form['name']
        customers = Customer.find_customer_by_name(name)
        return render_template('view_customers.html', customers=customers)
    return render_template('find_customer.html')

@app.route('/remove_book', methods=['GET', 'POST'])
def remove_book():
    if request.method == 'POST':
        book_id = int(request.form['book_id'])
        Book.remove_book(book_id)
        return redirect(url_for('view_books'))
    return render_template('remove_book.html')

@app.route('/remove_customer', methods=['GET', 'POST'])
def remove_customer():
    if request.method == 'POST':
        customer_id = int(request.form['customer_id'])
        Customer.remove_customer(customer_id)
        return redirect(url_for('view_customers'))
    return render_template('remove_customer.html')

if __name__ == '__main__':
    app.run(debug=True)
