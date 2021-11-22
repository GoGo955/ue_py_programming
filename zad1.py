class Student:

    def __init__(self, name: str, marks: int):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f'Student {self.name} with mark {self.marks}'

    def is_passed(self):
        return self.marks > 50

if __name__ == "__main__":
    stud1 = Student("Bob Ross", 74)
    stud2 = Student("Rob Boss", 35)

    print(f'{stud1}. Did he pass? -> {stud1.is_passed()}')
    print(f'{stud2}. Did he pass? -> {stud2.is_passed()}')
