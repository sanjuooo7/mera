class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        
    def update_grade(self, new_grade):
        self.grade = new_grade
        return f"{self.name}'s grade updated to {new_grade}"
        
    def display_student_info(self):
        return f"Name: {self.name}\nAge: {self.age}\nGrade: {self.grade}"
# Create instances and showcase functionality
student1 = Student("Alice", 18, "A")
print(student1.display_student_info())
print(student1.update_grade("B"))
print(student1.display_student_info())
# Create another instance
student2 = Student("Bob", 17, "C")
print(student2.display_student_info())
print(student2.update_grade("A"))
print(student2.display_student_info())
