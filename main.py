from models.student import Student
from models.course import Course
from services.student_service import StudentService
from services.course_service import CourseService
from utils.display import display_menu
from utils.helper import pick_course, pick_student
from utils.validators import get_valid_grade
from repo.student_repo import StudentRepo
from repo.course_repo import CourseRepo

student_repo = StudentRepo()
course_repo = CourseRepo()

def main():

    while True:
        display_menu()
        choice = input("Enter Your Choice: ").strip()

        if choice == "1":
            student = Student()
            student_repo.add_student(student)
        
        elif choice == "2":
            course = Course()
            print(course_repo.add_course(course))
            

        elif choice == "3":
            StudentService.enrol_in_course(pick_student(), pick_course())
       
        elif choice == "4":
            print("Choose Which Student To Add Grade For")
            student = pick_student()
            course = pick_course()
            grade_value = get_valid_grade()
            StudentService.add_grade_to_student(student, course, grade_value)


        elif choice == "5":
            StudentService.display_full_info(pick_student())

        elif choice == "6":
            CourseService.display_course_info(pick_course())

        elif choice == "7":
            StudentService.display_student_average(pick_student())

        elif choice == "8":
            StudentService.drop_student_from_course(pick_student(), pick_course())

        elif choice == "9":
            grade = StudentService.get_grade_for_course(pick_student(), pick_course())
            if grade is not None:
                print(grade)


        elif choice == "10":
            student = pick_student()
            course = pick_course()
            new_grade = get_valid_grade()
            StudentService.update_student_grade(student, course, new_grade)

        elif choice == "0":
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice, try again")

if __name__ == "__main__":
    main()