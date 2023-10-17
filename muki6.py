def sort_students(student_list):
  sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
  return sorted_students
class Student:
  def __init__(self, name, roll_number, cgpa):
      self.name = name
      self.roll_number = roll_number
      self.cgpa = cgpa

# Create a list of student objects
students = [
  Student("Alice", "101", 3.8),
  Student("Bob", "102", 3.6),
  Student("Charlie", "103", 3.9),
  Student("David", "104", 3.7)
]

# Sort the students by CGPA in descending order
sorted_students = sort_students(students)

# Print the sorted list of students
for student in sorted_students:
  print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")