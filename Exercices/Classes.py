class Car:

    def __init__(self, wheels, engine, color):
        self.wheels = wheels
        self.engine = engine
        self.color = color

    def display_info(self):
        print(f"nb wheels    : {self.wheels}")
        print(f"engine brand : {self.engine}")
        print(f"color        : {self.color}")


class main:
    BMW = Car(4, "BMW", "Black")
    Ferrari = Car(4, "Ferrari", "red")

    print("-------------------")
    BMW.display_info()
    print("-------------------")
    Ferrari.display_info()
    print("-------------------")
