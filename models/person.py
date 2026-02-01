"""
Person: Base class for people in the system
    __init__(name, age, gender, id)
    get_details()
    __str__()
"""

from utils.validators import get_valid_name, get_valid_age, get_valid_gender


class Person:
    def __init__(self):
        self.name = get_valid_name()
        self.age = get_valid_age()
        self.gender = get_valid_gender()
    
    def get_details(self):
        print(f"Hello {self.name}")
        print(f"You are {self.age} years old")
        print(f"You are {self.gender}")
    
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"
    