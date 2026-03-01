import math


class calculator:
    def __init__(self,number):
        self.number=number
    def squrae(self):
        print(f"The square of {self.number} is {self.number**2}")
    def cube(self):
        print(f"The cube of {self.number} is {self.number**3}")
    def squrare_root(self):
        result=math.sqrt(self.number)
        print(f"The squrae root of {self.number} is {result:.2f}")
    
num=int(input("Enter a number:"))
my_calc=calculator(num)

my_calc.squrae()
my_calc.cube()
my_calc.squrare_root()