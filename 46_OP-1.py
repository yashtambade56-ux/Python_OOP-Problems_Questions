# Create a Student class with name, roll, and marks; add method to compute average.

class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def average_marks(self):
        if not self.marks:
            return 0
        return sum(self.marks) / len(self.marks)
    
# Example usage
student1 = Student("ram", 1, [85, 90, 78])
print(f"Student Name: {student1.name}")
print(f"Roll Number: {student1.roll}")
print(f"Average Marks: {student1.average_marks()}")
student2 = Student("rahul", 2, [88, 76, 92, 85])
print(f"Student Name: {student2.name}")
print(f"Roll Number: {student2.roll}")
print(f"Average Marks: {student2.average_marks()}")