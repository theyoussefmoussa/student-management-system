from models.person import Person
from utils.validators import get_valid_course_name, get_valid_unique_id


class Student(Person):
    def __init__(self):
        super().__init__()
        self.student_id = get_valid_unique_id()
        self.courses = {}  # course_name -> grade

    
    def __str__(self):
        person_str = super().__str__()
        course_count = len(self.courses)
        grade_count = sum(1 for grade in self.courses.values() if grade is not None)
        return f" ID: {self.student_id}, {person_str}, Courses: {course_count}, Grades: {grade_count}"

    def add_course(self, course_name = None):
        # checks if course name isn't passed as parameter then take it from user
        course = course_name if course_name else get_valid_course_name()
        # checks if course exists
        if course in self.courses: 
            print("Course Is Already Exists")
            return 
        self.courses[course] = None
        print(f"Course '{course}' Added Successfully")

    def add_grade(self, grade):
        # checks if student enrolled in course or not
        if grade.course_name not in self.courses:
            print(f"You haven't enrolled in {grade.course_name}")
            return
        # checks if grade already exists
        if self.courses[grade.course_name] is not None:
            print(f"Grade for {grade.course_name} already exists")
            return
        # match grade with course name
        self.courses[grade.course_name] = grade
        print(f"Grade for {grade.course_name} added successfully")

    
    def remove_course(self, course):
        print("To Remove A Course") 
        if course in self.courses: 
            print(f"{course} Has Been Deleted Successfully")
            del self.courses[course]
        else: 
            print(f"Course {course} Is Not Found")


    def get_grades(self): 
        """Returns list of grades values"""
        return [grade for grade in self.courses.values() if grade is not None]
    
    def get_courses(self): 
        return self.courses.keys()       

