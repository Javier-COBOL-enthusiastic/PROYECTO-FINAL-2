import json
import os

MOCK_PATH_JUGADORES = os.path.join(os.path.dirname(__file__), "jugadores.json")
MOCK_PATH_EQUIPOS = os.path.join(os.path.dirname(__file__), "equipos.json")

# Carga los jugadores en memoria
with open(MOCK_PATH_JUGADORES, "r", encoding="utf-8") as f:
    _jugadores = json.load(f)

# Equipos
with open(MOCK_PATH_EQUIPOS, "r", encoding="utf-8") as f:
    _equipos = json.load(f)


def get_jugadores():
    return list(_jugadores)


def get_equipos():
    return list(_equipos)


def save_jugadores(jugadores):
    global _jugadores
    _jugadores = list(jugadores)
    with open(MOCK_PATH_JUGADORES, "w", encoding="utf-8") as f:
        json.dump(_jugadores, f, ensure_ascii=False, indent=4)


def save_equipos(equipos):
    global _equipos
    _equipos = list(equipos)
    with open(MOCK_PATH_EQUIPOS, "w", encoding="utf-8") as f:
        json.dump(_equipos, f, ensure_ascii=False, indent=4)


def create_jugador(nombre):
    nombre_lower = nombre.lower()
    if any(j["nombre"].lower() == nombre_lower for j in _jugadores):
        return None  # No agregar duplicados
    new_id = max([j["id"] for j in _jugadores], default=0) + 1
    jugador = {"id": new_id, "nombre": nombre}
    _jugadores.append(jugador)
    save_jugadores(_jugadores)
    return jugador


def create_equipo(nombre, jugadores):
    new_id = max([e["id"] for e in _equipos], default=0) + 1
    equipo = {"id": new_id, "nombre": nombre, "jugadores": jugadores}
    _equipos.append(equipo)
    save_equipos(_equipos)
    return equipo


def update_jugador(jugador_id, nombre):
    for j in _jugadores:
        if j["id"] == jugador_id:
            j["nombre"] = nombre
            break
    save_jugadores(_jugadores)


def update_equipo(equipo_id, nombre, jugadores):
    for e in _equipos:
        if e["id"] == equipo_id:
            e["nombre"] = nombre
            e["jugadores"] = jugadores
            break
    save_equipos(_equipos) 


def delete_jugador(jugador_id):
    global _jugadores
    _jugadores = [j for j in _jugadores if j["id"] != jugador_id]
    save_jugadores(_jugadores)


def delete_equipo(equipo_id):
    global _equipos
    _equipos = [e for e in _equipos if e["id"] != equipo_id]
    save_equipos(_equipos)
