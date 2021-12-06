from classes.Employee import Employee
from classes.Book import Book

class Order:
    def __init__(self, employee: Employee, student: str, books: Book, order_date: str):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        return (
            f"This is {self.student}s order from {self.order_date}. He/she order {self.books}. "
            f"Order will be handled by {self.employee}"
        )
