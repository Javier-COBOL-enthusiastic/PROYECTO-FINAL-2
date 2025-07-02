# KeyPlayer Manager

## Descripción
KeyPlayer Manager es una aplicación de gestión de torneos de videojuegos desarrollada en Python con Tkinter. Permite administrar jugadores, equipos y torneos de manera eficiente con una interfaz de usuario moderna y intuitiva.

## Características
- **Gestión de Jugadores**: Crear, editar, eliminar y visualizar jugadores
- **Gestión de Equipos**: Administrar equipos y asignar jugadores
- **Gestión de Torneos**: Crear y gestionar torneos con fechas, juegos y equipos participantes
- **Interfaz Moderna**: Diseño con esquinas redondeadas y efectos visuales
- **Validación de Datos**: Validación completa de formularios y datos de entrada
- **Almacenamiento Local**: Datos persistentes en archivos JSON

## Estructura del Proyecto

```
src/
├── main.py                 # Punto de entrada de la aplicación
├── models/                 # Modelos de datos
├── ui/                     # Interfaz de usuario
│   ├── elements.py         # Componentes UI personalizados
│   ├── main_window.py      # Ventana principal
│   ├── views/              # Vistas de la aplicación
│   └── mocks/              # Datos mock y funciones de persistencia
├── controllers/            # Controladores (futuro)
├── config/                 # Configuración (futuro)
└── assets/                 # Recursos (imágenes, etc.)
```

## Instalación y Uso

### Requisitos
- Python 3.7 o superior
- Tkinter (incluido con Python)

### Ejecución
1. Navega al directorio del proyecto
2. Ejecuta el archivo principal:
```bash
python src/main.py
```

## Tecnologías Utilizadas
- **Python**: Lenguaje principal
- **Tkinter**: Framework de interfaz gráfica
- **JSON**: Almacenamiento de datos
- **Math**: Matemáticas

## Funcionalidades Principales

### Gestión de Jugadores
- Crear nuevos jugadores con nombre y puntos
- Editar información de jugadores existentes
- Eliminar jugadores del sistema
- Visualizar lista completa de jugadores

### Gestión de Equipos
- Crear equipos y asignar jugadores
- Editar composición de equipos
- Eliminar equipos
- Ver detalles de equipos

### Gestión de Torneos
- Crear torneos con nombre, juego, fechas y número de equipos
- Validación completa de datos de torneo
- Editar torneos existentes
- Eliminar torneos
- Visualizar información de torneos

## Validaciones Implementadas
- Nombres únicos para jugadores y torneos
- Formato de fechas válido (dd/mm/yyyy)
- Fechas lógicas (fecha fin posterior a fecha inicio)
- Campos obligatorios completos
- Números válidos para puntos y cantidad de equipos

## Interfaz de Usuario
La aplicación cuenta con una interfaz moderna que incluye:
- Barra lateral de navegación
- Botones con esquinas redondeadas
- Efectos hover y animaciones
- Diálogos de confirmación y alerta
- Campos de entrada estilizados
- Tablas personalizadas para mostrar datos

## Desarrollo
Este proyecto está estructurado siguiendo principios de programación orientada a objetos y separación de responsabilidades. Cada módulo tiene una función específica y está bien documentado.

## Autor
Desarrollado como proyecto final de programación.
