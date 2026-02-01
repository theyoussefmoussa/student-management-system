from utils.validators import get_valid_course_name, get_valid_grade


class Grade:
    def __init__(self, course_name=None, grade=None): # to use it when creating Grade Object with values as parameters
        self.course_name = course_name if course_name else get_valid_course_name()
        self.grade = grade if grade is not None else get_valid_grade()

    def __str__(self):
        return f"{self.course_name}: {self.grade}"