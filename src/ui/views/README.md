# Carpeta views/

Esta carpeta contiene todas las vistas específicas de la aplicación KeyPlayer Manager.

## Contenido

### Archivos Principales

#### **welcome.py**
- **Clase**: `WelcomeView`
- **Propósito**: Pantalla de bienvenida que se muestra al iniciar la aplicación
- **Funcionalidad**: Muestra el logo principal y botones de navegación a las secciones principales

### Carpetas Específicas

#### **/torneos/**
Vistas relacionadas con la gestión de torneos:

- **torneo_list.py**: Lista de torneos con opciones de crear, editar, eliminar y ver
- **torneo_create.py**: Formulario para crear nuevos torneos con validación completa
- **torneo_editor.py**: Formulario para editar torneos existentes
- **torneo_ver.py**: Vista de solo lectura para visualizar detalles de un torneo

#### **/jugadores/**
Vistas relacionadas con la gestión de jugadores:

- **jugadores_list.py**: Lista de jugadores con opciones de crear, editar, eliminar y ver
- **jugador_create.py**: Formulario para crear y editar jugadores
- **jugadores_ver.py**: Vista de solo lectura para visualizar detalles de un jugador

#### **/equipo/**
Vistas relacionadas con la gestión de equipos:

- **equipo_list.py**: Lista de equipos con opciones de crear, editar, eliminar y ver
- **equipo_form.py**: Formulario para crear y editar equipos
- **equipo_ver.py**: Vista de solo lectura para visualizar detalles de un equipo

## Patrón de Diseño

Todas las vistas siguen un patrón consistente:

### 1. Vistas de Lista
- Muestran elementos en formato de tabla
- Incluyen botones de acción (crear, editar, eliminar, ver)
- Proporcionan contadores y estadísticas
- Permiten navegación a formularios

### 2. Vistas de Formulario
- Campos de entrada estilizados
- Validación en tiempo real
- Botones de guardar y cancelar
- Manejo de errores con diálogos

### 3. Vistas de Solo Lectura
- Muestran información detallada
- Sin opciones de edición
- Diseño limpio y organizado
- Botón de regreso a la lista

## Características Comunes

### Componentes Utilizados
- `TableView`: Para mostrar listas de datos
- `StyledEntry`: Para campos de entrada
- `StyledCombobox`: Para selecciones
- `RoundedButton`: Para acciones
- `AlertDialog`: Para mensajes de éxito/error
- `ConfirmDialog`: Para confirmaciones

### Validaciones
- Campos obligatorios
- Formatos de fecha válidos
- Nombres únicos
- Números válidos
- Lógica de fechas

### Navegación
- Integración con `main_window.py`
- Callbacks para acciones
- Manejo de parámetros (IDs)
- Transiciones suaves entre vistas

## Responsabilidades

### Presentación
- Mostrar datos de manera clara y organizada
- Proporcionar interfaces intuitivas
- Mantener consistencia visual

### Interacción
- Capturar entrada del usuario
- Validar datos en tiempo real
- Proporcionar feedback inmediato

### Coordinación
- Comunicarse con la capa de datos
- Manejar errores y excepciones
- Coordinar con la ventana principal

## Flujo de Datos

1. **Lectura**: Las vistas obtienen datos desde `/ui/mocks/`
2. **Validación**: Los datos se validan usando modelos de `/models/`
3. **Persistencia**: Los cambios se guardan a través de funciones mock
4. **Actualización**: Las vistas se actualizan automáticamente

## Extensibilidad

La estructura está preparada para agregar nuevas vistas:
- Nuevas entidades (partidas, resultados, etc.)
- Vistas de reportes y estadísticas
- Vistas de configuración
- Vistas de administración 