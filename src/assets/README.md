# Carpeta assets/

Esta carpeta contiene todos los recursos visuales y multimedia de la aplicación KeyPlayer Manager.

## Contenido

### Carpetas

#### **/images/**
Contiene todas las imágenes utilizadas en la interfaz de usuario:

**Logos:**
- `logo_azul.png`: Logo principal de la aplicación (versión azul)
- `logo_blanco.png`: Logo principal de la aplicación (versión blanca)
- `logo_azul_mini.png`: Logo pequeño de la aplicación (versión azul)
- `logo_blanco_mini.png`: Logo pequeño de la aplicación (versión blanca)
- `logo_side_bar.png`: Logo específico para la barra lateral

**Iconos de Acción:**
- `edit.png`: Icono para acciones de editar
- `delete.png`: Icono para acciones de eliminar
- `eye.png`: Icono para acciones de ver/visualizar

**Iconos de Estado:**
- `success.png`: Icono para mensajes de éxito
- `error.png`: Icono para mensajes de error

**Botones:**
- `boton_cerrar.png`: Botón de cerrar (versión normal)
- `boton_cerrar_mini.png`: Botón de cerrar (versión pequeña)

**Iconos Específicos:**
- `torneo_icon_historial.png`: Icono para historial de torneos

## Características de las Imágenes

### Formatos
- **PNG**: Formato principal para transparencias y calidad
- **Tamaños optimizados**: Diferentes versiones según el uso
- **Transparencia**: Soporte para fondos transparentes

### Organización
- **Nomenclatura clara**: Nombres descriptivos en español
- **Versiones múltiples**: Diferentes tamaños para diferentes usos
- **Categorización**: Agrupadas por función

## Uso en la Aplicación

### Logos
- **logo_azul.png**: Pantalla de bienvenida y elementos principales
- **logo_blanco.png**: Sobre fondos oscuros
- **logo_side_bar.png**: Barra lateral de navegación

### Iconos de Acción
- **edit.png**: Botones de editar en tablas y formularios
- **delete.png**: Botones de eliminar con confirmación
- **eye.png**: Botones de visualizar detalles

### Iconos de Estado
- **success.png**: Diálogos de éxito y confirmación
- **error.png**: Diálogos de error y advertencia

### Botones
- **boton_cerrar.png**: Cerrar ventanas y diálogos
- **boton_cerrar_mini.png**: Versión compacta para espacios reducidos

## Carga de Imágenes

### En el Código
```python
# Ejemplo de carga de imagen
logo_path = "assets/images/logo_azul.png"
logo_img = PhotoImage(file=logo_path)
```

### Rutas Relativas
- Las imágenes se cargan usando rutas relativas desde la carpeta `src/`
- La estructura de carpetas se mantiene consistente
- Las rutas se construyen dinámicamente según sea necesario

## Optimización

### Tamaños
- **Logos grandes**: Para pantallas principales (200-400px)
- **Logos medianos**: Para elementos de navegación (100-200px)
- **Iconos**: Para acciones y botones (16-64px)
- **Miniaturas**: Para espacios reducidos (16-32px)

### Calidad
- **PNG sin pérdida**: Para logos e iconos importantes
- **Compresión optimizada**: Balance entre calidad y tamaño
- **Transparencia**: Cuando es necesario para el diseño

## Mantenimiento

### Agregar Nuevas Imágenes
1. Colocar en la carpeta `/images/`
2. Usar nomenclatura consistente
3. Optimizar tamaño y formato
4. Actualizar documentación si es necesario

### Actualizar Imágenes Existentes
1. Mantener el mismo nombre de archivo
2. Preservar dimensiones si es posible
3. Probar en diferentes contextos de la aplicación
4. Verificar que no se rompan las referencias

### Backup
- Las imágenes son parte del control de versiones
- Cambios importantes deben ser documentados
- Versiones anteriores se pueden recuperar desde el historial

## Consideraciones de Diseño

### Consistencia Visual
- Paleta de colores coherente
- Estilo de iconografía uniforme
- Proporciones consistentes

### Accesibilidad
- Contraste adecuado en todas las versiones
- Tamaños mínimos para usabilidad
- Textos alternativos cuando sea necesario

### Responsividad
- Diferentes tamaños para diferentes resoluciones
- Escalado apropiado en diferentes contextos
- Optimización para pantallas pequeñas 