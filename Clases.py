# In Python, classes are a fundamental part of Object-Oriented Programming (OOP).
# A class is a blueprint for creating objects.
# Objects are instances of a class that contain attributes (variables) and methods (functions).

class Shape:
    # constructer to initialize shape name and size
    def __init__(self, name, sides):
        self.name = name
        self.sides = sides

    # method of shape class
    def shape_info(self):
        print(f'This is {self.name} shape it has {self.sides} sides ')


# frst object created
shape1 = Shape('Square', 4)
shape1.shape_info()

# second object created
shape2 = Shape('Triangle', 3)
shape2.shape_info()

# Another example of Class topic...........................................................
class Car:
    def __init__(self, brand, model):
        self.brand = brand  # Attribute
        self.model = model  # Attribute

    def display_info(self):  # Method
        print(f"Car: {self.brand} {self.model}")

# Creating an object (instance) of the class
my_car = Car("Toyota", "Corolla")

# Accessing attributes and methods
print(my_car.brand)  # Output: Toyota
my_car.display_info()  # Output: Car: Toyota Corolla


# Another example in which we write destructor ....................
class Test:
    def __init__(self, name):
        self.name = name
        print(f"{self.name} object created")

    def __del__(self):
        print(f"{self.name} object deleted")

t1 = Test("Object1")
del t1  # Manually deleting the object
