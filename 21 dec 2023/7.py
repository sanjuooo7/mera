import math

#common
class Shape:
    def calculate_area(self):
        pass
        
    def calculate_perimeter(self):
        pass

        #circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
            
    def calculate_area(self):
        return math.pi * self.radius**2

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius

    #square
class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length
        
    def calculate_area(self):
        return self.side_length**2
    
    def calculate_perimeter(self):
        return 4 * self.side_length

    #triangle
class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        
    def calculate_area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))
    
    def calculate_perimeter(self):
        return self.side1 + self.side2 + self.side3


# Instantiate objects and compute area/perimeter
circle = Circle(5)
square = Square(4)
triangle = Triangle(3, 4, 5)
# Print results
print(f"Circle - Area: {circle.calculate_area()}, Perimeter: {circle.calculate_perimeter()}")
print(f"Square - Area: {square.calculate_area()}, Perimeter: {square.calculate_perimeter()}")
print(f"Triangle - Area: {triangle.calculate_area()}, Perimeter: {triangle.calculate_perimeter()}")
