# KeyPlayer Manager

## Instalación en Windows

1. **Requisitos Previos**:
   - Python 3.x instalado (descargar desde [python.org](https://www.python.org/downloads/))
   - MySQL Server instalado (descargar desde [mysql.com](https://dev.mysql.com/downloads/mysql/))
   - MySQL Workbench (opcional, pero recomendado para gestionar la base de datos)

2. **Configuración de la Base de Datos**:
   - Abre MySQL Workbench o la línea de comandos de MySQL
   - Ejecuta el script `archivo_base_datos.sql` para crear la base de datos y las tablas
   - Por defecto, el sistema usa las siguientes credenciales:
     - Usuario: root
     - Contraseña: (vacía)
     - Puerto: 3306
   - Si tus credenciales son diferentes, modifica el archivo `src/config/conexion_db.py`

3. **Configuración del Entorno Virtual**:
   ```powershell
   # Crear el entorno virtual
   python -m venv venv

   # Activar el entorno virtual
   .\venv\Scripts\activate
   ```

4. **Instalar Dependencias**:
   ```powershell
   pip install -r requirements.txt
   ```

## Estructura del Proyecto

```
/src
    /assets
        /images
    /config
        conexion_db.py
    /models
        torneo.py
    /controllers
        torneos_gestion.py
        equipos_gestion.py
    /ui
        main_window.py
        Elements.py
        /views
    main.py
    archivo_base_datos.sql
    LICENSE
    README.md
    requirements.txt
```

## Ejecución

1. Asegúrate de que el entorno virtual está activado:
   ```powershell
   .\venv\Scripts\activate
   ```

2. Navega a la carpeta `src`:
   ```powershell
   cd src
   ```

3. Ejecuta la aplicación:
   ```powershell
   python main.py
   ```

## Solución de Problemas

1. **Error de conexión a MySQL**:
   - Verifica que el servicio de MySQL esté corriendo
   - Comprueba las credenciales en `src/config/conexion_db.py`
   - Asegúrate de que el puerto 3306 está disponible

2. **Error al instalar dependencias**:
   - Actualiza pip: `python -m pip install --upgrade pip`
   - Intenta instalar las dependencias una por una

3. **Error al activar el entorno virtual**:
   - Si recibes un error de ejecución de scripts, ejecuta en PowerShell como administrador:
   ```powershell
   Set-ExecutionPolicy RemoteSigned
   ```

## Dependencias
- Python 3.x
- mysql-connector-python
- tk (incluido en la instalación de Python)
