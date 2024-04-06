from errors import TooManyStudentsError

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