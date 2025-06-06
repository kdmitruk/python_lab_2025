class Student:
    def __init__(self, name):
        self.name = name

    def set_grades(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, 'grade_' + key, value)

    def avg(self):
        prz = 0
        suma = 0
        for key, value in self.__dict__.items():
            if key.startswith('grade_'):
                suma += value
                prz += 1
        return suma / prz

def main():
    student = Student('Jan Kowalski')
    student.set_grades(matematyka = 5, informatyka = 4)
    student.set_grades(angielski = 5)
    print(student.avg())

if __name__ == '__main__':
    main()