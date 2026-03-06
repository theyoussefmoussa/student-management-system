from database.connection import get_connection


class EnrollmentRepo: 
    def enroll_student(self, student_id, course_id): 
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO enrollments (student_id, course_id) VALUES (%s, %s)",
            (student_id, course_id)
        )
        conn.commit()
        state = "Student Enrolled Successfully"
        cursor.close()
        conn.close()
        return state
    
    def drop_student(self, student_id, course_id):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            'DELETE FROM enrollments WHERE student_id = %s AND course_id = %s',
            (student_id, course_id)
        ) 
        state = ''
        if cursor.rowcount == 0: 
            state = "Student Or Course Not Found"
        else: 
            state = "Deleted Successfully"
        conn.commit()
        cursor.close()
        conn.close()
        return state
    
    
    
    def get_courses_for_student(self, student_id): 
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT course_id FROM enrollments WHERE student_id = %s",
            (student_id,)
        )
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows 
    
    
    def get_students_for_course(self, course_id): 
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT student_id FROM enrollments WHERE course_id = %s",
            (course_id,)
        )
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows



    def is_enrolled(self, student_id, course_id): 
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT course_id FROM enrollments WHERE student_id = %s AND course_id = %s",
            (student_id,course_id,)
        )
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        return row is not None  # True or False