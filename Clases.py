# # In Python, classes are a fundamental part of Object-Oriented Programming (OOP).
# # A class is a blueprint for creating objects.
# # Objects are instances of a class that contain attributes (variables) and methods (functions).
#
# class Shape:
#     # constructer to initialize shape name and size
#     def __init__(self, name, sides):
#         self.name = name
#         self.sides = sides
#
#     # method of shape class
#     def shape_info(self):
#         print(f'This is {self.name} shape it has {self.sides} sides ')
#
#
# # frst object created
# shape1 = Shape('Square', 4)
# shape1.shape_info()
#
# # second object created
# shape2 = Shape('Triangle', 3)
# shape2.shape_info()
#
# # Another example of Class topic...........................................................
# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand  # Attribute
#         self.model = model  # Attribute
#
#     def display_info(self):  # Method
#         print(f"Car: {self.brand} {self.model}")
#
# # Creating an object (instance) of the class
# my_car = Car("Toyota", "Corolla")
#
# # Accessing attributes and methods
# print(my_car.brand)  # Output: Toyota
# my_car.display_info()  # Output: Car: Toyota Corolla
#
#
# # Another example in which we write destructor ....................
# class Test:
#     def __init__(self, name):
#         self.name = name
#         print(f"{self.name} object created")
#
#     def __del__(self):
#         print(f"{self.name} object deleted")
#
# t1 = Test("Object1")
# del t1  # Manually deleting the object

# -------------------------create class circle also draw circle
# Import the library

import matplotlib.pyplot as plt
# %matplotlib inline


# Create a class Circle

class Circle(object):

    # Constructor
    def __init__(self, radius=3, color='blue'):
        self.radius = radius
        self.color = color

        # Method

    def add_radius(self, r):
        self.radius = self.radius + r
        return (self.radius)

    # Method
    def drawCircle(self):
        """
        plt.Circle((0, 0), radius=self.radius, fc=self.color)
        → Circle draw karta hai center (0, 0) pe, with given radius and color (fc means face color).
        plt.gca()
        → "Get Current Axes" — jahan shape draw hogi.

        add_patch()
        → Circle ko canvas pe add karta hai.

        plt.axis('scaled')
        → Axes ko scale karta hai taake circle proper shape mein dikhe (warna oval ban sakta hai).

        plt.show()
        → Final drawing screen pe show karta hai.
        :return:
        """
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.show()


# Create an object RedCircle

RedCircle = Circle(10, 'red')
RedCircle.drawCircle()
# dir(RedCircle)

# GreenCircle = Circle(5, 'green')
# GreenCircle.drawCircle()
# ------------------------------------------------


# Create a new Rectangle class for creating a rectangle object

class Rectangle(object):

    # Constructor
    def __init__(self, width=2, height=3, color='r'):
        self.height = height
        self.width = width
        self.color = color

    # Method
    def drawRectangle(self):
        plt.gca().add_patch(plt.Rectangle((0, 0), self.width, self.height, fc=self.color))
        plt.axis('scaled')
        plt.show()

# Create a new object rectangle

SkinnyBlueRectangle = Rectangle(2, 3, 'blue')
SkinnyBlueRectangle.drawRectangle()
