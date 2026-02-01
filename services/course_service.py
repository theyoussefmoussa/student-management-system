"""
CourseService: Handles course-related business logic
"""

class CourseService:

    @staticmethod
    def get_course_average(course):
        """Calculate average grade for all students in the course"""
        students = course.get_students()
        
        if not students:
            print(f"No students enrolled in {course.name}")
            return None
        
        # Collect all grades for this course from all students
        total_grade = 0
        grade_count = 0
        
        for student in students:
            grades = student.get_grades()
            for grade in grades:
                if grade.course_name == course.name:
                    total_grade += grade.grade
                    grade_count += 1
        
        if grade_count == 0:
            print(f"No grades recorded for {course.name}")
            return None
        
        average = total_grade / grade_count
        return average
    
    
    @staticmethod
    def display_course_info(course):
        """Display complete course information"""
        print('-' * 50)
        print(f"Course: {course.name}")
        print(f"Credits: {course.credits}")
        print(f"Enrolled Students: {course.get_students_count()}")
        print()
        
        # Display student list
        students = course.get_students()
        if students:
            print("Students:")
            for student in students:
                print(f"  - {student.name} (ID: {student.student_id})")
        else:
            print("No students enrolled yet")
        print()
        
        # Display course average
        avg = CourseService.get_course_average(course)
        if avg is not None:
            print(f"Course Average: {avg:.2f}")
        
        print('-' * 50)