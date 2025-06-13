from tkinter import *
from ui.elements import TableView, TableActionButton, RoundedButton


class JugadoresView:
    def __init__(
        self,
        parent,
        on_crear_jugador=None,
        on_editar_jugador=None,
        on_eliminar_jugador=None,
        jugadores=None,
    ):
        frame = Frame(parent, bg="#EDEDED")
        frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        # Encabezado grande con fondo gris claro
        header_bg = Frame(frame, bg="#F6F6F6")
        header_bg.pack(fill="x", padx=0, pady=(0, 0))
        Label(
            header_bg,
            text="Jugadores",
            font=("Consolas", 28, "bold"),
            bg="#F6F6F6",
            fg="#222",
            anchor="w",
        ).pack(fill="x", padx=60, pady=(36, 18))

        # Más espacio entre el título y la tarjeta
        Frame(frame, height=18, bg="#EDEDED").pack()

        # Tarjeta de tabla de jugadores con fondo redondeado
        table_card_w, table_card_h = 980, 380
        table_card_container = Frame(
            frame, bg="#EDEDED", width=table_card_w, height=table_card_h
        )
        table_card_container.pack(
            anchor="n", padx=40, pady=(0, 0), fill=None, expand=False
        )

        headers = ["ID", "Nombre", "Acciones", ""]
        data = [[j["id"], j["nombre"]] for j in (jugadores or [])]

        def info_button(row, parent, text):
            btn = RoundedButton(
                parent,
                text=text,
                width=160,
                height=36,
                radius=16,
                font=("Consolas", 11, "bold"),
                bg="#9FACE8",
                fg="white",
                hover_bg="#688CCA",
                command=lambda: print(f"Ver historial de {row[1]}"),
            )
            btn.pack()
            return btn

        def action_buttons(row, parent, text):
            btn_frame = Frame(parent, bg=parent["bg"])
            TableActionButton(
                btn_frame,
                icon_path="assets/images/delete.png",
                command=lambda: (
                    on_eliminar_jugador(row[0]) if on_eliminar_jugador else None
                ),
            ).pack(side="left", padx=(0, 8))
            TableActionButton(
                btn_frame,
                icon_path="assets/images/edit.png",
                command=lambda: (
                    on_editar_jugador(row[0]) if on_editar_jugador else None
                ),
            ).pack(side="left", padx=(0, 8))
            return btn_frame

        col_widths = [60, 400, 200, 200]

        table = TableView(
            table_card_container,
            headers,
            data,
            actions=[info_button, action_buttons],
            title="Lista de jugadores",
            count=len(data),
            button_text="Crear jugador",
            button_command=on_crear_jugador,
            card_w=table_card_w,
            card_h=table_card_h,
            col_widths=col_widths,
            action_text="Ver historial",
            anchor_cols="center",
        )
        table.pack(padx=0, pady=(10, 0), fill="both", expand=True)
