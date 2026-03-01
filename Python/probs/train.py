class Train:
    def __init__(self,name,fare,seats):
        self.name=name
        self.fare=fare
        self.seats=seats
    def get_status(self):
        print(f"------Train Status:{self.name}----")
        print(f"Available seats:{self.seats}")
        print("-------------------------")
    def get_fare_info(self):
        print(f"The fare for {self.name} is :{self.fare}")
    def book_tickets(self):
        if self.seats>0:
            print(f"Sucess! your ticket has been booked in {self.name}")
            print(f"Your Seat number is {self.seats}")
            self.seats=self.seats-1
        else:
            print("This train is full ,Try tatkal or another train.")

rajadhani=Train("Rajadhani Express",2500,2)

rajadhani.get_status()
rajadhani.get_fare_info()
rajadhani.book_tickets()
rajadhani.book_tickets()
rajadhani.book_tickets()
rajadhani.get_status()
