Sure! Here's an updated README for your library project at `https://github.com/MaozGrama/LibraryProject.git`.

```markdown
# Library Management System

A simple library management system built using Flask for the web framework, SQLite for the database, and Bootstrap for styling. This system allows you to manage books, customers, and loans efficiently.

## Features

- Add a new customer
- Add a new book
- Loan a book
- Return a book
- Display all books
- Display all customers
- Display all loans
- Display late loans
- Find book by name
- Find customer by name
- Remove book
- Remove customer

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/MaozGrama/LibraryProject.git
   cd LibraryProject
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the SQLite database:
   ```bash
   python setup_database.py
   ```

## Usage

1. Run the Flask application:
   ```bash
   python app.py
   ```

2. Open your web browser and navigate to `http://127.0.0.1:5000/` to use the library management system.

## Project Structure

- `app.py`: Main application file that sets up the Flask routes.
- `setup_database.py`: Script to set up the SQLite database.
- `models/`: Directory containing the data access layer (DAL) classes for `Book`, `Customer`, and `Loan`.
- `templates/`: Directory containing the HTML templates for different pages.
- `static/`: Directory containing static files such as CSS and JavaScript (if any).

## Data Access Layer (DAL)

The DAL consists of three classes to interact with the database:

- `models/book.py`: Class to handle book-related operations.
- `models/customer.py`: Class to handle customer-related operations.
- `models/loan.py`: Class to handle loan-related operations.

## HTML Templates

The HTML templates use Bootstrap for styling and are organized as follows:

- `base.html`: Base template with the navigation bar and Bootstrap includes.
- `index.html`: Home page template.
- `add_customer.html`: Template to add a new customer.
- `add_book.html`: Template to add a new book.
- `loan_book.html`: Template to loan a book.
- `return_book.html`: Template to return a book.
- `view_books.html`: Template to view all books.
- `view_customers.html`: Template to view all customers.
- `view_loans.html`: Template to view all loans.
- `view_late_loans.html`: Template to view late loans.
- `find_book.html`: Template to find a book by name.
- `find_customer.html`: Template to find a customer by name.
- `remove_book.html`: Template to remove a book.
- `remove_customer.html`: Template to remove a customer.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```

Ensure you adjust the content based on the actual structure and specifics of your project as needed.