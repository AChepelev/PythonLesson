class Student:
    def __init__(self, gender, age, first_name, last_name, record_book):
        self.age = age
        self.gender = gender
        self.first_name = first_name
        self.last_name = last_name
        self.record_book = record_book

    def __str__(self):
        return f"Student: {self.gender}, Age: {self.age}, Firstname: {self.first_name}, Lastname: {self.last_name}, Recordbook: {self.record_book}"

    def __hash__(self):
        return hash(str(self))