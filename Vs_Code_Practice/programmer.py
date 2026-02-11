class programmer:
    company="Microsoft"
    def __init__(self,name,salary,role):
        self.name=name
        self.salary=salary
        self.role=role
    def get_info(self):
        print(f"---{self.company} Employee profile")
        print(f"Name:{self.name}")
        print(f"Role:{self.role}")
        print(f"Salary:${self.salary}")
        print("--------------------------------------------")

p1=programmer("Soham",120000,"Software Engineer")
p2=programmer("Sachin",150000,"Data Scientist")

p1.get_info()
p2.get_info()