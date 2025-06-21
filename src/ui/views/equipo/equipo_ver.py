from tkinter import *
from ui.elements import RoundedButton, StyledEntry


class EquipoFormViewNoEdit:
    def __init__(self, jugadores, parent, equipo):
        frame = Frame(parent, bg="#EDEDED")
        frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        header_bg = Frame(frame, bg="#F6F6F6")
        header_bg.pack(fill="x", padx=0, pady=(0, 0))
        titulo = f"Información de {equipo["nombre"]}"
        Label(
            header_bg,
            text=titulo,
            font=("Consolas", 28, "bold"),
            bg="#F6F6F6",
            fg="#222",
            anchor="w",
        ).pack(fill="x", padx=60, pady=(36, 18))

        Frame(frame, height=18, bg="#EDEDED").pack()

        card_w, card_h = 900, 520
        card = Frame(frame, bg="white", width=card_w, height=card_h)
        card.place(x=60, y=120)
        card.pack_propagate(False)

        Label(
            card,
            text="Nombre del equipo",
            font=("Consolas", 16, "bold"),
            bg="white",
            fg="#1A1832",
            anchor="w",
        ).pack(fill="x", padx=20, pady=(30, 6))

        
        Label(
            card,
            text=equipo["nombre"],
            font=("Consolas", 13),                        
            bg="#F6F6F6",
            fg="#222",
            relief="flat",
            highlightthickness=0,
        ).pack(fill="x", padx=20, pady=(0, 24))

        Label(
            card,
            text="Jugadores",
            font=("Consolas", 22, "bold"),
            bg="white",
            fg="#888",
            anchor="w",
        ).pack(fill="x", padx=20, pady=(0, 10))

        # --- SCROLLABLE AREA ---
        
        jugadores_frame_container = Frame(card, bg="white")
        jugadores_frame_container.pack(fill="both", padx=20, pady=(0, 24), expand=True)
        canvas = Canvas(
            jugadores_frame_container, bg="white", highlightthickness=0, height=220
        )
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar = Scrollbar(
            jugadores_frame_container, orient="vertical", command=canvas.yview
        )
        scrollbar.pack(side="right", fill="y")
        canvas.configure(yscrollcommand=scrollbar.set)
        jugadores_frame = Frame(canvas, bg="white")
        canvas.create_window((0, 0), window=jugadores_frame, anchor="nw")

        def on_configure(event):
            canvas.configure(scrollregion=canvas.bbox("all"))

        jugadores_frame.bind("<Configure>", on_configure)
        canvas.bind_all(
            "<MouseWheel>",
            lambda event: canvas.yview_scroll(int(-1 * (event.delta / 120)), "units"),
        )
        # --- END SCROLLABLE ---

        miembros = list(j["id_jugador"] for j in equipo["jugadores"])
        self.lider_id = (
            next((j["id_jugador"] for j in equipo["jugadores"] if j["es_lider"]), None) 
        )

        # Mostrar jugadores en grid
        idx = 0
        for jugador in jugadores:
            if(jugador["id"] not in miembros):
                continue
            col = idx % 3
            row = idx // 3
            # Card con borde redondeado
            card_j = Canvas(
                jugadores_frame, width=250, height=80, bg="white", highlightthickness=0
            )
            card_j.grid(row=row, column=col, padx=12, pady=10)
            # Dibuja fondo redondeado
            r = 18
            card_j.create_polygon(
                [
                    10 + r,
                    10,
                    240 - r,
                    10,
                    240,
                    10,
                    240,
                    10 + r,
                    240,
                    70 - r,
                    240,
                    70,
                    240 - r,
                    70,
                    10 + r,
                    70,
                    10,
                    70,
                    10,
                    70 - r,
                    10,
                    10 + r,
                    10,
                    10,
                ],
                smooth=True,
                fill="#FAFAFA",
                outline="#688CCA",
                width=2,
            )
            # Frame para contenido encima del canvas
            content = Frame(card_j, bg="#FAFAFA")
            card_j.create_window(125, 40, window=content)
            Label(
                content,
                text=jugador["nombre"],
                font=("Consolas", 13, "bold"),
                bg="#FAFAFA",
                fg="#222",
            ).pack(anchor="w", padx=0, pady=(0, 2))            
            if(self.lider_id == jugador["id"]):
                lider_btn = RoundedButton(
                    content,
                    text="Líder",
                    width=90,
                    height=28,
                    radius=12,
                    font=("Consolas", 9, "bold"),
                    bg="#688CCA",
                    fg="white",
                    hover_bg="#688CCA",
                    command=None,
                )
                lider_btn.pack(padx=(8, 0))
            idx += 1
        # RoundedButton(
        #     card,
        #     text="Guardar",
        #     width=320,
        #     height=44,
        #     radius=18,
        #     font=("Consolas", 13, "bold"),
        #     command=lambda: (
        #         on_save(self.name_var.get(), get_jugadores_result(), self.lider_id)
        #         if on_save
        #         else None
        #     ),
        # ).pack(pady=(30, 0))
