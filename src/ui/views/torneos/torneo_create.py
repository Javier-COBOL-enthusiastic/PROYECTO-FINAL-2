from tkinter import *
from ui.elements import RoundedButton, StyledEntry, TableActionButton
from ui.views.equipo.equipo_form import EquipoFormView
from ui.mocks import get_jugadores, update_equipo
from ui.elements import RoundedButton, AlertDialog    





class TorneoFormView:  
    def on_save_edit(self, equipo_id, nombre, jugadores, lider_id):
        equipos = self.equipos
        if not nombre.strip():
            AlertDialog(
                self.parent.winfo_toplevel(), "El nombre del equipo no puede estar vacío.", success=False
            )
            return
        if not jugadores:
            AlertDialog(self.parent.winfo_toplevel(), "Selecciona al menos un equipo.", success=False)
            return
        if not lider_id or not any(j["id_jugador"] == lider_id for j in jugadores):
            AlertDialog(self.parent.winfo_toplevel(), "Selecciona un líder válido.", success=False)
            return
        if any(
            e["nombre"].strip().lower() == nombre.strip().lower()
            and e["id"] != equipo_id
            for e in equipos
        ):
            AlertDialog(
                self.parent.winfo_toplevel(), "Ya existe un equipo con ese nombre.", success=False
            )
            return
        update_equipo(equipo_id, nombre, jugadores)
        AlertDialog(
            self.parent.winfo_toplevel(),
            "Equipo actualizado exitosamente.",
            success=True,
            on_close=self.__show_list(),
        )
        


    def show_edit_view(self, equipo_id):
        if not self.torneo:
            self.torneo = {"nombre":self.name_var.get()}            

        equipos = self.equipos
        equipo = next((e for e in equipos if e["id"] == equipo_id), None)

        if not equipo:
            return

        for widget in self.frame.winfo_children():
                widget.destroy()

        EquipoFormView(
            self.frame,
            get_jugadores(),
            equipo=equipo,
            on_save=lambda nombre, jugadores, lider: self.on_save_edit(
                equipo["id"], nombre, jugadores, lider
            ),
        ) 

    def __init__(self, parent, equipos, torneo=None, on_save=None):
        self.parent = parent
        self.frame = Frame(parent, bg="#EDEDED")
        self.torneo = torneo
        self.frame.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.equipos = equipos

        self.selected_equipos = set()
        self.equipo_vars = {}                

        self.__show_list()


    def __show_list(self):
        for widget in self.frame.winfo_children():
                widget.destroy()


        header_bg = Frame(self.frame, bg="#F6F6F6")
        header_bg.pack(fill="x", padx=0, pady=(0, 0))
        titulo = "Editar torneo" if self.torneo else "Crear torneo"
        Label(
            header_bg,
            text=titulo,
            font=("Consolas", 28, "bold"),
            bg="#F6F6F6",
            fg="#222",
            anchor="w",
        ).pack(fill="x", padx=60, pady=(36, 18))

        Frame(self.frame, height=18, bg="#EDEDED").pack()

        card_w, card_h = 900, 520
        card = Frame(self.frame, bg="white", width=card_w, height=card_h)
        card.place(x=60, y=120)
        card.pack_propagate(False)
        input_frame = Frame(card, bg="white", width=card_w, height=200)
        input_frame.pack(fill="x")
        Label(
            input_frame,
            text="Nombre del equipo",
            font=("Consolas", 14, "bold"),
            bg="white",
            fg="#1A1832",
            anchor="w",
        ).grid(column=0, row=0, padx=20, pady=(30, 6))        
        Label(
            input_frame,
            text="Fecha de Inicio",
            font=("Consolas", 14, "bold"),
            bg="white",
            fg="#1A1832",
            anchor="w",
        ).grid(column=1, row=0, padx=20, pady=(30, 6))
        Label(
            input_frame,
            text="Fecha de Fin",
            font=("Consolas", 14, "bold"),
            bg="white",
            fg="#1A1832",
            anchor="w",
        ).grid(column=2, row=0, padx=20, pady=(30, 6))

        self.name_var = StringVar(value=self.torneo["nombre"] if self.torneo else "")
        StyledEntry(
            input_frame,
            textvariable=self.name_var,
            font=("Consolas", 12),
            placeholder="Nombre del torneo...",
            border_radius=16,
            width=350
        ).grid(column=0, row=1,padx=20, pady=(0, 24))

        self.inicio = StringVar(value=self.torneo["inicio"] if self.torneo else "")
        StyledEntry(
            input_frame,
            textvariable=self.inicio,
            font=("Consolas", 12),
            placeholder="DD/MM/YYYY",
            border_radius=16,
            width=200
        ).grid(column=1, row=1,padx=20, pady=(0, 24))

        self.fin = StringVar(value=self.torneo["fin"] if self.torneo else "")
        StyledEntry(
            input_frame,
            textvariable=self.fin,
            font=("Consolas", 12),
            placeholder="DD/MM/YYYY",
            width=200,
            border_radius=16,
        ).grid(column=2, row=1,padx=20, pady=(0, 24))

        Label(
            card,
            text="Equipos",
            font=("Consolas", 22, "bold"),
            bg="white",
            fg="#888",
            anchor="w",
        ).pack(fill="x", padx=20, pady=(0, 10))


        equipos_frame_container = Frame(card, bg="white")
        equipos_frame_container.pack(fill="both", padx=20, pady=(0, 24), expand=True)
        canvas = Canvas(
            equipos_frame_container, bg="white", highlightthickness=0, height=220
        )
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar = Scrollbar(
            equipos_frame_container, orient="vertical", command=canvas.yview
        )
        scrollbar.pack(side="right", fill="y")
        canvas.configure(yscrollcommand=scrollbar.set)
        equipos_frame = Frame(canvas, bg="white")
        canvas.create_window((0, 0), window=equipos_frame, anchor="nw")

        def on_configure(event):
            canvas.configure(scrollregion=canvas.bbox("all"))

        equipos_frame.bind("<Configure>", on_configure)
        canvas.bind_all(
            "<MouseWheel>",
            lambda event: canvas.yview_scroll(int(-1 * (event.delta / 120)), "units"),
        )

        def toggle_equipo(jid):
            if self.equipo_vars[jid].get():
                self.selected_equipos.add(jid)
            else:
                self.selected_equipos.discard(jid)                

        for idx, equipo in enumerate(self.equipos):
            col = idx % 3
            row = idx // 3
            # Card con borde redondeado
            card_j = Canvas(
                equipos_frame, width=250, height=80, bg="white", highlightthickness=0
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
            content = Frame(card_j, bg="#FAFAFA")
            card_j.create_window(125, 40, window=content)
            Label(
                content,
                text=equipo["nombre"],
                font=("Consolas", 13, "bold"),
                bg="#FAFAFA",
                fg="#222",
            ).pack(anchor="w", padx=0, pady=(0, 2))
            btns = Frame(content, bg="#FAFAFA")
            btns.pack(anchor="w", pady=(0, 0))
            var = IntVar(value=1 if equipo["id"] in self.selected_equipos else 0)
            self.equipo_vars[equipo["id"]] = var
            chk = Checkbutton(
                btns,
                variable=var,
                command=lambda jid=equipo["id"]: toggle_equipo(jid),
                bg="#FAFAFA",
            )  
            chk.pack(side="left")           
            def action_button(id, parent, text):
                btn = RoundedButton(
                    parent,
                    text=text,
                    width=90,
                    height=28,
                    radius=12,
                    font=("Consolas", 9, "bold"),
                    bg="#EEE",
                    fg="#688CCA",
                    hover_bg="#DDD",
                    command=lambda id = id : self.show_edit_view(id)
                )
                return btn

            action_button(equipo["id"], btns, "Editar").pack(side="left", padx=(8, 0))

        RoundedButton(
            card,
            text="Guardar",
            width=320,
            height=44,
            radius=18,
            font=("Consolas", 13, "bold"),
            command=None            
        ).pack(pady=(30, 0))