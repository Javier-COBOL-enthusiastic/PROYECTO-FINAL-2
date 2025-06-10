from tkinter import *
import os
from ui.elements import RoundedButton
from ui.views.welcome import WelcomeView
from ui.views.torneo import TorneoView
from ui.views.equipo import EquipoView
from ui.views.jugadores import JugadoresView

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800
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
        self.sidebar = Frame(self.root, bg=SIDEBAR_COLOR, width=250)
        self.sidebar.pack(side="left", fill="y")
        logo_path = os.path.join("assets", "images", "logo_side_bar.png")
        logo_img = PhotoImage(file=logo_path)
        logo_label = Label(self.sidebar, image=logo_img, bg=SIDEBAR_COLOR)
        logo_label.image = logo_img
        logo_label.pack(pady=(40, 40))
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
                width=160,
                height=40,
                radius=18,
                bg=btn_bg,
                fg=btn_fg,
                font=(FONT_FAMILY, 16, "bold"),
                hover_bg="#e5eaff" if is_active else "#688CCA",
                command=cmd,
            )
            btn.pack(pady=8)

    def show_view(self, view_name):
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
            TorneoView(main_frame)
        elif view_name == "equipo":
            EquipoView(main_frame)
        elif view_name == "jugadores":
            JugadoresView(main_frame)

    def run(self):
        self.root.mainloop()
