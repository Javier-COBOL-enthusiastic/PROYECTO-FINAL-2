# Carpeta mocks/

Esta carpeta contiene el sistema de datos mock y persistencia de la aplicación KeyPlayer Manager.

## Contenido

### Archivos

#### **__init__.py**
Módulo principal que contiene todas las funciones de gestión de datos:

**Funciones de Lectura:**
- `get_jugadores()`: Obtiene la lista completa de jugadores
- `get_equipos()`: Obtiene la lista completa de equipos
- `get_torneos()`: Obtiene la lista completa de torneos

**Funciones de Creación:**
- `create_jugador(nombre, puntos)`: Crea un nuevo jugador
- `create_equipo(nombre, jugadores)`: Crea un nuevo equipo
- `create_torneo(torneo)`: Crea un nuevo torneo

**Funciones de Actualización:**
- `update_jugador(jugador_id, nombre, puntos)`: Actualiza un jugador existente
- `update_equipo(equipo_id, nombre, jugadores)`: Actualiza un equipo existente
- `update_torneo(torneo)`: Actualiza un torneo existente

**Funciones de Eliminación:**
- `delete_jugador(jugador_id)`: Elimina un jugador por su ID
- `delete_equipo(equipo_id)`: Elimina un equipo por su ID
- `delete_torneo(torneo_id)`: Elimina un torneo por su ID

**Funciones de Persistencia:**
- `save_jugadores(jugadores)`: Guarda la lista de jugadores en JSON
- `save_equipos(equipos)`: Guarda la lista de equipos en JSON
- `save_torneos(torneos)`: Guarda la lista de torneos en JSON

#### **jugadores.json**
Archivo JSON que almacena los datos de jugadores:
```json
[
  {
    "id": 1,
    "nombre": "Nombre del Jugador",
    "puntos": 100
  }
]
```

#### **equipos.json**
Archivo JSON que almacena los datos de equipos:
```json
[
  {
    "id": 1,
    "nombre": "Nombre del Equipo",
    "jugadores": [1, 2, 3]
  }
]
```

#### **torneos.json**
Archivo JSON que almacena los datos de torneos:
```json
[
  {
    "id": 1,
    "nombre": "Nombre del Torneo",
    "juego": "Nombre del Juego",
    "fecha_inicio": "01/01/2024",
    "fecha_fin": "31/01/2024",
    "num_equipos": 8
  }
]
```

## Características

### Persistencia de Datos
- Los datos se almacenan en archivos JSON
- Carga automática al iniciar la aplicación
- Guardado automático al realizar cambios
- Codificación UTF-8 para soporte de caracteres especiales

### Validaciones
- Verificación de nombres únicos
- Generación automática de IDs
- Prevención de duplicados
- Manejo de errores de archivo

### Gestión de Memoria
- Datos cargados en memoria para acceso rápido
- Actualización sincronizada entre memoria y archivo
- Liberación automática de recursos

## Uso

### Importación
```python
from ui.mocks import get_jugadores, create_jugador, update_jugador, delete_jugador
```

### Ejemplos de Uso
```python
# Obtener todos los jugadores
jugadores = get_jugadores()

# Crear un nuevo jugador
nuevo_jugador = create_jugador("Juan Pérez", 150)

# Actualizar un jugador
update_jugador(1, "Juan Pérez", 200)

# Eliminar un jugador
delete_jugador(1)
```

## Ventajas del Sistema Mock

### Simplicidad
- No requiere configuración de base de datos
- Fácil de entender y mantener
- Portabilidad completa

### Desarrollo
- Ideal para prototipado rápido
- Fácil de modificar y extender
- Datos persistentes entre sesiones

### Pruebas
- Datos predefinidos para testing
- Fácil reset de datos
- Control total sobre el estado

## Limitaciones

### Escalabilidad
- No recomendado para grandes volúmenes de datos
- Sin transacciones o concurrencia
- Sin índices o consultas complejas

### Funcionalidad
- Sin relaciones complejas entre entidades
- Sin validaciones a nivel de base de datos
- Sin backup automático

## Migración Futura

El sistema está diseñado para facilitar la migración a una base de datos real:
- Interfaces claras y consistentes
- Separación de lógica de negocio
- Funciones con nombres estándar (CRUD)
- Estructura de datos bien definida

## Mantenimiento

### Backup de Datos
- Los archivos JSON se pueden respaldar manualmente
- Formato legible para recuperación manual
- Versionado recomendado para cambios importantes

### Limpieza
- Eliminación de datos obsoletos
- Verificación de integridad de datos
- Optimización de archivos JSON 