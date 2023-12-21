class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        
    def update_year(self, new_year):
        self.year = new_year
        return f"Year updated to {new_year}"
    
    def display_car_details(self):
        return f"Make: {self.make}\nModel: {self.model}\nYear: {self.year}"


# Create instances and showcase functionality
car1 = Car("Toyota", "Camry", 2020)
print(car1.display_car_details())
print(car1.update_year(2022))
print(car1.display_car_details())
# Create another instance
car2 = Car("Honda", "Civic", 2018)
print(car2.display_car_details())
print(car2.update_year(2021))
print(car2.display_car_details())
