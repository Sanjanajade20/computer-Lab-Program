# Write a program to create a class that can calculate the perimeter/circumference and area of a regular shape. The class should also have a provision to accept the data relevant to the shape.

import math

class RegularShape:
    def __init__(self, shape_type):
        self.shape_type = shape_type.lower()
        self.parameters = {}

    def accept_data(self):
        if self.shape_type == "circle":
            self.parameters['radius'] = float(input("Enter the radius of the circle: "))
        elif self.shape_type == "polygon":
            self.parameters['sides'] = int(input("Enter the number of sides: "))
            self.parameters['length'] = float(input("Enter the length of each side: "))
        else:
            print("Unsupported shape.")

    def calculate_perimeter(self):
        if self.shape_type == "circle":
            return 2 * math.pi * self.parameters['radius']
        elif self.shape_type == "polygon":
            return self.parameters['sides'] * self.parameters['length']
        else:
            return None

    def calculate_area(self):
        if self.shape_type == "circle":
            return math.pi * self.parameters['radius'] ** 2
        elif self.shape_type == "polygon":
            n = self.parameters['sides']
            s = self.parameters['length']
            return (n * s ** 2) / (4 * math.tan(math.pi / n))
        else:
            return None

# Example usage
shape_type = input("Enter the shape (circle or polygon): ")
shape = RegularShape(shape_type)
shape.accept_data()

perimeter = shape.calculate_perimeter()
area = shape.calculate_area()

if perimeter is not None and area is not None:
    print(f"Perimeter: {perimeter:.2f}")
    print(f"Area: {area:.2f}")
else:
    print("Invalid shape entered.")
