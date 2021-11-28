class Library:

    def __init__(self, city: str, street: str, zip_code: str, open_hours: str, phone: str):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f"library, which located in {self.city} (zip code - {self.zip_code}), at {self.street}. " \
               f"Library is open {self.open_hours}, and the contact number is {self.phone}"


class Employee:

    def __init__(
            self, first_name: str,
            last_name: str,
            hire_date: str,
            birth_date: str,
            city: str,
            street: str,
            zip_code: str,
            phone: str
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return f"{self.first_name} {self.last_name}, from {self.city} ({self.zip_code}), {self.street} and born on " \
               f"{self.birth_date}. Hired on {self.hire_date}. Phone num is {self.phone}"


class Book:

    def __init__(
            self,
            library: Library,
            publication_date: str,
            author_name: str,
            author_surname: str,
            number_of_pages: int
    ):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f"{self.author_name} {self.author_surname} book from {self.publication_date} and with " \
               f"{self.number_of_pages} pages. It's in {self.library}"


class Order:

    def __init__(
            self,
            employee: Employee,
            student: str,
            books: Book,
            order_date: str
    ):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        return f'This is {self.student}s order from {self.order_date}. He/she order {self.books}. ' \
               f'Order will be handled by {self.employee}'


if __name__ == "__main__":
    lib1 = Library('Atlanta', "6th Ave 43/4", "52-213", "9 AM to 5 PM", "234 233 43")
    lib2 = Library('Atlanta', "9th Street 3/4", "52-253", "9 AM to 5 PM", "123 535 03")

    book1 = Book(lib1, "12-11-1245", "Dan", "Dan", 122)
    book2 = Book(lib1, "12-11-1245", "Ban", "Ban", 133)
    book3 = Book(lib1, "12-11-1245", "Ran", "Ran", 144)
    book4 = Book(lib2, "12-11-1245", "Wan", "Wan", 155)
    book5 = Book(lib2, "12-11-1245", "San", "San", 166)

    employee1 = Employee(
        'bob',
        'ross',
        '10-10-2021',
        '10-10-2020',
        'NY',
        'long street',
        '43-425',
        '324-324-55'
    )

    employee2 = Employee(
        'Roob',
        'BOss',
        '10-10-2021',
        '10-10-2020',
        'NY',
        'mid street',
        '41-425',
        '324-324-55'
    )

    employee3 = Employee(
        'SOB',
        'Soss',
        '10-10-2021',
        '10-10-2020',
        'NY',
        'short street',
        '42-425',
        '421-324-55'
    )

    order1 = Order(employee1, "studen1", book1, "13-11-2014")
    order2 = Order(employee2, "studen2", book5, "13-11-2014")

    print(order1)
    print(order2)
