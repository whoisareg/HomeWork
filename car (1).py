
class Car:
    def __init__(self,
                name: str,
                year: int,
                sign: str,
                speed: float,
                consumption: float,
                tank_size: float
                ) -> None:

        self.name = name
        self.year = year
        self.speed = speed
        self.consumption = consumption
        self.tank_size = tank_size
        self.__fuel__ = 0
        self.__sign__ = sign

    def calculate_time(self, distance: float) -> float:
        return distance / self.speed

    def register(self, new_sign_number: str) -> bool:
      
        if self.__sign__:
            return False

        if len(new_sign_number) == 7 and new_sign_number[:2].isdigit() and \
           new_sign_number[2:4].isupper() and new_sign_number[4:].isdigit():
            self.__sign__ = new_sign_number
            return True

        return False

    def fill(self, fuel_amount: float) -> None:

        self.__fuel__ = min(self.__fuel__ + fuel_amount, self.tank_size)

    def go(self, distance: float) -> bool:

        needed_fuel = (distance / 100) * self.consumption
        if self.__fuel__ >= needed_fuel:
            self.__fuel__ -= needed_fuel
            return True
        return False


    def get_sign(self) -> str:
        return self.__sign__

    def get_fuel(self) -> float:
        return self.__fuel__

    def max_distance_can_travel(self) -> float:
        return (self.__fuel__ / self.consumption) * 100


car = Car(name="Ford Fusion", year=2017, sign="", speed=100, consumption=12, tank_size=63)
print(f"Car name: {car.name}")
print(f"Car year: {car.year}")
print(f"Car average speed: {car.speed} km/h")
print(f"Car consumption: {car.consumption} L/100km")
print(f"Car tank size: {car.tank_size} L")
print(f"Car initial fuel: {car.get_fuel()} L")
print(f"Car sign: {car.get_sign()}")

if car.register("35AQ035"):
    print(f"Car registered with sign: {car.get_sign()}")
else:
    print("Registration failed.")

car.fill(60)
print(f"Fuel after filling: {car.get_fuel()} L")

time_needed = car.calculate_time(164)
print(f"Time needed to travel 164 km: {time_needed} hours")

if car.go(164):
    print(f"Traveled 164 km, fuel left: {car.get_fuel()} L")
else:
    print("Not enough fuel to travel 164 km")

max_distance = car.max_distance_can_travel()
print(f"Max distance can travel with current fuel: {max_distance} km")
