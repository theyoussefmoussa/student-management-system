# Student Management System

A command-line interface (CLI) application for managing students, courses, and grades. The system enables developers and technical users to create students, enroll them in courses, assign grades, and compute averages — all through an interactive menu-driven interface.

---

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Classes Overview](#classes-overview)
  - [Core Models](#core-models)
  - [Service Classes](#service-classes)
- [Utils Module](#utils-module)
  - [Constants](#constants)
  - [Validators](#validators)
  - [Display](#display)
  - [Helpers](#helpers)
- [Installation](#installation)
- [Usage](#usage)
- [Menu Options](#menu-options)
- [Configuration](#configuration)
- [Requirements](#requirements)

---

## Features

- **Create Student** — Register a new student with validated personal details and a unique ID
- **Create Course** — Create a new course with a name and credit hours
- **Enroll Student in Course** — Enroll an existing student into an existing course
- **Add Grade to Student** — Assign a grade (0–100) to a student for a specific course
- **Display Student Info** — View a student's full profile, enrolled courses, grades, and average
- **Display Course Info** — View a course's details, enrolled students, and average grade
- **Calculate Student Average** — Compute and display a student's overall grade average with a letter grade
- **Drop Student from Course** — Remove a student's enrollment from a course
- **Get Grade for Course** — Retrieve a student's grade for a specific course
- **Update Student Grade** — Modify an existing grade for a student in a given course

---

## Project Structure

```
student_management_system/
├── main.py
├── models/
│   ├── __init__.py
│   ├── person.py
│   ├── student.py
│   ├── grade.py
│   └── course.py
├── services/
│   ├── __init__.py
│   ├── student_service.py
│   └── course_service.py
└── utils/
    ├── __init__.py
    ├── constants.py
    ├── validators.py
    ├── display.py
    └── helper.py
```

---

## Classes Overview

### Core Models

#### `Person`

The base class representing a person in the system.

| Attribute | Type | Description |
|-----------|------|-------------|
| `name` | `str` | The person's full name |
| `age` | `int` | The person's age |
| `gender` | `str` | The person's gender |

| Method | Return | Description |
|--------|--------|-------------|
| `get_details()` | `None` | Prints the person's name, age, and gender |

---

#### `Student` *(inherits `Person`)*

Represents a student with academic data. Extends `Person` with a unique ID and course/grade tracking.

| Attribute | Type | Description |
|-----------|------|-------------|
| `name` | `str` | Student name (minimum 3 characters) |
| `age` | `int` | Student age (range: 17–29) |
| `gender` | `str` | Gender — `Male` or `Female` (case-insensitive input) |
| `student_id` | `str` | Unique numeric ID of fixed length |
| `courses` | `dict` | Dictionary with course names as keys and `Grade` objects as values |

| Method | Return | Description |
|--------|--------|-------------|
| `add_course(course_name)` | `None` | Adds a course to the student's enrolled courses after checking for duplicates |
| `remove_course(course_name)` | `None` | Removes a course from the student's enrolled courses if it exists |
| `get_grade()` | `list` | Returns a list of all `Grade` objects from the courses dictionary |
| `add_grade(course_name, grade)` | `None` | Assigns a `Grade` object to a course after validating enrollment and checking for existing grades |
| `get_courses()` | `list` | Returns a list of enrolled course names |

---

#### `Grade`

Represents a grade entry for a specific course.

| Attribute | Type | Description |
|-----------|------|-------------|
| `course_name` | `str` | The name of the course this grade belongs to |
| `grade` | `int` | The numeric grade value (0–100) |

> Both attributes can be passed as parameters during instantiation or entered by the user at runtime with input validation.

---

#### `Course`

Represents a course offered in the system.

| Attribute | Type | Description |
|-----------|------|-------------|
| `name` | `str` | The course name |
| `credit` | `int` | Credit hours of the course (range: 2–5) |
| `enrolled_students` | `list` | List of `Student` objects enrolled in this course |

| Method | Return | Description |
|--------|--------|-------------|
| `add_student(student)` | `None` | Adds a student to the enrolled students list |
| `remove_student(student)` | `None` | Removes a student from the enrolled list if found |
| `get_students()` | `list` | Returns the list of enrolled students |
| `get_students_count()` | `int` | Returns the number of students enrolled in the course |

---

### Service Classes

Service classes contain **static methods** only and are responsible for all business logic. They act as the bridge between user actions and the core models.

#### `StudentService`

| Method | Return | Description |
|--------|--------|-------------|
| `get_grade_for_course(student, course_name)` | `int` or `None` | Returns the numeric grade value for a specific course, or `None` if not found |
| `enrol_in_course(student, course)` | `None` | Enrolls a student in a course by updating both the student and course records |
| `drop_student_from_course(student, course)` | `None` | Removes a student from a course by updating both records |
| `add_grade_to_student(student, course_name, grade_value)` | `None` | Validates and assigns a grade to a student for a given course |
| `calculate_average_grade(student)` | `float` or `None` | Calculates and returns the student's overall grade average |
| `display_full_info(student)` | `None` | Prints the student's personal data, enrolled courses, grades, and average |
| `display_student_average(student)` | `None` | Displays the student's average grade along with the corresponding letter grade (A, B, C, D, F) |
| `update_student_grade(student, course_name, new_grade)` | `None` | Updates an existing grade for a student in a specified course after validation |

---

#### `CourseService`

| Method | Return | Description |
|--------|--------|-------------|
| `display_course_info(course)` | `None` | Prints the course name, credit hours, enrolled student count, student IDs, and the course average grade |
| `get_course_average(course)` | `float` or `None` | Calculates and returns the average grade across all enrolled students for the course |

---

## Utils Module

### Constants

Defined in `constants.py`. All application-wide configuration values are centralized here.

| Constant | Value | Description |
|----------|-------|-------------|
| `CS_COURSES` | list of 20 items | Predefined list of available computer science course names |
| `ID_LENGTH` | `6` | Required length for a student ID |
| `MIN_NAME_LENGTH` | `3` | Minimum number of characters for a student name |
| `MIN_AGE` | `17` | Minimum allowed student age |
| `MAX_AGE` | `29` | Maximum allowed student age |
| `MIN_CREDIT` | `2` | Minimum credit hours for a course |
| `MAX_CREDIT` | `5` | Maximum credit hours for a course |
| `MIN_GRADE` | `0` | Minimum allowed grade value |
| `MAX_GRADE` | `100` | Maximum allowed grade value |

---

### Validators

Defined in `validators.py`. Each function handles user input validation and returns a sanitized value only when all checks pass.

| Function | Return | Description |
|----------|--------|-------------|
| `get_valid_gender()` | `str` | Validates gender input as `Male` or `Female` (case-insensitive) |
| `get_valid_age()` | `int` | Validates age as an integer within the allowed range |
| `get_valid_name()` | `str` | Validates name — non-empty, alphabetic, minimum length, and title-cased |
| `get_valid_unique_id()` | `str` | Validates student ID — numeric, correct length, and unique across the system |
| `get_valid_grade()` | `int` | Validates grade as a positive integer within the allowed range |
| `get_valid_credit()` | `int` | Validates credit hours as a positive integer within the allowed range |
| `get_valid_course_name()` | `str` | Validates course name against the predefined list using case-insensitive matching |

---

### Display

Defined in `display.py`.

| Function | Description |
|----------|-------------|
| `display_menu()` | Prints the main application menu with all 10 available actions and the exit option |

---

### Helpers

Defined in `helper.py`. Utility functions used across the application to reduce redundant code.

| Function | Return | Description |
|----------|--------|-------------|
| `displaying_collectors(label, collectors)` | `None` | Displays all elements of a list (e.g., students or courses) with a label |
| `user_choice(label, choice_collector)` | `int` | Prompts the user to select an item by index, validates the input, and returns the zero-based index |
| `pick_student(students)` | `Student` | Combines `displaying_collectors` and `user_choice` to let the user select a student |
| `pick_course(courses)` | `Course` | Combines `displaying_collectors` and `user_choice` to let the user select a course |

---

## Installation

1. Clone the repository:

```bash
git clone <repository_url>
cd student_management_system
```

2. Ensure you have **Python 3.6+** installed:

```bash
python --version
```

3. No external dependencies are required. The project uses only Python standard libraries.

---

## Usage

Run the application by executing `main.py`:

```bash
python main.py
```

The system will display the main menu. Enter the corresponding number to perform an action. Enter `0` to exit.

---

## Menu Options

| Option | Action |
|--------|--------|
| `1` | Create Student |
| `2` | Create Course |
| `3` | Enroll Student in Course |
| `4` | Add Grade to Student |
| `5` | Display Student Info |
| `6` | Display Course Info |
| `7` | Calculate Student Average |
| `8` | Drop Student from Course |
| `9` | Get Grade for Course |
| `10` | Update Student Grade |
| `0` | Exit |

---

## Configuration

All system-wide limits and predefined data are managed in `utils/constants.py`. To adjust any of the following, modify the corresponding value in that file:

- Student age range
- Name length requirement
- Student ID length
- Grade and credit hour ranges
- Available course list

---

## Requirements

- Python 3.6 or higher
- No third-party libraries required