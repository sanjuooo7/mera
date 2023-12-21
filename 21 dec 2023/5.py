class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def calculate_area(self):
        return self.length * self.width
    def calculate_perimeter(self):
        return 2 * (self.length + self.width)
    
# Instantiate objects and compute area/perimeter
rectangle1 = Rectangle(5, 10)
area1 = rectangle1.calculate_area()
perimeter1 = rectangle1.calculate_perimeter()

rectangle2 = Rectangle(8, 6)
area2 = rectangle2.calculate_area()
perimeter2 = rectangle2.calculate_perimeter()

# Print results
print(f"Rectangle 1 - Area: {area1}, Perimeter: {perimeter1}")
print(f"Rectangle 2 - Area: {area2}, Perimeter: {perimeter2}")
