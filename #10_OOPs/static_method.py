class Employee:
    language = "Python"
    salary = 1200000

    def greet(self):
        print(f"the language is {self.language}. the salary is {self.salary}")

    @staticmethod
    def greed():
        print("good morning")    

harry = Employee()
harry.language = "javaScript"  #this is intance attribute
print(harry.language, harry.salary)

harry.greet()
