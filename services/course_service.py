"""
CourseService: Handles course-related business logic
"""

from repo.course_repo import CourseRepo
from repo.enrollment_repo import EnrollmentRepo
from repo.grade_repo import GradeRepo

course_repo = CourseRepo()
enrollment_repo = EnrollmentRepo()
grade_repo = GradeRepo()

class CourseService:

    @staticmethod
    def get_course_average(course_id):
        """Calculate average grade for all students in the course"""
        students = enrollment_repo.get_students_for_course(course_id)
        
        if not students:
            print(f"No students enrolled in {course_id}")
            return None
        
        total_grade = 0
        grade_count = 0
        
        for student in students:
            grade = grade_repo.get_grade(student[0], course_id)
            if grade:
                total_grade += grade[2]
                grade_count += 1
        
        if grade_count == 0:
            print(f"No grades recorded for {course_id}")
            return None
        
        average = total_grade / grade_count
        return average
    
    
    @staticmethod
    def display_course_info(course_name):
        """Display complete course information"""
        print('-' * 50)
        course = course_repo.get_course_by_name(course_name)

        if not course:
            print(f"Course {course_name} Not Found")
            return

        course_id   = course[0]
        course_name = course[1]
        course_credit = course[2]

        print(f"Course: {course_name}")
        print(f"Credits: {course_credit}")

        students = enrollment_repo.get_students_for_course(course_id)
        print(f"Enrolled Students: {len(students)}")
        print()
        
        if students:
            print("Students:")
            for student in students:
                print(f"  - ID: {student[0]}")
        else:
            print("No students enrolled yet")
        print()
        
        avg = CourseService.get_course_average(course_id)
        if avg is not None:
            print(f"Course Average: {avg:.2f}")
        
        print('-' * 50)