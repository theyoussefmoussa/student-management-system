from models.person import Person
from utils.validators import get_valid_unique_id


class Student(Person):
    def __init__(self):
        super().__init__()
        self.student_id = get_valid_unique_id()
