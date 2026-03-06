from database.connection import get_connection


class GradeRepo: 
    def add_grade(self, student_id, course_id, grade_value): 
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO grades (student_id, course_id, grade_value) VALUES (%s, %s, %s)",
            (student_id, course_id, grade_value,)
        )
        conn.commit()
        state = 'Grade Added Successfully'
        cursor.close()
        conn.close()
        return state
    
    def get_grade(self, student_id, course_id): 
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT student_id, course_id, grade_value FROM grades WHERE student_id = %s AND course_id = %s",
            (student_id, course_id,)
        )
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        return row
    
    def get_all_grades_for_student(self, student_id):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT course_id, grade_value FROM grades WHERE student_id = %s",
            (student_id,)
        )
        row = cursor.fetchall()
        cursor.close()
        conn.close()
        return row
    
    def update_grade(self, student_id, course_id, new_grade):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "UPDATE grades SET grade_value = %s WHERE student_id = %s AND course_id = %s",
            (new_grade, student_id, course_id,)
        )
        conn.commit()
        state = 'Grade Updated Successfully'
        cursor.close()
        conn.close()
        return state
    
    
    def delete_grade(self, student_id, course_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM grades WHERE student_id = %s AND course_id = %s",
            (student_id, course_id)
        )
        conn.commit()
        state = "Grade Deleted Successfully"
        cursor.close()
        conn.close()
        return state