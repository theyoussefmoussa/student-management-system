# Student Management System

A command-line interface (CLI) application for managing students, courses, and grades. The system enables developers and technical users to create students, enroll them in courses, assign grades, and compute averages — all through an interactive menu-driven interface.

> **v2.0** — Migrated from in-memory storage to a persistent **MySQL** database using the Repository Pattern.

---

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Database Schema](#database-schema)
- [Classes Overview](#classes-overview)
  - [Core Models](#core-models)
  - [Service Classes](#service-classes)
  - [Repository Classes](#repository-classes)
- [Utils Module](#utils-module)
  - [Constants](#constants)
  - [Validators](#validators)
  - [Display](#display)
  - [Helpers](#helpers)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Menu Options](#menu-options)
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
- **Drop Student from Course** — Remove a student's enrollment and grade from a course
- **Get Grade for Course** — Retrieve a student's grade for a specific course
- **Update Student Grade** — Modify an existing grade for a student in a given course

---

## Project Structure

```
student_management_system/
├── main.py
├── .env                        # Database credentials (not tracked by Git)
├── .gitignore
├── requirements.txt
├── models/
│   ├── person.py
│   ├── student.py
│   └── course.py
├── services/
│   ├── student_service.py
│   └── course_service.py
├── repo/
│   ├── student_repo.py
│   ├── course_repo.py
│   ├── enrollment_repo.py
│   └── grade_repo.py
├── database/
│   ├── connection.py
│   └── schema.sql
└── utils/
    ├── constants.py
    ├── validators.py
    ├── display.py
    └── helper.py
```

---

## Database Schema

The application uses a **MySQL** database with 4 tables:

```
students ──────────────────────────────┐
│ student_id (PK, VARCHAR 6)           │
│ name                                 │
│ age                                  │         enrollments
│ gender                               ├────< student_id (FK)
                                       │     course_id  (FK)
courses ───────────────────────────────┤
│ course_id (PK, AUTO_INCREMENT)       │
│ name (UNIQUE)                        │
│ credit                               │

grades
│ id (PK, AUTO_INCREMENT)
│ student_id (FK → students)
│ course_id  (FK → courses)
│ grade_value
│ UNIQUE (student_id, course_id)
```

All foreign keys use `ON DELETE CASCADE` — deleting a student or course automatically removes all related enrollments and grades.

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

Represents a student. Extends `Person` with a unique ID. Data is persisted in the database via `StudentRepo`.

| Attribute | Type | Description |
|-----------|------|-------------|
| `name` | `str` | Student name (minimum 3 characters) |
| `age` | `int` | Student age (range: 17–29) |
| `gender` | `str` | Gender — `Male` or `Female` (case-insensitive input) |
| `student_id` | `str` | Unique numeric ID of fixed length (6 digits) |

---

#### `Course`

Represents a course offered in the system. Data is persisted in the database via `CourseRepo`.

| Attribute | Type | Description |
|-----------|------|-------------|
| `name` | `str` | The course name (must be from the predefined CS courses list) |
| `credit` | `int` | Credit hours of the course (range: 2–5) |

---

### Service Classes

Service classes contain **static methods** only and are responsible for all business logic. They act as the bridge between user actions and the repositories.

#### `StudentService`

| Method | Return | Description |
|--------|--------|-------------|
| `get_grade_for_course(student_id, course_name)` | `int` or `None` | Returns the numeric grade value for a specific course |
| `enrol_in_course(student_id, course_name)` | `None` | Enrolls a student in a course after checking for duplicate enrollment |
| `drop_student_from_course(student_id, course_name)` | `None` | Removes a student from a course and deletes their grade for it |
| `add_grade_to_student(student_id, course_name, grade_value)` | `None` | Validates and assigns a grade to a student for a given course |
| `calculate_average_grade(student_id)` | `float` or `None` | Calculates and returns the student's overall grade average |
| `display_full_info(student_id)` | `None` | Prints the student's personal data, enrolled courses, grades, and average |
| `display_student_average(student_id)` | `None` | Displays the student's average grade with a letter grade (A, B, C, D, F) |
| `update_student_grade(student_id, course_name, new_grade)` | `None` | Updates an existing grade for a student in a specified course |

---

#### `CourseService`

| Method | Return | Description |
|--------|--------|-------------|
| `display_course_info(course_name)` | `None` | Prints the course name, credit hours, enrolled student count, student IDs, and course average |
| `get_course_average(course_id)` | `float` or `None` | Calculates and returns the average grade across all enrolled students |

---

### Repository Classes

Repositories handle all direct communication with the MySQL database. Each repository is responsible for one table only.

#### `StudentRepo`

| Method | Description |
|--------|-------------|
| `add_student(student)` | Inserts a new student record |
| `get_all_students()` | Returns all students |
| `get_student_by_id(student_id)` | Returns a single student by ID |
| `delete_student(student_id)` | Deletes a student record |

#### `CourseRepo`

| Method | Description |
|--------|-------------|
| `add_course(course)` | Inserts a new course record |
| `get_all_courses()` | Returns all courses |
| `get_course_by_name(course_name)` | Returns a course by name |
| `get_course_by_id(course_id)` | Returns a course by ID |
| `delete_course_by_id(course_id)` | Deletes a course record |

#### `EnrollmentRepo`

| Method | Description |
|--------|-------------|
| `enroll_student(student_id, course_id)` | Creates an enrollment record |
| `drop_student(student_id, course_id)` | Deletes an enrollment record |
| `get_courses_for_student(student_id)` | Returns all course IDs for a student |
| `get_students_for_course(course_id)` | Returns all student IDs for a course |
| `is_enrolled(student_id, course_id)` | Returns `True` if the student is enrolled |

#### `GradeRepo`

| Method | Description |
|--------|-------------|
| `add_grade(student_id, course_id, grade_value)` | Inserts a new grade record |
| `get_grade(student_id, course_id)` | Returns a specific grade |
| `get_all_grades_for_student(student_id)` | Returns all grades for a student |
| `update_grade(student_id, course_id, new_grade)` | Updates an existing grade |
| `delete_grade(student_id, course_id)` | Deletes a grade record |

---

## Utils Module

### Constants

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

| Function | Return | Description |
|----------|--------|-------------|
| `get_valid_gender()` | `str` | Validates gender as `Male` or `Female` (case-insensitive) |
| `get_valid_age()` | `int` | Validates age as an integer within the allowed range |
| `get_valid_name()` | `str` | Validates name — non-empty, alphabetic, minimum length, title-cased |
| `get_valid_unique_id()` | `str` | Validates student ID — numeric, correct length, unique (checked against database) |
| `get_valid_grade()` | `int` | Validates grade as a positive integer within the allowed range |
| `get_valid_credit()` | `int` | Validates credit hours as a positive integer within the allowed range |
| `get_valid_course_name()` | `str` | Validates course name against the predefined list using case-insensitive matching |

---

### Display

| Function | Description |
|----------|-------------|
| `display_menu()` | Prints the main application menu with all 10 available actions and the exit option |

---

### Helpers

| Function | Return | Description |
|----------|--------|-------------|
| `user_choice(label, choice_collector)` | `int` | Prompts the user to select an item by index, validates input, returns zero-based index |
| `pick_student()` | `str` | Fetches students from database, displays them, and returns the selected `student_id` |
| `pick_course()` | `str` | Fetches courses from database, displays them, and returns the selected `course_name` |

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

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create the database by running `database/schema.sql` in your MySQL client:

```bash
mysql -u root -p < database/schema.sql
```

---

## Configuration

Create a `.env` file in the root directory with your database credentials:

```
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=student_management_system
```

> ⚠️ Never commit your `.env` file. It is already listed in `.gitignore`.

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

## Requirements

- Python 3.6 or higher
- MySQL 8.0 or higher
- `mysql-connector-python`
- `python-dotenv`

> Install all dependencies via:
>
> ```bash
> pip install -r requirements.txt
> ```