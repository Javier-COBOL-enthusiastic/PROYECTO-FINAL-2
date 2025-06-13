from tkinter import *
from ui.elements import RoundedButton, StyledEntry


class EquipoFormView:
    def __init__(self, parent, jugadores, equipo=None, on_save=None):
        frame = Frame(parent, bg="#EDEDED")
        frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        header_bg = Frame(frame, bg="#F6F6F6")
        header_bg.pack(fill="x", padx=0, pady=(0, 0))
        titulo = "Editar equipo" if equipo else "Crear equipo"
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

        self.name_var = StringVar(value=equipo["nombre"] if equipo else "")
        StyledEntry(
            card,
            textvariable=self.name_var,
            font=("Consolas", 13),
            placeholder="Nombre del equipo...",
            border_radius=16,
        ).pack(fill="x", padx=20, pady=(0, 24))

        Label(
            card,
            text="Jugadores",
            font=("Consolas", 22, "bold"),
            bg="white",
            fg="#888",
            anchor="w",
        ).pack(fill="x", padx=20, pady=(0, 10))

        # Estado de selección y líder
        self.selected_jugadores = (
            set(j["id_jugador"] for j in equipo["jugadores"]) if equipo else set()
        )
        self.lider_id = (
            next((j["id_jugador"] for j in equipo["jugadores"] if j["es_lider"]), None)
            if equipo
            else None
        )
        self.jugador_vars = {}
        self.lider_btns = {}

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

        def update_lider_buttons():
            for jid, btn in self.lider_btns.items():
                if self.lider_id == jid:
                    btn.set_text("Líder")
                    btn.set_colors(bg="#688CCA", fg="white", hover_bg="#4B6EA8")
                else:
                    btn.set_text("Hacer líder")
                    btn.set_colors(bg="#EEE", fg="#688CCA", hover_bg="#DDD")

        def toggle_jugador(jid):
            if self.jugador_vars[jid].get():
                self.selected_jugadores.add(jid)
            else:
                self.selected_jugadores.discard(jid)
                if self.lider_id == jid:
                    self.lider_id = None
                    update_lider_buttons()

        def set_lider(jid):
            if jid in self.selected_jugadores:
                self.lider_id = jid
                update_lider_buttons()

        # Mostrar jugadores en grid
        for idx, jugador in enumerate(jugadores):
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
            btns = Frame(content, bg="#FAFAFA")
            btns.pack(anchor="w", pady=(0, 0))
            var = IntVar(value=1 if jugador["id"] in self.selected_jugadores else 0)
            self.jugador_vars[jugador["id"]] = var
            chk = Checkbutton(
                btns,
                variable=var,
                command=lambda jid=jugador["id"]: toggle_jugador(jid),
                bg="#FAFAFA",
            )
            chk.pack(side="left")
            # Botón redondeado para líder
            lider_btn = RoundedButton(
                btns,
                text="Líder" if self.lider_id == jugador["id"] else "Hacer líder",
                width=90,
                height=28,
                radius=12,
                font=("Consolas", 9, "bold"),
                bg="#688CCA" if self.lider_id == jugador["id"] else "#EEE",
                fg="white" if self.lider_id == jugador["id"] else "#688CCA",
                hover_bg="#4B6EA8" if self.lider_id == jugador["id"] else "#DDD",
                command=lambda jid=jugador["id"]: set_lider(jid),
            )
            lider_btn.pack(side="left", padx=(8, 0))
            self.lider_btns[jugador["id"]] = lider_btn
            update_lider_buttons()

        def get_jugadores_result():
            return [
                {"id_jugador": jid, "es_lider": (jid == self.lider_id)}
                for jid in self.selected_jugadores
            ]

        RoundedButton(
            card,
            text="Guardar",
            width=320,
            height=44,
            radius=18,
            font=("Consolas", 13, "bold"),
            command=lambda: (
                on_save(self.name_var.get(), get_jugadores_result(), self.lider_id)
                if on_save
                else None
            ),
        ).pack(pady=(30, 0))
