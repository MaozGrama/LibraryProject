from book import Book
from customer import Customer
from loan import Loan

def display_menu():
    print("Library Management System")
    print("1. Add a new customer")
    print("2. Add a new book")
    print("3. Loan a book")
    print("4. Return a book")
    print("5. Display all books")
    print("6. Display all customers")
    print("7. Display all loans")
    print("8. Display late loans")
    print("9. Find book by name")
    print("10. Find customer by name")
    print("11. Remove book")
    print("12. Remove customer")
    print("0. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter customer name: ")
            city = input("Enter customer city: ")
            age = int(input("Enter customer age: "))
            Customer.add_customer(name, city, age)
        
        elif choice == '2':
            name = input("Enter book name: ")
            author = input("Enter book author: ")
            year_published = int(input("Enter year published: "))
            book_type = int(input("Enter book type (1/2/3): "))
            Book.add_book(name, author, year_published, book_type)
        
        elif choice == '3':
            cust_id = int(input("Enter customer ID: "))
            book_id = int(input("Enter book ID: "))
            Loan.loan_book(cust_id, book_id)
        
        elif choice == '4':
            cust_id = int(input("Enter customer ID: "))
            book_id = int(input("Enter book ID: "))
            Loan.return_book(cust_id, book_id)
        
        elif choice == '5':
            books = Book.get_all_books()
            for book in books:
                print(book)
        
        elif choice == '6':
            customers = Customer.get_all_customers()
            for customer in customers:
                print(customer)
        
        elif choice == '7':
            loans = Loan.get_all_loans()
            for loan in loans:
                print(loan)
        
        elif choice == '8':
            late_loans = Loan.get_late_loans()
            for late_loan in late_loans:
                print(late_loan)
        
        elif choice == '9':
            name = input("Enter book name: ")
            books = Book.find_book_by_name(name)
            for book in books:
                print(book)
        
        elif choice == '10':
            name = input("Enter customer name: ")
            customers = Customer.find_customer_by_name(name)
            for customer in customers:
                print(customer)
        
        elif choice == '11':
            book_id = int(input("Enter book ID to remove: "))
            Book.remove_book(book_id)
        
        elif choice == '12':
            customer_id = int(input("Enter customer ID to remove: "))
            Customer.remove_customer(customer_id)
        
        elif choice == '0':
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == '__main__':
    main()
