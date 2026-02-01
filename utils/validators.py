from utils.constants import CS_COURSES, ID_LENGTH, MAX_AGE, MAX_CREDIT, MAX_GRADE, MIN_AGE, MIN_CREDIT, MIN_GRADE, MIN_NAME_LENGTH


_used_student_ids = set()

def get_valid_gender() : 
    genders = ["Female", "Male"]
    while True : 
        gender = input("Enter Your Gender: ").strip().capitalize()
        if gender in genders : 
            return gender
        print("Invalid Gender, Must be 'Male' or 'Female'")

def get_valid_name() : 
    while True : 
        name = input('Enter Your Name: ')
        if not name: 
            print("Enter A Valid Name")
            continue
        
        if len(name) < MIN_NAME_LENGTH : 
            print("Your Name Must Be Atleast 3 Letters")
            continue # To Skip This Iteration
        if name.replace(" ", "").isalpha() : 
            return name.title()
        else : 
            print("Your Name Contains Only Letters..")
        


def get_valid_age():
    while True:
        age = input("Enter Your Age: ")
        
        # Step 1: Check if valid number
        if not age.isdecimal():
            print("Please Enter A Valid Age")
            continue
        # Step 2: Convert to int
        age = int(age)
        
        # Step 3: Check range
        if MIN_AGE <= age <= MAX_AGE: 
            return age
        else : 
            print("Enter An Age in Range of (17~29)")

def get_valid_unique_id() : 
    while True : 
        id = input("Enter Your ID: ")
        
        if not id : 
            print("ID CAN'T Be Empty")
            continue
        
        elif not id.isnumeric() : 
            print("Only Digits Allowed")
            continue
        
        elif len(id) != ID_LENGTH : 
            print("Length Must Be 6 Digits")
            continue
        elif id in _used_student_ids : 
            print(f"ID '{id}' Is Already Taken, Try Different One")
        else : 
            _used_student_ids.add(id) # Added To Set
            return id
        


def get_valid_grade() : 
    while True : 
        grade = input("Enter Your Grade: ")
        if not grade.isdecimal() : 
            print("Grade Must Be Positive Numbers")
            continue
        
        grade = int(grade)

        if MIN_GRADE <= grade <= MAX_GRADE : 
            return grade
        print("Write A Grade Between 0 and 100")
            


def get_valid_credit() : 
    while True : 
        credit = input("Enter Subject's Credit: ")

        if not credit.isdecimal() :
            print("Credit Must Be Positive Number")
            continue
        credit = int(credit)

        if MIN_CREDIT <= credit <= MAX_CREDIT : 
            return credit
        print("Enter A Valid Credit")


def get_valid_course_name() : 
    while True:
        course = input("Enter Your Course Name: ").strip()
        
        if not course:
            print("Course Name Can't Be Empty")
            continue
        
        # Case-insensitive search
        for valid_course in CS_COURSES:
            if course.lower() == valid_course.lower():
                return valid_course  # Return the correct format
        
        print(f"'{course}' is not a valid course")
        print("Available courses:")
        for c in CS_COURSES[:5]:  # Show first 5 as examples
            print(f"  - {c}")
        print("  ...")
        
