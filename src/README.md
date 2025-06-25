# Carpeta src/

Esta carpeta contiene el código fuente principal de la aplicación KeyPlayer Manager.

## Contenido

### Archivos Principales
- **main.py**: Punto de entrada de la aplicación. Inicializa la ventana principal y ejecuta la aplicación.

### Carpetas

#### `/models/`
Contiene los modelos de datos de la aplicación:
- **torneo.py**: Clase Torneo y excepciones personalizadas para validación de datos de torneos

#### `/ui/`
Contiene toda la interfaz de usuario:
- **main_window.py**: Ventana principal de la aplicación con navegación y gestión de vistas
- **elements.py**: Componentes UI personalizados (botones, tablas, campos de entrada, diálogos)
- **/views/**: Vistas específicas de cada sección de la aplicación
- **/mocks/**: Datos mock y funciones de persistencia usando archivos JSON

#### `/controllers/`
Carpeta preparada para futuros controladores de la aplicación (actualmente vacía)

#### `/config/`
Carpeta preparada para archivos de configuración (actualmente vacía)

#### `/assets/`
Recursos de la aplicación:
- **/images/**: Iconos, logos e imágenes utilizadas en la interfaz

#### `/venv/`
Entorno virtual de Python (no incluido en el control de versiones)

## Estructura de Navegación

La aplicación sigue un patrón de navegación basado en vistas:
1. **WelcomeView**: Pantalla de bienvenida con botones de navegación
2. **TorneoView**: Lista y gestión de torneos
3. **EquipoView**: Lista y gestión de equipos  
4. **JugadoresView**: Lista y gestión de jugadores

Cada vista puede tener subvistas para crear, editar o visualizar elementos específicos.

## Flujo de Datos

1. Los datos se almacenan en archivos JSON en `/ui/mocks/`
2. Las funciones de persistencia están en `/ui/mocks/__init__.py`
3. Los modelos validan los datos antes de su almacenamiento
4. Las vistas consumen y muestran los datos a través de las funciones mock 