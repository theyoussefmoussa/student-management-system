from database.connection import get_connection


class CourseRepo: 
    def add_course(self, course): 
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO courses (name, credit) VALUES(%s, %s)",
            (course.name, course.credit)
        )
        conn.commit()
        state= 'Course Added Successfully'
        cursor.close()
        conn.close()
        return state
    
    def get_all_courses(self): 
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT course_id, name, credit FROM courses",
        )
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows 
    
    def get_course_by_name(self, course_name): 
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT course_id, name, credit FROM courses WHERE name = %s",
            (course_name,)
        )
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        return row
    def get_course_by_id(self, course_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT course_id, name, credit FROM courses WHERE course_id = %s",
            (course_id,)
        )
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        return row
    
    def delete_course_by_id(self, course_id): 
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM courses WHERE course_id = %s",
            (course_id,)
        )
        state = ''
        if cursor.rowcount == 0: 
            state = "Course Not Found"
        else: 
            state = "Deleted Successfully"
        cursor.close()
        conn.close()
        return state