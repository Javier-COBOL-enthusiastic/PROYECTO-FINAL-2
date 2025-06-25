# Carpeta config/

Esta carpeta está preparada para archivos de configuración de la aplicación KeyPlayer Manager.

## Propósito

Los archivos de configuración centralizarán todas las configuraciones de la aplicación, permitiendo un manejo flexible y mantenible de parámetros, constantes y configuraciones del sistema.

## Estructura Futura Propuesta

### Archivos de Configuración

#### **app_config.py**
Configuración general de la aplicación:
- Configuración de la ventana principal
- Colores y temas
- Fuentes y estilos
- Configuración de idioma

#### **database_config.py**
Configuración de base de datos (futuro):
- Parámetros de conexión
- Configuración de pool de conexiones
- Timeouts y reintentos
- Configuración de transacciones

#### **ui_config.py**
Configuración específica de la interfaz:
- Dimensiones de componentes
- Configuración de animaciones
- Configuración de efectos visuales
- Configuración de responsive design

#### **logging_config.py**
Configuración de logging:
- Niveles de log
- Formato de mensajes
- Destinos de log (archivo, consola)
- Rotación de archivos de log

### Archivos de Configuración por Entorno

#### **config.ini** o **config.json**
Archivo de configuración principal:
- Configuraciones por defecto
- Configuraciones específicas por entorno
- Configuraciones de usuario

#### **.env**
Variables de entorno:
- Configuraciones sensibles
- Configuraciones específicas del entorno
- Configuraciones de desarrollo vs producción

## Beneficios de la Configuración Centralizada

### Flexibilidad
- Cambios de configuración sin modificar código
- Configuraciones específicas por entorno
- Personalización por usuario

### Mantenibilidad
- Configuraciones organizadas y documentadas
- Fácil identificación de parámetros
- Control de versiones de configuración

### Escalabilidad
- Fácil agregar nuevas configuraciones
- Configuraciones por módulo
- Configuraciones dinámicas

## Tipos de Configuración

### Configuración Estática
- Colores y temas
- Dimensiones de ventanas
- Configuraciones de UI
- Constantes de la aplicación

### Configuración Dinámica
- Configuraciones de base de datos
- Configuraciones de red
- Configuraciones de logging
- Configuraciones de rendimiento

### Configuración por Entorno
- Desarrollo
- Pruebas
- Producción
- Personalizada por usuario

## Implementación Futura

### Fases de Desarrollo
1. **Fase 1**: Crear archivos de configuración básicos
2. **Fase 2**: Implementar carga dinámica de configuración
3. **Fase 3**: Agregar validación de configuración
4. **Fase 4**: Implementar configuración por entorno

### Consideraciones Técnicas
- **Validación**: Verificar que las configuraciones sean válidas
- **Valores por Defecto**: Proporcionar valores seguros por defecto
- **Documentación**: Documentar cada configuración
- **Migración**: Facilitar migración de configuraciones existentes

## Ejemplo de Estructura

### app_config.py
```python
# Configuración de la aplicación
WINDOW_CONFIG = {
    'width': 1200,
    'height': 720,
    'title': 'KeyPlayer Manager',
    'resizable': False
}

COLORS = {
    'primary': '#9FACE8',
    'secondary': '#688CCA',
    'background': '#EDEDED',
    'text': '#222'
}

FONTS = {
    'main': ('Consolas', 13),
    'title': ('Consolas', 20, 'bold'),
    'button': ('Consolas', 16, 'bold')
}
```

### config.json
```json
{
  "app": {
    "name": "KeyPlayer Manager",
    "version": "1.0.0",
    "debug": false
  },
  "ui": {
    "theme": "light",
    "language": "es",
    "animations": true
  },
  "database": {
    "type": "json",
    "path": "./data"
  }
}
```

## Migración desde Configuración Actual

### Identificación
- Constantes hardcodeadas en el código
- Configuraciones dispersas en diferentes archivos
- Valores que podrían ser configurables

### Extracción
- Mover constantes a archivos de configuración
- Crear clases de configuración
- Implementar carga dinámica

### Refactorización
- Actualizar código para usar configuración centralizada
- Mantener compatibilidad durante la transición
- Documentar cambios

## Seguridad

### Configuraciones Sensibles
- No incluir en control de versiones
- Usar variables de entorno
- Encriptar cuando sea necesario
- Validar en tiempo de ejecución

### Validación
- Verificar tipos de datos
- Validar rangos de valores
- Verificar dependencias
- Proporcionar mensajes de error claros

## Documentación

Cuando se implemente la configuración, esta documentación incluirá:
- Guía de configuración por módulo
- Ejemplos de configuración
- Guía de troubleshooting
- Referencia completa de parámetros 