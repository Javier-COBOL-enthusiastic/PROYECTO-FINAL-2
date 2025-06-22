from tkinter import *
from ui.elements import TableView, MenuButton, TableActionButton
import os
from tkinter import PhotoImage
from ui.elements import RoundedButton


def draw_rounded_rect(canvas, x1, y1, x2, y2, r, fill, outline, width=1):
    # Arcos de las esquinas
    canvas.create_arc(
        x1,
        y1,
        x1 + 2 * r,
        y1 + 2 * r,
        start=90,
        extent=90,
        style="pieslice",
        fill=fill,
        outline=outline,
        width=width,
    )
    canvas.create_arc(
        x2 - 2 * r,
        y1,
        x2,
        y1 + 2 * r,
        start=0,
        extent=90,
        style="pieslice",
        fill=fill,
        outline=outline,
        width=width,
    )
    canvas.create_arc(
        x2 - 2 * r,
        y2 - 2 * r,
        x2,
        y2,
        start=270,
        extent=90,
        style="pieslice",
        fill=fill,
        outline=outline,
        width=width,
    )
    canvas.create_arc(
        x1,
        y2 - 2 * r,
        x1 + 2 * r,
        y2,
        start=180,
        extent=90,
        style="pieslice",
        fill=fill,
        outline=outline,
        width=width,
    )

    # Rectángulo central
    canvas.create_rectangle(
        x1 + r, y1, x2 - r, y2, fill=fill, outline=outline, width=width
    )
    # Rectángulos laterales
    canvas.create_rectangle(
        x1, y1 + r, x1 + r, y2 - r, fill=fill, outline=outline, width=width
    )
    canvas.create_rectangle(
        x2 - r, y1 + r, x2, y2 - r, fill=fill, outline=outline, width=width
    )


class HistorialCard:
    def __init__(self, parent, estados):
        hist_card_w, hist_card_h = 980, 250
        self.container = Frame(parent, bg="#EDEDED")
        self.container.pack(anchor="n", padx=40, pady=(0, 32), fill=None, expand=False)

        hist_canvas = Canvas(
            self.container,
            width=hist_card_w,
            height=hist_card_h,
            bg="#EDEDED",
            highlightthickness=0,
        )
        hist_canvas.pack()

        # Fondo blanco
        draw_rounded_rect(
            hist_canvas,
            0,
            0,
            hist_card_w,
            hist_card_h,
            18,
            fill="white",
            outline="#DDD",
            width=2,
        )

        # Frame principal encima del canvas
        hist_content = Frame(hist_canvas, bg="white")
        hist_canvas.create_window(
            0,
            0,
            anchor="nw",
            window=hist_content,
            width=hist_card_w,
            height=hist_card_h,
        )

        Label(
            hist_content,
            text="Historial",
            font=("Consolas", 16, "bold"),
            bg="white",
            fg="#222",
        ).pack(anchor="w", padx=32, pady=(32, 0))

        cards_frame = Frame(hist_content, bg="white")
        cards_frame.pack(pady=(24, 0))

        card_w, card_h = 210, 130
        sep = 48

        for i, (estado, num) in enumerate(estados):
            card_canvas = Canvas(
                cards_frame,
                width=card_w,
                height=card_h,
                bg="white",
                highlightthickness=0,
            )
            card_canvas.grid(row=0, column=i, padx=(0 if i == 0 else sep, 0))

            draw_rounded_rect(
                card_canvas,
                0,
                0,
                card_w,
                card_h,
                18,
                fill="#EDEDED",
                outline="#EDEDED",
                width=1,
            )

            card_canvas.create_text(
                card_w // 2,
                32,
                text=estado,
                font=("Consolas", 14, "bold"),
                fill="#888",
            )

            icon_path = os.path.join("assets", "images", "torneo_icon_historial.png")
            icon_img = PhotoImage(file=icon_path)
            card_canvas.create_image(card_w // 2 - 38, 85, image=icon_img)
            card_canvas.image = icon_img  # evitar que se borre
            card_canvas.create_text(
                card_w // 2 + 38,
                85,
                text=str(num),
                font=("Consolas", 26, "bold"),
                fill="#222",
            )


class TorneoView:
    def __init__(self, parent, on_crear_torneo=None, on_editar_torneo=None, on_eliminar_torneo=None, on_ver_torneo=None):        
        frame = Frame(parent, bg="#EDEDED")
        frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        # Encabezado grande con fondo gris claro
        header_bg = Frame(frame, bg="#F6F6F6")
        header_bg.pack(fill="x", padx=0, pady=(0, 0))
        Label(
            header_bg,
            text="Torneos",
            font=("Consolas", 28, "bold"),
            bg="#F6F6F6",
            fg="#222",
            anchor="w",
        ).pack(fill="x", padx=60, pady=(36, 18))

        # Más espacio entre el título y la tarjeta
        Frame(frame, height=18, bg="#EDEDED").pack()

        # Usar la nueva clase para el historial
        estados = [("Iniciado", 1), ("Pendiente", 3), ("Finalizado", 5)]
        self.historial = HistorialCard(frame, estados)

        # Tabla torneos
        table_card_w, table_card_h = 980, 350
        table_card_container = Frame(
            frame, bg="#EDEDED", width=table_card_w, height=table_card_h
        )
        table_card_container.pack(
            anchor="n", padx=40, pady=(0, 0), fill=None, expand=False
        )

        headers = ["ID", "Torneo", "Inicio", "Fin", "Estado", ""] 
        #@20220270 aca deberia ir la llamada a todos los torneos pq aca se hace la tabla
        data = [
            [f"{i:02}", f"Torneo {i}", "01/01/24", "05/01/24", "Pendiente"]
            for i in range(1, 10)
        ]

        def action_buttons(row, parent, text):
            btn_frame = Frame(parent, bg=parent["bg"])
            TableActionButton(
                btn_frame,
                icon_path="assets/images/edit.png",
                command=lambda: (
                    on_editar_torneo(row[0]) if on_editar_torneo else None
                )
            ).pack(side="left", padx=(0, 8))
            TableActionButton(
                btn_frame,
                icon_path="assets/images/delete.png",
                command=lambda: (
                    on_eliminar_torneo(row[0]) if on_eliminar_torneo else None
                )
            ).pack(side="left", padx=(0, 8))
            TableActionButton(
                btn_frame,
                icon_path="assets/images/eye.png",
                command=lambda: (
                    on_ver_torneo(row[0]) if on_ver_torneo else None
                )
            ).pack(side="left")
            return btn_frame

        col_widths = [60, 150, 160, 160, 180, 200]

        table = TableView(
            table_card_container,
            headers,
            data,
            actions=[action_buttons],
            title="Lista de torneos",
            count=len(data),
            button_text="Crear torneo",
            button_command=on_crear_torneo,
            col_widths=col_widths,
            action_text="Ver información",
            card_w=table_card_w,
            card_h=table_card_h,
        )
        table.pack(padx=0, pady=(10, 0), fill="both", expand=True)
