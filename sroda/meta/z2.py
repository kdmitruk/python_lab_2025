class Student:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, f"grade_{key}", value)

    def __str__(self):
        return str(self.__dict__)

    def avg(self) -> float:
        sum = 0
        n = 0
        for key, value in self.__dict__.items():
            if key.startswith("grade_"):
                sum += float(value)
                n += 1
        return sum/n

if __name__ == "__main__":
    s1 = Student(matma=4, fizyka=5, polski=1)
    print(s1.grade_matma, s1.avg())