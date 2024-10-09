class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(self.fname, self.lname)


class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.year = year

student1 = Student("Jimmy", "Riley", 2024)
student1.printname()
print("Graduation Year", student1.year)
