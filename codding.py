class Car:
    def __init__(self, model, age, tank_size, consuption):
        self.model = model
        self.age = age
        self.tank_size = tank_size
        self.petrol_amount = 0
        self.consuption = consuption
        
    def fill(self):
        print('qani litr benzin a harkavor?')
        amount = float(input())
        if amount <= 0:
            print("hamakargi sxal, krkin pordzeq")
        elif self.petrol_amount + amount > self.tank_size:
            amount = self.tank_size
            print(f"duq lcrel eq {amount} litr benzin")
        else:
            self.petrol_amount += amount
            print(f"duq lcrel eq {amount} litr benzin")
            
    def go(self):
        print('vorqan chanaparh eq uzum ancnel km-ov?')
        distance = float(input())
        needed_petrol = distance * self.consuption
        if needed_petrol <= self.petrol_amount:
            self.petrol_amount -= needed_petrol
            print(f"qshvel a {distance} km, exac benziny {self.petrol_amount} litr a.")
        else:
            print("dzer unecac benziny dzez tex chi hascni")

                
a1 = Car("Ford Fusion", 7, 63, 0.3)
a1.fill()
a1.go()


                
                
                            
        
    