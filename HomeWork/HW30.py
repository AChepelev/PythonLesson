class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.age = age
        self.gender = gender
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"Human: {self.gender}, Age: {self.age}, Firstname: {self.first_name}, Lastname: {self.last_name}"


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        self.age = age
        self.gender = gender
        self.first_name = first_name
        self.last_name = last_name
        self.record_book = record_book

    def __str__(self):
        return f"Student: {self.gender}, Age: {self.age}, Firstname: {self.first_name}, Lastname: {self.last_name}, Recordbook: {self.record_book}"

class TooManyStudentsError(Exception):
    pass

class Group:
    def __init__(self, number):
        self.number = number
        self.students = {}

    def add_student(self, student):
        if len(self.students) >= 10:
            raise TooManyStudentsError("До групи можна додати не більше 10 студентів.")
        else:
            self.students[student.last_name] = student

    def delete_student(self, last_name):
        if last_name in self.students:
            del self.students[last_name]
            return True
        else:
            return False

    def find_student(self, last_name):
        return self.students.get(last_name, None)

    def __str__(self):
        all_students = '\n'.join(str(student) for student in self.students.values())
        return f'Number: {self.number}\n{all_students}'


# Приклад використання:
group = Group('PD1')

try:
    for i in range(11):
        student = Student('Male', 20, f'Ім\'я {i}', f'Прізвище {i}', f'RB{i}')
        group.add_student(student)
except TooManyStudentsError as e:
    print(f"Помилка: {e}")

print(group)