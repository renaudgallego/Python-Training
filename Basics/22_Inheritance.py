class ParentClass:
    # attributes / methods
    pass


class ChildClass:
    # attributes / merthods
    pass


class Vehicule:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def display_vehicule_info(self):
        print(f"brand : {self.brand}")
        print(f"speed : {self.speed}")


class Car(Vehicule):  # <- 'Vehicule' is the parent class of 'Car'
    def __init__(self, brand, speed, fuel):
        # since 'Vehicule' is parent class, this line call the constructor of the parent class = super()
        super().__init__(brand, speed)
        self.fuel = fuel

    def display_car_info(self):
        self.display_vehicule_info()  # call the method of the parent class
        print(f"fuel  : {self.fuel}")


class main:
    my_bicycle = Vehicule(brand="Decathlon", speed=60)
    my_bicycle.display_vehicule_info()
    print("------------------------------")

    car1 = Car(brand="renault", speed=150, fuel="benzine")
    car1.display_car_info()
    print("------------------------------")

    car2 = Car(brand="peugeot", speed=145, fuel="diesel")
    car2.display_car_info()
