# Aquí manejaremos la lógica de gestión de equipos

from config.conexion_db import obtener_conexion
from datetime import datetime


def ver_equipos():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM equipos")
    resultados = cursor.fetchall()
    conexion.close()
    return resultados


def agregar_equipo(nombre):
    # La fecha de creación se establece automáticamente al momento de agregar el equipo
    fecha_creacion = datetime.now().date()
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute(
        "INSERT INTO equipos (nombre_equipo, fecha_creacion) VALUES (%s, %s)",
        (nombre, fecha_creacion),
    )
    conexion.commit()
    conexion.close()


def eliminar_equipo(id_equipo):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM equipos WHERE id_equipo = %s", (id_equipo))
    conexion.commit()
    conexion.close()


def actualizar_equipo(id_equipo, nuevo_nombre, nueva_fecha_creacion):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute(
        "UPDATE equipos SET nombre_equipo = %s, fecha_creacion = %s WHERE id_equipo = %s",
        (nuevo_nombre, nueva_fecha_creacion, id_equipo),
    )
    conexion.commit()
    conexion.close()
