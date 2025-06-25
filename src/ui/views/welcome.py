"""
Vista de bienvenida de la aplicación KeyPlayer Manager
Esta vista se muestra al iniciar la aplicación y proporciona
navegación a las diferentes secciones del sistema.
"""

from tkinter import *
from ui.elements import RoundedButton


class WelcomeView:
    """
    Vista de bienvenida que muestra el logo y botones de navegación
    Es la primera pantalla que ve el usuario al abrir la aplicación
    """
    
    def __init__(self, parent, main_window):
        """
        Constructor de la vista de bienvenida
        
        Args:
            parent: Widget padre donde se mostrará la vista
            main_window: Instancia de la ventana principal para navegación
        """
        # Crear el frame principal
        frame = Frame(parent, bg="#EDEDED")
        frame.place(relx=0, rely=0, relwidth=1, relheight=1)
        
        # Frame de contenido centrado
        content_frame = Frame(frame, bg="#EDEDED")
        content_frame.pack(expand=True)
        
        # Cargar y mostrar el logo principal
        logo_path = "assets/images/logo_azul.png"
        logo_img = PhotoImage(file=logo_path)
        logo_label = Label(content_frame, image=logo_img, bg="#EDEDED")
        logo_label.image = logo_img
        logo_label.pack(pady=(60, 20))
        
        # Título principal
        title = Label(
            content_frame,
            text="Bienvenido a K.E.Y. player manager",
            font=("Consolas", 28, "bold"),
            bg="#EDEDED",
            fg="#444",
        )
        title.pack(pady=(0, 16))
        
        # Subtítulo
        subtitle = Label(
            content_frame,
            text="¿Qué deseas hacer?",
            font=("Consolas", 12),
            bg="#EDEDED",
            fg="#888",
        )
        subtitle.pack(pady=(0, 40))
        
        # Frame para los botones de navegación
        btn_frame = Frame(content_frame, bg="#EDEDED")
        btn_frame.pack()
        
        # Botón para ir a la sección de torneos
        RoundedButton(
            btn_frame,
            "Torneo",
            font=("Consolas", 16, "bold"),
            command=lambda: main_window.show_view("torneo"),
        ).pack(side="left", padx=28)
        
        # Botón para ir a la sección de equipos
        RoundedButton(
            btn_frame,
            "Equipos",
            font=("Consolas", 16, "bold"),
            command=lambda: main_window.show_view("equipo"),
        ).pack(side="left", padx=28)
        
        # Botón para ir a la sección de jugadores
        RoundedButton(
            btn_frame,
            "Jugadores",
            font=("Consolas", 16, "bold"),
            command=lambda: main_window.show_view("jugadores"),
        ).pack(side="left", padx=28)
