class Car:

    # class attribute
    location = "Europe"

    # dunder init = constructor / called at the creation of instance
    def __init__(self, wheels, engine, color):
        self.wheels = wheels
        self.engine = engine
        self.color = color

    # method
    def display_info(self):
        print(f"nb wheels    : {self.wheels}")
        print(f"engine type : {self.engine}")
        print(f"color        : {self.color}")


class main:

    # instance attributes -> need to be initialized at creation of instance through dunder __init__ / constructor
    BMW = Car(4, "diesel", "Black")
    Ferrari = Car(4, "hybrid", "red")

    print("-------------------")
    BMW.display_info()
    print("-------------------")
    Ferrari.display_info()
    print("-------------------")

    # additional instance attributes -> need to be initialized after declaration
    BMW.gears = 6
    Ferrari.speed = 350
    Ferrari.seats = 2
    print(f"Bmw - gears : {BMW.gears}")
    print(f"Ferrari - speed : {Ferrari.speed}")
    print(f"Ferrari - seats : {Ferrari.seats}")
    print("-------------------")

    # class attribute -> no need to initialize class attributes since they are initialized at the creation of the instance
    print(f"bmw - location : {BMW.location}")
    print(f"ferrari - location : {Ferrari.location}")
    print("-------------------")

    # modify class attribute
    BMW.location = "Germany"
    print(f"bmw - location : {BMW.location}")
    print(f"ferrari - location : {Ferrari.location}")
    print("-------------------")
