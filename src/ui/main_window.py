"""
Ventana principal de la aplicación KeyPlayer Manager
Este módulo contiene la clase MainWindow que gestiona la interfaz principal
de la aplicación, incluyendo la barra lateral y la navegación entre vistas.
"""

from tkinter import *
import os
from ui.elements import RoundedButton, AlertDialog, ConfirmDialog
from ui.views.welcome import WelcomeView
from ui.views.torneos import TorneoFormView, TorneoView, TorneoEdit, TorneoFormViewNoEdit
from ui.views.equipo import EquipoView
from ui.views.jugadores import JugadoresView, JugadorFormView, JugadorFormViewNoEdit
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "mocks"))
from ui.mocks import get_jugadores, create_jugador, update_jugador, delete_jugador, get_equipos, get_torneos, update_torneo, delete_torneo

# Constantes de configuración de la ventana
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 720
BG_COLOR = "#EDEDED"
SIDEBAR_COLOR = "#9FACE8"
FONT_FAMILY = "Consolas"


class MainWindow:
    """
    Clase principal que gestiona la ventana de la aplicación
    Se encarga de la navegación entre diferentes vistas y la gestión
    de la interfaz de usuario principal.
    """
    
    def __init__(self):
        """
        Constructor de la ventana principal
        Inicializa la ventana de Tkinter y configura sus propiedades básicas
        """
        # Crear la ventana principal
        self.root = Tk()
        self.root.title("KeyPlayer Manager")
        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+0+0")
        self.root.resizable(False, False)
        self.root.configure(bg=BG_COLOR)
        
        # Variables de estado
        self.current_view = None
        self.sidebar = None
        
        # Mostrar la vista de bienvenida por defecto
        self.show_view("welcome")

    def clear_main(self):
        """
        Limpia todos los widgets de la ventana principal
        Se usa antes de cambiar de vista
        """
        for widget in self.root.winfo_children():
            widget.destroy()

    def show_sidebar(self, active):
        """
        Crea y muestra la barra lateral de navegación
        
        Args:
            active (str): Nombre de la vista activa para resaltar el botón correspondiente
        """
        # Crear el frame de la barra lateral
        self.sidebar = Frame(
            self.root,
            bg=SIDEBAR_COLOR,
        )
        self.sidebar.pack(side="left", fill="y")
        
        # Cargar y mostrar el logo
        logo_path = os.path.join("assets", "images", "logo_side_bar.png")
        logo_img = PhotoImage(file=logo_path)
        logo_label = Label(self.sidebar, image=logo_img, bg=SIDEBAR_COLOR)
        logo_label.image = logo_img
        logo_label.pack(pady=(40, 20))
        
        # Definir los elementos del menú
        menu_items = [
            ("Inicio", lambda: self.show_view("welcome")),
            ("Torneo", lambda: self.show_view("torneo")),
            ("Equipo", lambda: self.show_view("equipo")),
            ("Jugadores", lambda: self.show_view("jugadores")),
        ]
        
        # Crear los botones del menú
        for name, cmd in menu_items:
            is_active = name.lower() == active
            btn_bg = "white" if is_active else SIDEBAR_COLOR
            btn_fg = SIDEBAR_COLOR if is_active else "white"
            btn = RoundedButton(
                self.sidebar,
                name,
                width=200,
                height=60,
                radius=18,
                bg=btn_bg,
                fg=btn_fg,
                font=(FONT_FAMILY, 16, "bold"),
                hover_bg="#e5eaff" if is_active else "#688CCA",
                command=cmd,
            )
            btn.pack(pady=8)

    def show_alert(self, parent, message, success=True, next_view=None):
        """
        Muestra un diálogo de alerta al usuario
        
        Args:
            parent: Widget padre para el diálogo
            message (str): Mensaje a mostrar
            success (bool): Si es True muestra alerta de éxito, si es False muestra error
            next_view (str): Vista a mostrar después de cerrar el diálogo
        """
        def go_next():
            if next_view:
                self.show_view(next_view)

        AlertDialog(parent, message, success=success, on_close=go_next)

    def show_view(self, view_name, torneo_id=None,jugador_id=None):
        """
        Cambia la vista actual de la aplicación
        
        Args:
            view_name (str): Nombre de la vista a mostrar
            torneo_id (int): ID del torneo (para vistas específicas de torneo)
            jugador_id (int): ID del jugador (para vistas específicas de jugador)
        """
        # Limpiar la ventana principal
        self.clear_main()
        
        # Mostrar barra lateral si no es la vista de bienvenida
        if view_name != "welcome":
            self.show_sidebar(view_name)
            main_frame = Frame(self.root, bg=BG_COLOR)
            main_frame.pack(side="left", fill="both", expand=True)
        else:
            main_frame = self.root
            
        # Mostrar la vista correspondiente según el nombre
        if view_name == "welcome":
            WelcomeView(main_frame, self)
        elif view_name == "torneo":
            # Función para manejar la eliminación de torneos
            def on_delete_torneo(torneo_id):
                def do_delete():
                    delete_torneo(torneo_id)
                    self.show_view("torneo")  # Recargar la vista

                ConfirmDialog(
                    self.root,
                    "¿Estás seguro que deseas eliminar este torneo?",
                    on_confirm=do_delete,
                    on_cancel=None,
                )
                    
            # Mostrar vista de torneos con sus callbacks
            TorneoView(main_frame, 
                      on_crear_torneo=lambda : self.show_view("torneo_form"), 
                      on_eliminar_torneo=lambda torneo_id : on_delete_torneo(torneo_id), 
                      on_editar_torneo=lambda torneo_id : self.show_view("torneo_edit", torneo_id=torneo_id), 
                      on_ver_torneo=lambda torneo_id : self.show_view("torneo_view", torneo_id))            
        elif view_name == "torneo_form":            
            TorneoFormView(main_frame, get_jugadores(), get_equipos(), lambda : self.show_view("torneo"))   
        elif view_name == "torneo_view":
            # Mostrar vista de torneo específico (solo lectura)
            torneos = get_torneos()
            if torneo_id is None:
                self.show_view("torneo")
            
            torneo = next((j for j in torneos if j["id"] == torneo_id), None)   
            TorneoFormViewNoEdit(main_frame, torneo)
        elif view_name == "torneo_edit":
            # Mostrar vista de edición de torneo
            torneos = get_torneos()
            if torneo_id is None:
                self.show_view("torneo")
            
            torneo = next((j for j in torneos if j["id"] == torneo_id), None)          
            def on_save_torneo(torneo):
                update_torneo(torneo)
                self.show_alert(self.root, "Torneo actualizado.")
                self.show_view("torneo")                        
            TorneoEdit(main_frame, torneo, on_save=on_save_torneo)
        elif view_name == "equipo":
            EquipoView(main_frame)        
        elif view_name == "jugadores":
            jugadores = get_jugadores()            
            # Función para manejar la eliminación de jugadores
            def on_eliminar_jugador(jugador_id):
                def do_delete():
                    delete_jugador(jugador_id)
                    self.show_view("jugadores")  # Recargar la vista

                ConfirmDialog(
                    self.root,
                    "¿Estás seguro que deseas eliminar este jugador?",
                    on_confirm=do_delete,
                    on_cancel=None,
                )

            # Mostrar vista de jugadores con sus callbacks
            JugadoresView(
                main_frame,
                on_crear_jugador=lambda: self.show_view("jugador_form"),
                on_editar_jugador=lambda jugador_id: self.show_view("jugador_form", jugador_id=jugador_id),
                on_eliminar_jugador=on_eliminar_jugador,
                on_ver_jugador=lambda jugador_id: self.show_view("jugador_form_no_edit", jugador_id=jugador_id),
                jugadores=jugadores,
            )
        elif view_name == "jugador_form_no_edit":
            # Mostrar formulario de jugador en modo solo lectura
            jugadores = get_jugadores()
            jugador = None 
            if jugador_id is None:
                self.show_view("jugadores")
                
            jugador = next((j for j in jugadores if j["id"] == jugador_id), None)  
            JugadorFormViewNoEdit(main_frame, jugador)      

        elif view_name == "jugador_form":
            jugadores = get_jugadores()
            jugador = None 
            
            if jugador_id is not None:
                jugador = next((j for j in jugadores if j["id"] == jugador_id), None)

            # Función para crear un nuevo jugador
            def crear_jugador(nombre, puntos):
                nombre = nombre.strip()
                if not nombre or nombre == "" or nombre == "Nombre del jugador...":
                    self.show_alert(self.root, "El nombre no puede estar vacío", success=False)
                    return
                if len(nombre) > 29:
                    AlertDialog(
                        self.root, "El nombre del jugador es muy largo.", success=False
                    )
                    return
                nombre_lower = nombre.lower()                
                for j in jugadores:
                    if j["nombre"].lower() == nombre_lower:
                        self.show_alert(self.root, "Ya existe un jugador con ese nombre", success=False)
                        return
                try:
                    create_jugador(nombre, puntos)
                    self.show_alert(self.root, "Dato agregado exitosamente", success=True, next_view="jugadores")
                except Exception as e:
                    self.show_alert(self.root, "Error al crear jugador", success=False)

            # Función para actualizar un jugador existente
            def actualizar_jugador(nombre, puntos, id):
                nombre = nombre.strip()
                if not nombre or nombre == "" or nombre == "Nombre del jugador...":
                    self.show_alert(self.root, "El nombre no puede estar vacío", success=False)
                    return
                if len(nombre) > 28:
                    AlertDialog(
                        self.root, "El nombre del jugador es muy largo.", success=False
                    )
                    return
                nombre_lower = nombre.lower()
                for j in jugadores:
                    if j["id"] != id and j["nombre"].lower() == nombre_lower:
                        self.show_alert(self.root, "Ya existe un jugador con ese nombre", success=False)
                        return
                try:
                    update_jugador(id, nombre, puntos)
                    self.show_alert(self.root, "Jugador actualizado exitosamente", success=True, next_view="jugadores")
                except Exception as e:
                    self.show_alert(self.root, "Error al actualizar jugador", success=False)

            # Función general para guardar (crear o actualizar)
            def on_save(nombre, puntos, id, is_editing):
                if is_editing:
                    actualizar_jugador(nombre, puntos, id)
                else:
                    crear_jugador(nombre, puntos)

            JugadorFormView(
                main_frame,
                on_save=lambda nombre, puntos, id: on_save(nombre, puntos, id, jugador_id is not None),
                initial_name=jugador["nombre"] if jugador else "",
                initial_points=jugador["puntos"] if jugador else 0,
                jugador_id=jugador_id,
            )


    def run(self):
        """
        Inicia el bucle principal de la aplicación
        """
        self.root.mainloop()
