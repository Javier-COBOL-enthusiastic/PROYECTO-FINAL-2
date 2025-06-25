# Carpeta models/

Esta carpeta contiene los modelos de datos de la aplicación KeyPlayer Manager.

## Contenido

### Archivos

#### **torneo.py**
Contiene la lógica de negocio para la entidad Torneo:

**Clases de Excepción:**
- `NombreInvalido`: Se lanza cuando el nombre del torneo está vacío o es inválido
- `FormatoFechaInvalido`: Se lanza cuando el formato de fecha no es válido (dd/mm/yyyy)
- `FechaInvalida`: Se lanza cuando las fechas no son lógicas (fecha fin antes que inicio)
- `JuegoInvalido`: Se lanza cuando no se selecciona un juego para el torneo

**Clase Principal:**
- `Torneo`: Clase que representa un torneo en el sistema
  - Constructor: Valida todos los datos del torneo antes de su creación
  - Método `__valid_format__`: Valida el formato de fecha y normaliza el formato

## Responsabilidades

Los modelos en esta carpeta se encargan de:

1. **Validación de Datos**: Verificar que los datos ingresados cumplan con las reglas de negocio
2. **Lógica de Negocio**: Implementar las reglas específicas del dominio
3. **Transformación de Datos**: Normalizar y limpiar los datos antes de su procesamiento
4. **Manejo de Errores**: Definir excepciones específicas para diferentes tipos de errores

## Uso

Los modelos se utilizan principalmente en las vistas para validar los datos antes de enviarlos a la capa de persistencia. Por ejemplo:

```python
from models.torneo import Torneo, NombreInvalido

try:
    torneo = Torneo(datos_formulario)
    # Si llega aquí, los datos son válidos
except NombreInvalido:
    # Manejar error de nombre inválido
```

## Extensibilidad

Esta carpeta está preparada para agregar más modelos en el futuro:
- `jugador.py`: Modelo para la entidad Jugador
- `equipo.py`: Modelo para la entidad Equipo
- `partida.py`: Modelo para la entidad Partida (futuro) 