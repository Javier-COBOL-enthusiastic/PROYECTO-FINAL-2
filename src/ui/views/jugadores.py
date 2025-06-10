from tkinter import *


class JugadoresView:
    def __init__(self, parent):
        frame = Frame(parent, bg="#EDEDED")
        frame.place(relx=0, rely=0, relwidth=1, relheight=1)
        Label(
            frame,
            text="Página de Jugadores",
            font=("Consolas", 24, "bold"),
            bg="#EDEDED",
        ).pack(pady=40)
