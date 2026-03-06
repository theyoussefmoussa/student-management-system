CREATE DATABASE student_management_system;
USE student_management_system;

CREATE TABLE students (
    student_id VARCHAR(6) PRIMARY KEY,
    name       VARCHAR(100) NOT NULL,
    age        INT NOT NULL,
    gender     VARCHAR(10) NOT NULL
);

CREATE TABLE courses (
    course_id  INT AUTO_INCREMENT PRIMARY KEY,
    name       VARCHAR(100) NOT NULL UNIQUE,
    credit     INT NOT NULL
);

CREATE TABLE enrollments (
    student_id VARCHAR(6) NOT NULL,
    course_id  INT NOT NULL,
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (course_id)  REFERENCES courses(course_id)   ON DELETE CASCADE
);

CREATE TABLE grades (
    id          INT AUTO_INCREMENT PRIMARY KEY,
    student_id  VARCHAR(6) NOT NULL,
    course_id   INT NOT NULL,
    grade_value INT NOT NULL,
    UNIQUE (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (course_id)  REFERENCES courses(course_id)   ON DELETE CASCADE
);