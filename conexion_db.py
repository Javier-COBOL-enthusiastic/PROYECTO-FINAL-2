import mysql.connector

def obtener_conexion():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="gestion_videojuegos", # De momento así se llama la base de datos
        port=3306
    )
def cerrar_conexion(conexion):
    if conexion.is_connected():
        conexion.close()
        print("Conexión cerrada correctamente.")
    else:
        print("La conexión ya estaba cerrada.")