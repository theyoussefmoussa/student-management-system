from connection import get_connection

conn = get_connection()
print("Connected successfully!" if conn.is_connected() else "Connection failed!")
conn.close()