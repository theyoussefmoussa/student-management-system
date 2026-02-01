def displaying_collectors(label, collectors):
    print(f"All {label}")
    for index,collector in enumerate(collectors, 1): 
        print(f"{index}. {collector}")


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


def pick_student(students):
    displaying_collectors('Students', students)
    student_index = user_choice('Students', students)
    return students[student_index]

def pick_course(courses) : 
    displaying_collectors('Courses', courses)
    course_index = user_choice('Courses', courses)
    return courses[course_index]
