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


WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 720
BG_COLOR = "#EDEDED"
SIDEBAR_COLOR = "#9FACE8"
FONT_FAMILY = "Consolas"


class MainWindow:
    def __init__(self):
        self.root = Tk()
        self.root.title("KeyPlayer Manager")
        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+0+0")
        self.root.resizable(False, False)
        self.root.configure(bg=BG_COLOR)
        self.current_view = None
        self.sidebar = None
        self.show_view("welcome")

    def clear_main(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def show_sidebar(self, active):
        self.sidebar = Frame(
            self.root,
            bg=SIDEBAR_COLOR,
        )
        self.sidebar.pack(side="left", fill="y")
        logo_path = os.path.join("assets", "images", "logo_side_bar.png")
        logo_img = PhotoImage(file=logo_path)
        logo_label = Label(self.sidebar, image=logo_img, bg=SIDEBAR_COLOR)
        logo_label.image = logo_img
        logo_label.pack(pady=(40, 20))
        menu_items = [
            ("Inicio", lambda: self.show_view("welcome")),
            ("Torneo", lambda: self.show_view("torneo")),
            ("Equipo", lambda: self.show_view("equipo")),
            ("Jugadores", lambda: self.show_view("jugadores")),
        ]
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
        def go_next():
            if next_view:
                self.show_view(next_view)

        AlertDialog(parent, message, success=success, on_close=go_next)

    def show_view(self, view_name, torneo_id=None,jugador_id=None):
        self.clear_main()
        if view_name != "welcome":
            self.show_sidebar(view_name)
            main_frame = Frame(self.root, bg=BG_COLOR)
            main_frame.pack(side="left", fill="both", expand=True)
        else:
            main_frame = self.root
        if view_name == "welcome":
            WelcomeView(main_frame, self)
        elif view_name == "torneo":
            def on_delete_torneo(torneo_id):
                def do_delete():
                    delete_torneo(torneo_id)
                    self.show_view(
                        "torneo"
                    )  # Solo recarga la vista, no muestra dialog extra

                ConfirmDialog(
                    self.root,
                    "¿Estás seguro que deseas eliminar este torneo?",
                    on_confirm=do_delete,
                    on_cancel=None,
                )
                    

                
            TorneoView(main_frame, on_crear_torneo=lambda : self.show_view("torneo_form"), on_eliminar_torneo=lambda torneo_id : on_delete_torneo(torneo_id), on_editar_torneo=lambda torneo_id : self.show_view("torneo_edit", torneo_id=torneo_id), on_ver_torneo=lambda torneo_id : self.show_view("torneo_view", torneo_id))            
        elif view_name == "torneo_form":            
            TorneoFormView(main_frame, get_jugadores(), get_equipos(), lambda : self.show_view("torneo"))   
        elif view_name == "torneo_view":
            torneos = get_torneos()
            if torneo_id is None:
                self.show_view("torneo")
            
            torneo = next((j for j in torneos if j["id"] == torneo_id), None)   
            TorneoFormViewNoEdit(main_frame, torneo)
        elif view_name == "torneo_edit":
            torneos = get_torneos()
            if torneo_id is None:
                self.show_view("torneo")
            
            torneo = next((j for j in torneos if j["id"] == torneo_id), None)          
            def on_save_torneo(torneo):
                update_torneo(torneo)
                self.show_alert(
                    self.root, "Torneo actualizado."
                )
                self.show_view("torneo")                        
            TorneoEdit(main_frame, torneo, on_save=on_save_torneo)
        elif view_name == "equipo":
            EquipoView(main_frame)        
        elif view_name == "jugadores":
            jugadores = get_jugadores()            
            def on_eliminar_jugador(jugador_id):
                def do_delete():
                    delete_jugador(jugador_id)
                    self.show_view(
                        "jugadores"
                    )  # Solo recarga la vista, no muestra dialog extra

                ConfirmDialog(
                    self.root,
                    "¿Estás seguro que deseas eliminar este jugador?",
                    on_confirm=do_delete,
                    on_cancel=None,
                )

            JugadoresView(
                main_frame,
                on_crear_jugador=lambda: self.show_view("jugador_form"),
                on_editar_jugador=lambda jugador_id: self.show_view(
                    "jugador_form", jugador_id=jugador_id
                ),
                on_eliminar_jugador=on_eliminar_jugador,
                on_ver_jugador=lambda jugador_id: self.show_view(
                    "jugador_form_no_edit", jugador_id=jugador_id
                ),
                jugadores=jugadores,
            )
        elif view_name == "jugador_form_no_edit":
            jugadores = get_jugadores()
            jugador = None 
            if jugador_id is None: #quien muesta errores en 2025???? smh
                self.show_view("jugadores")
                
            jugador = next((j for j in jugadores if j["id"] == jugador_id), None)  
            JugadorFormViewNoEdit(main_frame, jugador)      

        elif view_name == "jugador_form":
            jugadores = get_jugadores()
            jugador = None 
            
            if jugador_id is not None:
                jugador = next((j for j in jugadores if j["id"] == jugador_id), None)

            def crear_jugador(nombre, puntos):
                nombre = nombre.strip()
                if not nombre or nombre == "" or nombre == "Nombre del jugador...":
                    self.show_alert(
                        self.root, "El nombre no puede estar vacío", success=False
                    )
                    return
                nombre_lower = nombre.lower()
                for j in jugadores:
                    if j["nombre"].lower() == nombre_lower:
                        self.show_alert(
                            self.root,
                            "Ya existe un jugador con ese nombre",
                            success=False,
                        )
                        return
                try:
                    create_jugador(nombre, puntos)
                    self.show_alert(
                        self.root,
                        "Dato agregado exitosamente",
                        success=True,
                        next_view="jugadores",
                    )
                except Exception as e:
                    self.show_alert(
                        self.root,
                        "Ha ocurrido un error",
                        success=False,
                        next_view="jugadores",
                    )

            def actualizar_jugador(nombre, puntos, id):
                nombre = nombre.strip()
                if not nombre:
                    self.show_alert(
                        self.root, "El nombre no puede estar vacío", success=False
                    )
                    return
                nombre_lower = nombre.lower()
                for j in jugadores:
                    if j["nombre"].lower() == nombre_lower and j["id"] != id:
                        self.show_alert(
                            self.root,
                            "Ya existe un jugador con ese nombre",
                            success=False,
                        )
                        return
                try:
                    update_jugador(id, nombre, puntos)
                    self.show_alert(
                        self.root,
                        "Dato actualizado exitosamente",
                        success=True,
                        next_view="jugadores",
                    )
                except Exception as e:
                    self.show_alert(
                        self.root,
                        "Ha ocurrido un error",
                        success=False,
                        next_view="jugadores",
                    )

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
        self.root.mainloop()
