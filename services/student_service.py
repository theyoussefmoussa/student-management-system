"""
StudentService: Handles student-related business logic
"""

from models.grade import Grade
from utils.constants import MAX_GRADE, MIN_GRADE


class StudentService: 

    @staticmethod
    def get_grade_for_course(student, course_name):
        """Get student's grade for a specific course"""
        # Get all grades
        grades = student.get_grades()
        
        # Search for the grade with matching course name
        for grade in grades:
            if grade.course_name == course_name:
                return grade.grade
        
        # If not found
        print(f"No grade found for {course_name}")
        return None

    
    @staticmethod
    def enrol_in_course(student, course):
        """Enroll student in a course"""
        # Check if already enrolled
        enrolled_courses = student.get_courses()
        if course.name in enrolled_courses:
            print(f"Already enrolled in {course.name}")
            return
        
        # Add course to student
        student.add_course(course.name)
        
        # Add student to course
        course.add_student(student)
        
        print(f"Student {student.name} enrolled successfully in {course.name}")


    @staticmethod
    def drop_student_from_course(student, course):
        """Drop student from a course"""
        # Check if student is enrolled
        enrolled_courses = student.get_courses()
        if course.name not in enrolled_courses:
            print(f"Student not enrolled in {course.name}")
            return
        
        # Remove course from student
        student.remove_course(course.name)
        
        # Remove student from course
        course.remove_student(student)
            
        print(f"Student {student.name} dropped from {course.name}")


    @staticmethod
    def add_grade_to_student(student, course_name, grade_value):
        """Add a grade to student for a specific course"""
        # Validate grade value
        if not (MIN_GRADE <= grade_value <= MAX_GRADE):
            print("Grade must be between 0 and 100")
            return
        
        # Check if student is enrolled in the course
        enrolled_courses = student.get_courses()
        course_names = [course for course in enrolled_courses]
        
        if course_name not in course_names:
            print(f"Student not enrolled in {course_name}")
            return
        
        # Create Grade object
        new_grade = Grade(course_name, grade_value)
        
        # Add to student's grades
        student.add_grade(new_grade)

    @staticmethod
    def calculate_average_grade(student):
        """Calculate student's average grade"""
        grades = student.get_grades()
        
        # Handle empty grades
        if not grades:
            print("There are no grades to calculate")
            return None
        
        # Calculate average
        total = sum(grade.grade for grade in grades)
        average = total / len(grades)
        
        return average


    @staticmethod
    def display_full_info(student):
        """Display complete student information"""
        print('-' * 50)
        print('-' * 15, 'Student Profile', '-' * 15)
        print('-' * 50)
        
        print(f"Name: {student.name}")
        print(f"Age: {student.age}")
        print(f"Gender: {student.gender}")
        print(f"Student ID: {student.student_id}")
        print()
        
        # Display courses
        print("Enrolled Courses:")
        courses = student.get_courses()
        if courses:
            for course in courses:
                print(f"  - {course}")
        else:
            print("  No courses enrolled")
        print()
        
        # Display grades
        print("Grades:")
        grades = student.get_grades()
        if grades:
            for grade in grades:
                print(f"  - {grade.course_name}: {grade.grade}")
        else:
            print("  No grades yet")
        print()
        
        # Display average
        StudentService.display_student_average(student)
        print('-' * 50)


    @staticmethod
    def display_student_average(student):
        """Display student's average grade and GPA letter"""
        avg = StudentService.calculate_average_grade(student)
        
        if avg is None:
            return
        
        print(f"{student.name}'s Average Grade: {avg:.2f}")
        
        # Calculate letter grade
        if avg >= 90:
            letter = 'A'
        elif avg >= 80:
            letter = 'B'
        elif avg >= 70:
            letter = 'C'
        elif avg >= 60:
            letter = 'D'
        else:
            letter = 'F'
        
        print(f"GPA Letter: {letter}")


    @staticmethod
    def update_student_grade(student, course_name, new_grade):
        """Update a student's grade for a specific course"""
        # Validate new grade
        if not (MIN_GRADE<= new_grade <= MAX_GRADE):
            print("Grade must be between 0 and 100")
            return
        
        # Find the grade to update
        grades = student.get_grades()
        for grade in grades:
            if grade.course_name == course_name:
                # Update the grade
                grade.grade = new_grade
                print(f"Grade updated to {new_grade} for {course_name}")
                return
        
        # If grade not found
        print(f"No grade found for {course_name}")