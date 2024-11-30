class Library:
    def __init__(self, city, street, zip_code, open_hours, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f'Library in {self.city}, {self.street}, {self.zip_code}. Open: {self.open_hours}. Phone: {self.phone}'


class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return f'Employee: {self.first_name} {self.last_name}, Hire date: {self.hire_date}, Birth date: {self.birth_date}, Address: {self.street}, {self.city}, {self.zip_code}, Phone: {self.phone}'


class Book:
    def __init__(self, library, publication_date, author_name, author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f'Book by {self.author_name} {self.author_surname}, Published: {self.publication_date}, Pages: {self.number_of_pages}, Available at: {self.library}'


class Order:
    def __init__(self, employee, books, order_date):
        self.employee = employee
        self.books = books
        self.order_date = order_date

    def __str__(self):
        books_str = ', '.join([str(book) for book in self.books])
        return f'Order processed by: {self.employee}, Date: {self.order_date}, Books: {books_str}'


library1 = Library("Katowice", "Main St 1", "40-000", "9:00-18:00", "123-456-789")
library2 = Library("Warszawa", "Second St 5", "00-001", "10:00-19:00", "987-654-321")

book1 = Book(library1, "2020-01-01", "John", "Doe", 250)
book2 = Book(library1, "2019-05-12", "Jane", "Smith", 300)
book3 = Book(library2, "2018-07-23", "Emily", "Jones", 150)
book4 = Book(library2, "2021-11-15", "Michael", "Brown", 400)
book5 = Book(library1, "2022-02-28", "Linda", "White", 200)

employee1 = Employee("Anna", "Nowak", "2015-08-01", "1990-04-12", "Katowice", "Main St 2", "40-000", "111-222-333")
employee2 = Employee("Piotr", "Kowalski", "2017-06-15", "1985-03-23", "Warszawa", "Second St 6", "00-001", "444-555-666")
employee3 = Employee("Maria", "Lewandowska", "2019-10-30", "1992-12-05", "Katowice", "Main St 3", "40-000", "777-888-999")

order1 = Order(employee1, [book1, book2], "2024-10-28")
order2 = Order(employee2, [book3, book4, book5], "2024-10-29")

print(order1)
print(order2)
