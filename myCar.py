

class Car:
    def __init__(self, model, year, tank_size, consumption):
        self.model = model
        self.year = year
        self.tank_size = tank_size
        self.petrol_amount = 0
        self.consumption = consumption
        
    
    def fill(self, amount):
        if amount <= 0:
            raise ValueError("Invalid amount.")
        elif self.petrol_amount + amount > self.tank_size:
            amount = self.tank_size - self.petrol_amount
        self.petrol_amount += amount
        print(f"{amount} liters of petrol added.")
            
    
    def go(self, distance):
        needed_petrol = distance * self.consumption
        if needed_petrol <= self.petrol_amount:
            self.petrol_amount -= needed_petrol
            print(f"Distance traveled: {distance} km. The capacity of the tank is {self.petrol_amount} liters.")
        else:
            print("Not enough petrol to cover the distance. Please fill up.")
            print(f"Current petrol amount: {self.petrol_amount} liters.")


myCar = Car("Ford Fusion", 2017, 63, 0.3)
myCar.fill(40)
myCar.go(120)