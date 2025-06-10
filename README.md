# KeyPlayer Manager

## Instalación

1. Crea un entorno virtual (opcional pero recomendado):
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Configura la base de datos usando el script `archivo_base_datos.sql`.

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

Desde la carpeta `src`:
```bash
python main.py
```

## Dependencias
- Python 3.x
- mysql-connector-python
- tk
