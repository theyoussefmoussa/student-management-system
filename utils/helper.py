from repo.student_repo import StudentRepo
from repo.course_repo import CourseRepo

student_repo = StudentRepo()
course_repo = CourseRepo()

def user_choice(lablel, choice_collector) : 
    while True:
        choice = input(f"Enter Your {lablel} ")
        
        # Step 1: Check if valid number
        if not choice.isdecimal():
            print("Please Enter A Valid Choice")
            continue
        # Step 2: Convert to int
        choice = int(choice)
        
        # Step 3: Check range from 0 to n-1
        if choice in range(1, len(choice_collector)+1) : 
            return choice - 1 # to validate index
        else : 
            print("Try Again Later")

def pick_student():
    students = student_repo.get_all_students()
    print("All Students")
    for index, student in enumerate(students, 1):
        print(f"{index}. {student[1]}")  # [1] = name
    student_index = user_choice('Students', students)
    return students[student_index][0]  # [0] = student_id

def pick_course():
    courses = course_repo.get_all_courses()
    print("All Courses")
    for index, course in enumerate(courses, 1):
        print(f"{index}. {course[1]}")  # [1] = name
    course_index = user_choice('Courses', courses)
    return courses[course_index][1]  # [1] = name