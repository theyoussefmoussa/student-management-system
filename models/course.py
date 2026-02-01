from utils.validators import get_valid_course_name, get_valid_credit


class Course : 
   def __init__(self):
    self.name = get_valid_course_name()
    self.credits = get_valid_credit()
    self.enrolled_students = []

   def __str__(self):
      student_count = len(self.enrolled_students)
      return f"Course: {self.name}, Credits: {self.credits}, Students: {student_count}"
   
   def add_student(self,student) : 
      self.enrolled_students.append(student)
   
   def remove_student(self,student) : 
      if student in self.enrolled_students : 
         self.enrolled_students.remove(student)
      else : 
         print(f"Student {student.name} is NOT Found In This Course")
   def get_students(self):
      """Return List of enrolled students"""
      return self.enrolled_students

   def get_students_count(self) : 
      return len(self.enrolled_students)

