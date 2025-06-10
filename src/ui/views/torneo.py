from tkinter import *
from ui.elements import TableView, MenuButton, TableActionButton
import os
from tkinter import PhotoImage
from ui.elements import RoundedButton


def draw_rounded_rect(canvas, x1, y1, x2, y2, r, fill, outline, width=1):

    points = [
        (x1 + r, y1),
        (x2 - r, y1),
        (x2, y1),
        (x2, y1 + r),
        (x2, y2 - r),
        (x2, y2),
        (x2 - r, y2),
        (x1 + r, y2),
        (x1, y2),
        (x1, y2 - r),
        (x1, y1 + r),
        (x1, y1),
    ]
    return canvas.create_polygon(
        points, smooth=True, fill=fill, outline=outline, width=width
    )


class TorneoView:
    def __init__(self, parent):
        frame = Frame(parent, bg="#EDEDED")
        frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        Label(
            frame,
            text="Torneos",
            font=("Consolas", 28, "bold"),
            bg="#EDEDED",
            fg="#222",
        ).pack(anchor="w", padx=60, pady=(36, 18))

        hist_card_container = Frame(frame, bg="#EDEDED")
        hist_card_container.pack(
            anchor="n", padx=40, pady=(0, 32), fill=None, expand=False
        )
        hist_canvas = Canvas(
            hist_card_container,
            width=980,
            height=250,
            bg="#EDEDED",
            highlightthickness=0,
        )
        hist_canvas.pack()
        r = 18
        w, h = 980, 250
        draw_rounded_rect(hist_canvas, 0, 0, w, h, r, fill="white", outline="white")
        hist_frame = Frame(hist_canvas, bg="white")
        hist_frame.place(x=0, y=0, width=w, height=h)
        Label(
            hist_frame,
            text="Historial",
            font=("Consolas", 16, "bold"),
            bg="white",
            fg="#222",
        ).pack(anchor="w", padx=32, pady=(32, 0))

        cards_frame = Frame(hist_frame, bg="white")
        cards_frame.place(relx=0.5, rely=0.0, y=80, anchor="n")
        estados = [("Iniciado", 1), ("Pendiente", 3), ("Finalizado", 5)]
        card_w, card_h = 210, 130
        sep = 48
        total_cards = len(estados)
        total_width = total_cards * card_w + (total_cards - 1) * sep
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
                card_w // 2, 32, text=estado, font=("Consolas", 14, "bold"), fill="#888"
            )

            icon_path = os.path.join("assets", "images", "torneo_icon_historial.png")
            icon_img = PhotoImage(file=icon_path)
            card_canvas.create_image(card_w // 2 - 38, 85, image=icon_img)
            card_canvas.image = icon_img
            card_canvas.create_text(
                card_w // 2 + 38,
                85,
                text=str(num),
                font=("Consolas", 26, "bold"),
                fill="#222",
            )

        # Tabla torneos
        table_card_container = Frame(frame, bg="#EDEDED")
        table_card_container.pack(
            anchor="n", padx=40, pady=(0, 0), fill=None, expand=False
        )

        card_w, card_h = 980, 480
        card_canvas = Canvas(
            table_card_container,
            width=card_w,
            height=card_h,
            bg="#EDEDED",
            highlightthickness=0,
        )
        card_canvas.pack()
        draw_rounded_rect(
            card_canvas, 0, 0, card_w, card_h, 18, fill="white", outline="white"
        )

        table_card = Frame(card_canvas, bg="white")
        table_card.place(x=0, y=0, width=card_w, height=card_h)

        title_row = Frame(table_card, bg="white")
        title_row.pack(fill="x", padx=32, pady=(24, 0))
        Label(
            title_row,
            text="Torneos",
            font=("Consolas", 20, "bold"),
            bg="white",
            fg="#222",
        ).pack(side="left")
        RoundedButton(
            title_row,
            text="Crear torneo",
            width=180,
            height=48,
            radius=18,
            font=("Consolas", 14, "bold"),
            command=lambda: print("Crear torneo"),
        ).pack(side="right", padx=(0, 50))

        headers = ["ID", "Torneo", "Inicio", "Fin", "Estado", ""]
        data = [
            [f"{i:02}", f"Torneo {i}", "01/01/24", "05/01/24", "Pendiente"]
            for i in range(1, 40)
        ]

        def action_buttons(row, parent, text):
            btn_frame = Frame(parent, bg=parent["bg"])
            TableActionButton(
                btn_frame,
                icon_path="assets/images/edit.png",
                command=lambda: print(f"Editar {row[1]}"),
            ).pack(side="left", padx=(0, 8))
            TableActionButton(
                btn_frame,
                icon_path="assets/images/delete.png",
                command=lambda: print(f"Eliminar {row[1]}"),
            ).pack(side="left", padx=(0, 8))
            TableActionButton(
                btn_frame,
                icon_path="assets/images/eye.png",
                command=lambda: print(f"Ver info de {row[1]}"),
            ).pack(side="left")
            return btn_frame

        col_widths = [60, 150, 160, 160, 180, 200]

        table = TableView(
            table_card,
            headers,
            data,
            actions=[action_buttons],
            title=None,
            count=len(data),
            col_widths=col_widths,
            action_text="Ver información",
        )
        table.pack(padx=0, pady=(10, 0), fill="both", expand=True)
