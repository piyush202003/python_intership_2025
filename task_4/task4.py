print("1. Create a class 'Student' with attributes name, roll_no, marks.")
class Students:
    def __init__(self):
        self.__name = 'Rajesh'
        self.__rollNo = 59
        self.__marks = 74
    def student(self):
        print(self.__name, self.__rollNo, self.__marks)

obj = Students()
obj.student()

print("2. Implement encapsulation using private variables.")
class Subject:
    def __init__(self):
        self.__math = 42
        self.__english = 56
        self.__marathi = 67
        self.__science = 54
        self.__history = 53
    
    def markSheet(self):
        print("Students Mark Sheet=")
        print('Math = ', self.__math)
        print('Marathi = ', self.__marathi)
        print("English = ", self.__english)
        print('Science = ', self.__science)
        print('History = ', self.__history)

marks = Subject()
marks.markSheet()

print("3. Create inheritance using a class 'GraduateStudent'.")
class StudentList():
    def __init__(self, *args, **kwargs):
        self.graduationStatus = {'Rajesh':False, 'Ramesh': True, 'Seeta':False, 'Rani':False, 'Nandini':True, 'Pranav':True, 'Abhay':True}

class GraduateStudent(StudentList):
    def graduated(self):
        print('List of Graduated students = ',end='')
        for i in self.graduationStatus:
            print(i,end='->')
obj = GraduateStudent()
obj.graduated()

print("4. Write a decorator to measure execution time of a function.")
def measure_time(func):
    def wrapper(*args, **kwargs):
        print("Function started")
        result = func(*args, **kwargs)
        print("Function ended")
        return result
    return wrapper

@measure_time
def greet(name):
    print("Hello", name)

greet("Piyush")

print("5. Create a generator that generates even numbers up to 50.")
def even_numbers():
    for num in range(2, 51, 2):
        yield num
for num in even_numbers():
    print(num,end=' ')

print("6. Use lambda function to sort a list of tuples based on second value.")
data = [
    ('Ahay',23),
    ('Pranav',45),
    ('Pramod',32),
    ('Amit',54),
    ('Sharma',25)
]
data = sorted(data, key=lambda x : x[1])
print(data)
