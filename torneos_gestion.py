# Aquí manejaremos la lógica de gestión de equipos

from conexion_db import obtener_conexion
from datetime import datetime


# Función para traer los id y nombres de los videojuegos para cargar en el combobox
def ver_videojuegos():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT id_videojuego, nombre_videojuego FROM videojuegos")
    resultados = cursor.fetchall()
    conexion.close()
    return resultados

# Función para traer los id nombres de las fases de los torneos para cargar en el combobox
def ver_fases():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("select id_fase, fase FROM fases_torneo")
    resultados = cursor.fetchall()
    conexion.close()
    return resultados

# Función para traer los id, nombres y usuarios de los jugadores para cargar en el combobox
def ver_jugadores():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT id_jugador, nombre_jugador, usuario FROM jugadores")
    resultados = cursor.fetchall()
    conexion.close()
    return resultados

# Manejo de datos, METODO CRUD

# Agregar (Create)
def agregar_torneos(nombre, fecha_inicio, fecha_fin, id_fase, id_videojuego):
    # La fecha de creación se establece automáticamente al momento de agregar el equipo
    fecha_creacion = datetime.now().date()
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO torneos (nombre_torneo, fecha_inicio, fecha_finalizacion, id_fase, id_videojuego) VALUES (%s, %s)", (nombre, fecha_inicio, fecha_fin, id_fase, id_videojuego))
    conexion.commit()
    conexion.close()

# Leer o vizualizar (Read)
def ver_torneos():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM torneos")
    resultados = cursor.fetchall()
    conexion.close()
    return resultados

# Actualizar (Update)
def actualizar_torneos(id_torneo, nuevo_torneo, nueva_fecha_inicio, nueva_fecha_fin, nuevo_id_fase, nuevo_id_videojuego):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("UPDATE torneos SET nombre_torneo = %s, fecha_inicio = %s, fecha_finalizacion = %s, id_fase = %s, id_videojuego = %s WHERE id_torneo = %s", (nuevo_torneo, nueva_fecha_inicio, nueva_fecha_fin, nuevo_id_fase, nuevo_id_videojuego, id_torneo))
    conexion.commit()
    conexion.close()

# Eliminar (Delete)
def eliminar_torneos(id_torneo):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM torneos WHERE id_torneo = %s", (id_torneo))
    conexion.commit()
    conexion.close()

