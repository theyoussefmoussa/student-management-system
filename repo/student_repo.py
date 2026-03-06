from database.connection import get_connection


class StudentRepo : 
    def add_student(self, student) : 
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO students (student_id, name, age, gender) VALUES (%s, %s, %s, %s)",
            (student.student_id, student.name, student.age, student.gender)
        )

        conn.commit()
        state = "Student Added Successfully"
        cursor.close()
        conn.close()
        return state

    
    def get_all_students(self) : 
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT student_id, name, age, gender FROM students",
        )
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows

    def get_student_by_id(self, student_id): 
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT student_id, name, age, gender FROM students WHERE student_id = %s",
            (student_id,)
        )
        row = cursor.fetchone()

        cursor.close()
        conn.close()

        if row: 
            return row
        else : 
            return None
        

    def delete_student(self, student_id) : 
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM students WHERE student_id = %s",
            (student_id,)
        )

        state = ''
        if cursor.rowcount == 0: 
            state = "Student Not Found"
        else: 
            state = "Deleted Successfully"
        cursor.close()
        conn.close()
        return state
