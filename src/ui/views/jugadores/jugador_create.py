from tkinter import *
from ui.elements import RoundedButton, StyledEntry


class JugadorFormView:
    def __init__(self, parent, on_save=None, initial_name="", jugador_id=None):
        frame = Frame(parent, bg="#EDEDED")
        frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        # Encabezado grande con fondo gris claro
        header_bg = Frame(frame, bg="#F6F6F6")
        header_bg.pack(fill="x", padx=0, pady=(0, 0))
        titulo = "Editar jugador" if jugador_id is not None else "Crear jugador"
        Label(
            header_bg,
            text=titulo,
            font=("Consolas", 28, "bold"),
            bg="#F6F6F6",
            fg="#222",
            anchor="w",
        ).pack(fill="x", padx=60, pady=(36, 18))

        # Más espacio entre el título y la tarjeta
        Frame(frame, height=18, bg="#EDEDED").pack()

        # Tarjeta de formulario alineada a la izquierda
        card_w, card_h = 540, 220
        card = Frame(frame, bg="white", width=card_w, height=card_h)
        card.place(x=60, y=140)  # alineado a la izquierda
        card.pack_propagate(False)

        Label(
            card,
            text="Nombre del jugador",
            font=("Consolas", 16, "bold"),
            bg="white",
            fg="#1A1832",
            anchor="w",
        ).pack(fill="x", padx=20, pady=(30, 6))

        self.name_var = StringVar(value=initial_name)
        StyledEntry(
            card,
            textvariable=self.name_var,
            font=("Consolas", 13),
            placeholder="Nombre del jugador...",
            border_radius=16,
        ).pack(fill="x", padx=20, pady=(0, 32), anchor="w")

        RoundedButton(
            card,
            text="Guardar",
            width=180,
            height=44,
            radius=18,
            font=("Consolas", 13, "bold"),
            command=lambda: (
                on_save(self.name_var.get(), jugador_id) if on_save else None
            ),
        ).pack(pady=(0, 0), padx=20, anchor="w")
