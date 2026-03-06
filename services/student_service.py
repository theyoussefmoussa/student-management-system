"""
StudentService: Handles student-related business logic
"""
from repo.student_repo import StudentRepo
from repo.course_repo import CourseRepo
from repo.enrollment_repo import EnrollmentRepo
from repo.grade_repo import GradeRepo
from utils.constants import MAX_GRADE, MIN_GRADE

student_repo = StudentRepo()
course_repo = CourseRepo()
enrollment_repo = EnrollmentRepo()
grade_repo = GradeRepo()


class StudentService: 

    @staticmethod
    def get_grade_for_course(student_id, course_name):
        """Get student's grade for a specific course"""
        course = course_repo.get_course_by_name(course_name)
        if not course: 
            print(f"Course {course_name} Not Found")
            return None
        course_id = course[0]

        grade = grade_repo.get_grade(student_id, course_id)
        if not grade: 
            print(f"No Grades Found for {course_name}")
            return None
        return grade[2]

    @staticmethod
    def enrol_in_course(student_id, course_name):
        """Enroll student in a course"""
        # Get course_id from database
        course = course_repo.get_course_by_name(course_name)
        if not course:
            print(f"Course {course_name} Not Found")
            return
        course_id = course[0]

        # Check if already enrolled
        if enrollment_repo.is_enrolled(student_id, course_id):
            print(f"Already enrolled in {course_name}")
            return
        
        enrollment_repo.enroll_student(student_id, course_id)
        print(f"Student {student_id} Has Enrolled {course_name} Successfully")

    @staticmethod
    def drop_student_from_course(student_id, course_name):
        """Drop student from a course"""
        # Get course_id from database
        course = course_repo.get_course_by_name(course_name)
        if not course:
            print(f"Course {course_name} Not Found")
            return
        course_id = course[0]

        # Check if student is enrolled
        if not enrollment_repo.is_enrolled(student_id, course_id):
            print(f"Student not enrolled in {course_name}")
            return
        
        enrollment_repo.drop_student(student_id, course_id)
        grade_repo.delete_grade(student_id, course_id)
        print(f"Student {student_id} dropped from {course_name}")

    @staticmethod
    def add_grade_to_student(student_id, course_name, grade_value):
        """Add a grade to student for a specific course"""
        # Validate grade value
        if not (MIN_GRADE <= grade_value <= MAX_GRADE):
            print("Grade must be between 0 and 100")
            return
        
        # Get course_id from database
        course = course_repo.get_course_by_name(course_name)
        if not course:
            print(f"Course {course_name} Not Found")
            return
        course_id = course[0]

        # Check if student is enrolled
        if not enrollment_repo.is_enrolled(student_id, course_id):
            print(f"Student {student_id} is not enrolled in {course_name}")
            return
        
        grade_repo.add_grade(student_id, course_id, grade_value)
        print("Grade Added Successfully")

    @staticmethod
    def calculate_average_grade(student_id):
        """Calculate student's average grade"""
        grades = grade_repo.get_all_grades_for_student(student_id)
        
        if not grades:
            print("There are no grades to calculate")
            return None
        total = sum(grade[1] for grade in grades)  # [1] = grade_value
        average = total / len(grades)
        return average

    @staticmethod
    def display_full_info(student_id):
        """Display complete student information"""
        print('-' * 50)
        print('-' * 15, 'Student Profile', '-' * 15)
        print('-' * 50)
        
        student = student_repo.get_student_by_id(student_id)
        print(f"Name: {student[1]}")
        print(f"Age: {student[2]}")
        print(f"Gender: {student[3]}")
        print(f"Student ID: {student_id}")
        print()
        
        # Display courses
        print("Enrolled Courses:")
        courses = enrollment_repo.get_courses_for_student(student_id)
        if courses:
            for course in courses:
                course_data = course_repo.get_course_by_id(course[0])
                print(f"  - {course_data[1]}")
        else:
            print("  No courses enrolled")
        print()
                
        # Display grades
        print("Grades:")
        grades = grade_repo.get_all_grades_for_student(student_id)
        if grades:
            for grade in grades:
                course_data = course_repo.get_course_by_id(grade[0])  # grade[0] = course_id
                print(f"  - {course_data[1]}: {grade[1]}")            # course name: grade value
        else:
            print("  No grades yet")
        print()
        
        StudentService.display_student_average(student_id)
        print('-' * 50)

    @staticmethod
    def display_student_average(student_id):
        """Display student's average grade and GPA letter"""
        student = student_repo.get_student_by_id(student_id)
        student_name = student[1]

        avg = StudentService.calculate_average_grade(student_id)
        if avg is None:
            return
        
        print(f"{student_name}'s Average Grade: {avg:.2f}")
        
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
    def update_student_grade(student_id, course_name, new_grade):
        """Update a student's grade for a specific course"""
        # Validate new grade
        if not (MIN_GRADE <= new_grade <= MAX_GRADE):
            print("Grade must be between 0 and 100")
            return
        
        # Get course_id from database
        course = course_repo.get_course_by_name(course_name)
        if not course:
            print(f"Course {course_name} Not Found")
            return
        course_id = course[0]

        # Check if grade exists
        grade = grade_repo.get_grade(student_id, course_id)
        if not grade:
            print(f"No grade found for {course_name}")
            return
        
        grade_repo.update_grade(student_id, course_id, new_grade)
        print("Grade Updated Successfully")