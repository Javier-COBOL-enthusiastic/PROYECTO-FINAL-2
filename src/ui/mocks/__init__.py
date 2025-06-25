"""
Módulo de datos mock para la aplicación KeyPlayer Manager
Este módulo proporciona funciones para simular una base de datos
usando archivos JSON para almacenar jugadores, equipos y torneos.
"""

import json
import os

# Rutas a los archivos JSON de datos mock
MOCK_PATH_JUGADORES = os.path.join(os.path.dirname(__file__), "jugadores.json")
MOCK_PATH_EQUIPOS = os.path.join(os.path.dirname(__file__), "equipos.json")
MOCK_PATH_TORNEOS = os.path.join(os.path.dirname(__file__), "torneos.json")

# Carga los jugadores en memoria desde el archivo JSON
with open(MOCK_PATH_JUGADORES, "r", encoding="utf-8") as f:
    _jugadores = json.load(f)

# Carga los equipos en memoria desde el archivo JSON
with open(MOCK_PATH_EQUIPOS, "r", encoding="utf-8") as f:
    _equipos = json.load(f)

# Carga los torneos en memoria desde el archivo JSON
with open(MOCK_PATH_TORNEOS, "r", encoding="utf-8") as f:
    _torneos = json.load(f)


def get_jugadores():
    """
    Obtiene la lista completa de jugadores
    
    Returns:
        list: Lista de diccionarios con datos de jugadores
    """
    return list(_jugadores)


def get_equipos():
    """
    Obtiene la lista completa de equipos
    
    Returns:
        list: Lista de diccionarios con datos de equipos
    """
    return list(_equipos)

def get_torneos():
    """
    Obtiene la lista completa de torneos
    
    Returns:
        list: Lista de diccionarios con datos de torneos
    """
    return list(_torneos)

def save_torneos(torneos):
    """
    Guarda la lista de torneos en el archivo JSON
    
    Args:
        torneos: Lista de torneos a guardar
    """
    global _torneos
    _torneos = list(torneos)
    with open(MOCK_PATH_TORNEOS, "w", encoding="utf-8") as f:
        json.dump(_torneos, f, ensure_ascii=False, indent=4)

def create_torneo(torneo):
    """
    Crea un nuevo torneo
    
    Args:
        torneo: Diccionario con los datos del torneo
        
    Returns:
        dict: Torneo creado con ID asignado, o None si ya existe
    """
    nombre_lower = torneo["nombre"].lower()
    if any(j["nombre"].lower() == nombre_lower for j in _torneos):
        return None
    new_id = max([j["id"] for j in _torneos], default=0) + 1
    torneo["id"] = new_id
    _torneos.append(torneo)
    save_torneos(_torneos)
    return torneo

def save_jugadores(jugadores):
    """
    Guarda la lista de jugadores en el archivo JSON
    
    Args:
        jugadores: Lista de jugadores a guardar
    """
    global _jugadores
    _jugadores = list(jugadores)
    with open(MOCK_PATH_JUGADORES, "w", encoding="utf-8") as f:
        json.dump(_jugadores, f, ensure_ascii=False, indent=4)


def save_equipos(equipos):
    """
    Guarda la lista de equipos en el archivo JSON
    
    Args:
        equipos: Lista de equipos a guardar
    """
    global _equipos
    _equipos = list(equipos)
    with open(MOCK_PATH_EQUIPOS, "w", encoding="utf-8") as f:
        json.dump(_equipos, f, ensure_ascii=False, indent=4)


def create_jugador(nombre, puntos=0):
    """
    Crea un nuevo jugador
    
    Args:
        nombre: Nombre del jugador
        puntos: Puntos iniciales del jugador (por defecto 0)
        
    Returns:
        dict: Jugador creado con ID asignado, o None si ya existe
    """
    nombre_lower = nombre.lower()
    if any(j["nombre"].lower() == nombre_lower for j in _jugadores):
        return None  # No agregar duplicados
    new_id = max([j["id"] for j in _jugadores], default=0) + 1
    jugador = {"id": new_id, "nombre": nombre, "puntos": puntos}
    _jugadores.append(jugador)
    save_jugadores(_jugadores)
    return jugador


def create_equipo(nombre, jugadores):
    """
    Crea un nuevo equipo
    
    Args:
        nombre: Nombre del equipo
        jugadores: Lista de IDs de jugadores que pertenecen al equipo
        
    Returns:
        dict: Equipo creado con ID asignado
    """
    new_id = max([e["id"] for e in _equipos], default=0) + 1
    equipo = {"id": new_id, "nombre": nombre, "jugadores": jugadores}
    _equipos.append(equipo)
    save_equipos(_equipos)
    return equipo

def update_torneo(torneo):
    """
    Actualiza un torneo existente
    
    Args:
        torneo: Diccionario con los datos actualizados del torneo
    """
    for j in _torneos:
        if j["id"] == torneo["id"]:
            j = torneo
            break
    save_torneos(_torneos)

def update_jugador(jugador_id, nombre, puntos):
    """
    Actualiza un jugador existente
    
    Args:
        jugador_id: ID del jugador a actualizar
        nombre: Nuevo nombre del jugador
        puntos: Nuevos puntos del jugador
    """
    for j in _jugadores:
        if j["id"] == jugador_id:
            j["nombre"] = nombre
            j["puntos"] = puntos
            break
    save_jugadores(_jugadores)



def update_equipo(equipo_id, nombre, jugadores):
    """
    Actualiza un equipo existente
    
    Args:
        equipo_id: ID del equipo a actualizar
        nombre: Nuevo nombre del equipo
        jugadores: Nueva lista de IDs de jugadores
    """
    for e in _equipos:
        if e["id"] == equipo_id:
            e["nombre"] = nombre
            e["jugadores"] = jugadores
            break
    save_equipos(_equipos) 


def delete_torneo(torneo_id):
    """
    Elimina un torneo por su ID
    
    Args:
        torneo_id: ID del torneo a eliminar
    """
    global _torneos
    _torneos = [j for j in _torneos if j["id"] != torneo_id]
    save_torneos(_torneos)

def delete_jugador(jugador_id):
    """
    Elimina un jugador por su ID
    
    Args:
        jugador_id: ID del jugador a eliminar
    """
    global _jugadores
    _jugadores = [j for j in _jugadores if j["id"] != jugador_id]
    save_jugadores(_jugadores)


def delete_equipo(equipo_id):
    """
    Elimina un equipo por su ID
    
    Args:
        equipo_id: ID del equipo a eliminar
    """
    global _equipos
    _equipos = [e for e in _equipos if e["id"] != equipo_id]
    save_equipos(_equipos)
