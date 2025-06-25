# Carpeta ui/

Esta carpeta contiene toda la interfaz de usuario de la aplicación KeyPlayer Manager.

## Contenido

### Archivos Principales

#### **main_window.py**
Ventana principal de la aplicación que gestiona:
- Inicialización de la ventana de Tkinter
- Navegación entre diferentes vistas
- Barra lateral con menú de navegación
- Gestión de diálogos de alerta y confirmación
- Coordinación entre vistas y datos

#### **elements.py**
Componentes de interfaz de usuario personalizados:
- `RoundedButton`: Botón con esquinas redondeadas y efectos hover
- `MenuButton`: Botón de menú con efectos visuales
- `TableActionButton`: Botón de acción para tablas con iconos
- `TableView`: Tabla personalizada con diseño moderno
- `StyledEntry`: Campo de entrada con placeholder y esquinas redondeadas
- `StyledCombobox`: Combobox personalizado con dropdown
- `AlertDialog`: Diálogo de alerta modal (éxito/error)
- `ConfirmDialog`: Diálogo de confirmación modal

### Carpetas

#### **/views/**
Contiene las vistas específicas de cada sección:

**/torneos/**
- `torneo_list.py`: Lista de torneos con acciones
- `torneo_create.py`: Formulario para crear torneos
- `torneo_editor.py`: Formulario para editar torneos
- `torneo_ver.py`: Vista de solo lectura de torneos

**/jugadores/**
- `jugadores_list.py`: Lista de jugadores con acciones
- `jugador_create.py`: Formulario para crear/editar jugadores
- `jugadores_ver.py`: Vista de solo lectura de jugadores

**/equipo/**
- `equipo_list.py`: Lista de equipos con acciones
- `equipo_form.py`: Formulario para crear/editar equipos
- `equipo_ver.py`: Vista de solo lectura de equipos

**Archivos generales:**
- `welcome.py`: Vista de bienvenida con navegación principal

#### **/mocks/**
Sistema de datos mock y persistencia:
- `__init__.py`: Funciones CRUD para jugadores, equipos y torneos
- `jugadores.json`: Datos de jugadores en formato JSON
- `equipos.json`: Datos de equipos en formato JSON
- `torneos.json`: Datos de torneos en formato JSON

## Características de la UI

### Diseño Moderno
- Esquinas redondeadas en todos los componentes
- Paleta de colores consistente
- Efectos hover y animaciones suaves
- Tipografía moderna (Consolas)

### Componentes Reutilizables
- Todos los elementos UI están diseñados para ser reutilizables
- Configuración flexible a través de parámetros
- Consistencia visual en toda la aplicación

### Experiencia de Usuario
- Navegación intuitiva con barra lateral
- Feedback visual inmediato
- Diálogos informativos y de confirmación
- Validación en tiempo real

## Patrón de Navegación

La aplicación sigue un patrón de navegación basado en vistas:

1. **WelcomeView**: Pantalla inicial con opciones principales
2. **Vistas de Lista**: Muestran elementos con opciones de acción
3. **Vistas de Formulario**: Para crear o editar elementos
4. **Vistas de Solo Lectura**: Para visualizar detalles

## Gestión de Estado

- Cada vista es independiente y se crea/destruye según sea necesario
- Los datos se mantienen en archivos JSON
- La navegación se maneja centralmente desde `main_window.py`

## Responsabilidades

- **Presentación**: Mostrar datos de manera clara y atractiva
- **Interacción**: Capturar entrada del usuario de manera intuitiva
- **Validación Visual**: Proporcionar feedback inmediato sobre errores
- **Navegación**: Facilitar el movimiento entre diferentes secciones 