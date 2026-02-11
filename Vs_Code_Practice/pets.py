class Employee:
    salary=50000
    increment=10

    @property
    def salaryAfterIncrement(self):
        return self.salary+(self.salary*self.increment/100)
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self,newval):
        self.increment=((newval-self.salary)/self.salary)*100

e=Employee()
print(f"Current Salary with {e.increment}%increment:{e.salaryAfterIncrement}")
e.salaryAfterIncrement=60000
print(f"To get 60000, the new increment percentage is :{e.increment}")