# You need to left a few blank lines at the very top of the file

class Car:
    def __init__(self, model, age, tank_size, consuption):
        self.model = model
        self.age = age
        self.tank_size = tank_size
        self.petrol_amount = 0
        self.consuption = consuption

    def fill(self):
        print('qani litr benzin a harkavor?')       # Use english, pls
        amount = float(input())         # amount must be function argument, not be inputed manualy
        if amount <= 0:
            print("hamakargi sxal, krkin pordzeq")      # If any mistake in user provided data, you need to tell user about it
                                                        # Maybe, it will be better to use       raise ValueError
        elif self.petrol_amount + amount > self.tank_size:
            amount = self.tank_size     # This line would not save given amount to the self.petrol_amount
            print(f"duq lcrel eq {amount} litr benzin")     # Using same line twice. You may place it after your if-else block
        else:
            self.petrol_amount += amount
            print(f"duq lcrel eq {amount} litr benzin")

    def go(self):
        print('vorqan chanaparh eq uzum ancnel km-ov?')
        distance = float(input())           # distance must be function argument, not be inputed manualy
        needed_petrol = distance * self.consuption
        if needed_petrol <= self.petrol_amount:
            self.petrol_amount -= needed_petrol
            print(f"qshvel a {distance} km, exac benziny {self.petrol_amount} litr a.")
        else:
            print("dzer unecac benziny dzez tex chi hascni")


a1 = Car("Ford Fusion", 7, 63, 0.3)         # Variable name 'a1' is a very bad practice
a1.fill()
a1.go()
