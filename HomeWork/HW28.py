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

class Group:

    def __init__(self, number):
        self.number = number
        self.group = {}

    def add_student(self, student):
        self.group[student.last_name] = student

    def delete_student(self, last_name):
        if last_name in self.group:
            del self.group[last_name]
            return True
        else:
            return False

    def find_student(self, last_name):
        return self.group.get(last_name, None)

    def __str__(self):
        all_students = '\n'.join(str(student) for student in self.group.values())
        return f'Number:{self.number}\n{all_students}'


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr)
assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'

gr.delete_student('Taylor')
print(gr)  # Only one student

gr.delete_student('Taylor')  # No error!