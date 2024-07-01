import unittest
from book import Book
from customer import Customer
from loan import Loan

class TestLibrary(unittest.TestCase):

    def test_add_and_get_book(self):
        Book.add_book('Test Book', 'Test Author', 2023, 1)
        books = Book.get_all_books()
        self.assertTrue(any(book[1] == 'Test Book' for book in books))

    def test_add_and_get_customer(self):
        Customer.add_customer('Test Customer', 'Test City', 30)
        customers = Customer.get_all_customers()
        self.assertTrue(any(customer[1] == 'Test Customer' for customer in customers))

    def test_loan_and_return_book(self):
        # Assume there is a customer with ID 1 and a book with ID 1
        Loan.loan_book(1, 1)
        loans = Loan.get_all_loans()
        self.assertTrue(any(loan[0] == 1 and loan[1] == 1 for loan in loans))
        Loan.return_book(1, 1)
        loans = Loan.get_all_loans()
        self.assertFalse(any(loan[0] == 1 and loan[1] == 1 for loan in loans))

if __name__ == '__main__':
    unittest.main()
