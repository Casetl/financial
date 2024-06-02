import psycopg2

try:
    connection = psycopg2.connect(
        dbname="postgres_db",
        user="postgres_user",
        password="postgres_password",
        host="localhost",
        port="5432"
    )
    cursor = connection.cursor()
    cursor.execute("SELECT 1;")
    print("Conexión exitosa")
    cursor.close()
    connection.close()
except Exception as e:
    print(f"Error de conexión: {e}")