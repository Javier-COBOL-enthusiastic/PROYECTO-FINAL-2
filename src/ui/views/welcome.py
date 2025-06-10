from tkinter import *
from ui.elements import RoundedButton


class WelcomeView:
    def __init__(self, parent, main_window):
        frame = Frame(parent, bg="#EDEDED")
        frame.place(relx=0, rely=0, relwidth=1, relheight=1)
        # Nuevo content_frame centrado
        content_frame = Frame(frame, bg="#EDEDED")
        content_frame.pack(expand=True)
        logo_path = "assets/images/logo_azul.png"
        logo_img = PhotoImage(file=logo_path)
        logo_label = Label(content_frame, image=logo_img, bg="#EDEDED")
        logo_label.image = logo_img
        logo_label.pack(pady=(60, 20))
        title = Label(
            content_frame,
            text="Bienvenido a K.E.Y. player manager",
            font=("Consolas", 28, "bold"),
            bg="#EDEDED",
            fg="#444",
        )
        title.pack(pady=(0, 16))
        subtitle = Label(
            content_frame,
            text="¿Qué deseas hacer?",
            font=("Consolas", 12),
            bg="#EDEDED",
            fg="#888",
        )
        subtitle.pack(pady=(0, 40))
        btn_frame = Frame(content_frame, bg="#EDEDED")
        btn_frame.pack()
        RoundedButton(
            btn_frame,
            "Torneo",
            font=("Consolas", 16, "bold"),
            command=lambda: main_window.show_view("torneo"),
        ).pack(side="left", padx=28)
        RoundedButton(
            btn_frame,
            "Equipos",
            font=("Consolas", 16, "bold"),
            command=lambda: main_window.show_view("equipo"),
        ).pack(side="left", padx=28)
        RoundedButton(
            btn_frame,
            "Jugadores",
            font=("Consolas", 16, "bold"),
            command=lambda: main_window.show_view("jugadores"),
        ).pack(side="left", padx=28)
