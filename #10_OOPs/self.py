class Employee:
    language = "Python"
    salary = 1200000

    def getInfo(self):
        print(f"the language is {self.language}. the salary is {self.salary}")

harry = Employee()
harry.language = "javaScript"  #this is intance attribute
print(harry.language, harry.salary)

# Employee.getInfo(harry)
harry.getInfo()