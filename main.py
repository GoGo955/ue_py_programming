from classes.Book import Book
import classes.Library
from classes.Employee import Employee
from classes.Order import Order


if __name__ == "__main__":
    lib1 = Library.Library("Atlanta", "6th Ave 43/4", "52-213", "9 AM to 5 PM", "234 233 43")
    lib2 = Library.Library("Atlanta", "9th Street 3/4", "52-253", "9 AM to 5 PM", "123 535 03")

    book1 = Book(lib1, "12-11-1245", "Dan", "Dan", 122)
    book2 = Book(lib1, "12-11-1245", "Ban", "Ban", 133)
    book3 = Book(lib1, "12-11-1245", "Ran", "Ran", 144)
    book4 = Book(lib2, "12-11-1245", "Wan", "Wan", 155)
    book5 = Book(lib2, "12-11-1245", "San", "San", 166)

    employee1 = Employee(
        "bob",
        "ross",
        "10-10-2021",
        "10-10-2020",
        "NY",
        "long street",
        "43-425",
        "324-324-55",
    )

    employee2 = Employee(
        "Roob",
        "BOss",
        "10-10-2021",
        "10-10-2020",
        "NY",
        "mid street",
        "41-425",
        "324-324-55",
    )

    employee3 = Employee(
        "SOB",
        "Soss",
        "10-10-2021",
        "10-10-2020",
        "NY",
        "short street",
        "42-425",
        "421-324-55",
    )

    order1 = Order(employee1, "studen1", book1, "13-11-2014")
    order2 = Order(employee2, "studen2", book5, "13-11-2014")

    print(order1)
    print(order2)
