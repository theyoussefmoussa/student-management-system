from utils.validators import get_valid_course_name, get_valid_credit


class Course:
    def __init__(self):
        self.name = get_valid_course_name()
        self.credit = get_valid_credit()

