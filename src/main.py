"""
Archivo principal de la aplicación KeyPlayer Manager
Este archivo es el punto de entrada de la aplicación y se encarga de inicializar
la ventana principal y ejecutar la aplicación.
"""

from ui.main_window import MainWindow

if __name__ == "__main__":
    # Crear la instancia de la ventana principal
    app = MainWindow()
    # Ejecutar la aplicación
    app.run()
    

