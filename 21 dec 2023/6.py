class Employee:
    def __init__(self, name, employee_id, basic_pay, hra_percentage, da_percentage):
        self.name = name
        self.employee_id = employee_id
        self.basic_pay = basic_pay
        self.hra_percentage = hra_percentage
        self.da_percentage = da_percentage
    def calculate_salary(self):
        hra = (self.hra_percentage / 100) * self.basic_pay
        da = (self.da_percentage / 100) * self.basic_pay
        salary = self.basic_pay + hra + da
        return salary
    def display_employee_info(self):
        return f"Name: {self.name}\nEmployee ID: {self.employee_id}\nBasic Pay: ${self.basic_pay}\nSalary: ${self.calculate_salary()}"

# Instantiate objects and display employee information
employee1 = Employee("John Doe", "E123", 50000, 20, 15)
print(employee1.display_employee_info())
employee2 = Employee("Jane Smith", "E456", 60000, 18, 12)
print(employee2.display_employee_info())
