# Write a program to create a class that can calculate the surface area and volume of a solid. The class should also have a provision to accept the data relevant to the solid
class Solid:
    def __init__(self):
        self.length = 0
        self.breadth = 0
        self.height = 0
    def accept_data(self):
        self.length = int(input("Enter the length of the solid: "))
        self.breadth = int(input("Enter the breadth of the solid: "))
        self.height = int(input("Enter the height of the solid: "))
    def surface_area(self):
        return 2 * (self.length * self.breadth + self.breadth * self.height + self.height * self.length)
    def volume(self):
        return self.length * self.breadth * self.height
    
solid = Solid()
solid.accept_data()
print("Surface Area of the solid is: ", solid.surface_area())
print("Volume of the solid is: ", solid.volume())