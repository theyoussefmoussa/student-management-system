from models.student import Student
from models.course import Course
from services.student_service import StudentService
from services.course_service import CourseService
from utils.display import display_menu
from utils.helper import displaying_collectors, pick_course, pick_student
from utils.validators import get_valid_grade

def main():
    students = []
    courses = []

    while True:
        display_menu()
        choice = input("Enter Your Choice: ").strip()

        if choice == "1":
            students.append(Student())
            displaying_collectors('Students', students)
        
        elif choice == "2":
            courses.append(Course())
            displaying_collectors('Courses', courses)
            

        elif choice == "3":
            if not students or not courses:
                print("Create a student and course first")
                continue
            StudentService.enrol_in_course(pick_student(students), pick_course(courses))
       
        elif choice == "4":
            if not students or not courses : 
                print("Create a Student and a Course First")
                continue

            print("Choose Which Student To Add Grade For")
            student = pick_student(students)
            course = pick_course(courses).name
            grade_value = get_valid_grade()
            StudentService.add_grade_to_student(student, course, grade_value)


        elif choice == "5":
            if not students:
                print("Create a student first")
                continue

            StudentService.display_full_info(pick_student(students))

        elif choice == "6":
            if not courses:
                print("Create a course first")
                continue
            CourseService.display_course_info(pick_course(courses))

        elif choice == "7":
            if not students:
                print("Create a student first")
                continue
            StudentService.display_student_average(pick_student(students))

        elif choice == "8":
            if not students or not courses:
                print("Create a student and course first")
                continue
            StudentService.drop_student_from_course(pick_student(students), pick_course(courses))

        elif choice == "9":
            if not students:
                print("Create Student First")
                continue
            if not courses:
                print("Create Courses First")
                continue
            grade = StudentService.get_grade_for_course(pick_student(students), pick_course(courses).name)
            if grade is not None:
                print(grade)


        elif choice == "10":
            if not students or not courses:
                print("Create a student and course first")
                continue
            
            student = pick_student(students)
            course = pick_course(courses).name
            new_grade = get_valid_grade()
            StudentService.update_student_grade(student, course, new_grade)

        elif choice == "0":
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice, try again")

if __name__ == "__main__":
    main()