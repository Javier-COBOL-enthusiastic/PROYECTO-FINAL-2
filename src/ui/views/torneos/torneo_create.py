from tkinter import *
from ui.elements import RoundedButton, StyledEntry, StyledCombobox, AlertDialog
from ui.views.equipo.equipo_form import EquipoFormView
from ui.views.jugadores import JugadorFormView
from ui.mocks import update_jugador, update_equipo, create_torneo, delete_torneo
from datetime import datetime
from math import sqrt




class TorneoFormView:
    def actualizar_torneo(self):
         self.torneo = {
                "nombre":self.name_var.get(), 
                "inicio":self.inicio.get(), 
                "fin":self.fin.get(), 
                "juego":self.juego_selec.get()
        }     

    def impar_cancelar(self):            
            delete_torneo(self.torneo["id"])
            self.__show_list()

    def on_save(self):
        self.actualizar_torneo()             

        self.clean_data = [x for i, x in self.torneo.items()]
        
        #print(self.clean_data)     
                
        if(len(self.clean_data[0]) == 0 or self.clean_data[0] == "Nombre del torneo..."):
            AlertDialog(
                self.parent.winfo_toplevel(), "El nombre del torneo no puede estar vacío.", success=False, on_close=self.__show_list
            )
            return

        if(len(self.clean_data) > 34):
            AlertDialog(self.parent.winfo_toplevel(), "El nombre del torneo es muy largo.", success=False, on_close=self.__show_list)

        if(len(self.clean_data[-1]) == 0): 
            AlertDialog(
                self.parent.winfo_toplevel(), "El juego es invalido.", success=False, on_close=self.__show_list
            )
            return


        
        r1 = self.__valid_format__(self.clean_data[1])
        r2 = self.__valid_format__(self.clean_data[2])
        if(not(r1 and r2)):
            AlertDialog(
                self.parent.winfo_toplevel(), "El formato del fecha es incorrecto. \nEjemplo correcto: '02/07/2025'", success=False, on_close=self.__show_list
            )
            return
        f_1 = None
        f_2 = None
        try:
            f_1 = datetime.strptime(self.clean_data[1], "%d/%m/%Y")
            f_2 = datetime.strptime(self.clean_data[2], "%d/%m/%Y")
        except ValueError:
            AlertDialog(self.parent.winfo_toplevel(), "El formato del fecha es incorrecto. \nEjemplo correcto: '02/07/2025'", success=False, on_close=self.__show_list)
            return
        
        

    
        if(f_2 < f_1): #el inicio es despues del fin xd????
            AlertDialog(
                self.parent.winfo_toplevel(), "La fechas de fin es invalida.", success=False, on_close=self.__show_list
            )
            return
        actual = datetime.now()
        cmp = datetime(actual.year, actual.month, actual.day)
        if(f_1 < cmp):
            AlertDialog(
                self.parent.winfo_toplevel(), "La fecha de inicio es invalida", success=False, on_close=self.__show_list
            )
            return
        n_participantes = len(self.selected)
        if n_participantes <= 1:
            AlertDialog(
                self.parent.winfo_toplevel(), "El número de participantes es menor o igual que 1.", success=False, on_close=self.__show_list
            )
            return        

                    
        if n_participantes % 2 != 0: #Hay q ver como manejar esto XD
            AlertDialog(
                self.parent.winfo_toplevel(), 
                "El número de participantes es impar.", 
                success=False, on_close=self.__show_list
            )
            return
        
        #Parte de crear el torneo y matchmaking
        matches = []        
        data = []
        if self.mostrar_equipo:                    

            juga = set()            
            data = [j for j in self.equipos if j["id"] in self.selected]

            prom = 0
            for equipo in data:
                prom += len(equipo["jugadores"])
                for jg in equipo["jugadores"]:
                    juga.add(jg["id_jugador"])
            
            if(len(juga) != prom):
                AlertDialog(
                    parent=self.parent.winfo_toplevel(),
                    message="Un jugador está registrado en dos equipos.",
                    success=False, on_close=self.__show_list
                )      
                return


            prom = prom / len(data)

            std_valid = prom * 0.334

            suma = 0
            for equipo in data:
                suma += (len(equipo["jugadores"]) - prom) ** 2
            
            suma = suma / (len(data) - 1)

            std = sqrt(suma)

            if(int(std) > int(std_valid)):
                AlertDialog(
                    parent=self.parent.winfo_toplevel(),
                    message="La cantidad de jugadores entre los equipos es muy desigual.",
                    success=False, on_close=self.__show_list
                )      
                return

            def add_puntos(equipo): #quitar despues?
                suma = 0
                for id in equipo["jugadores"]:
                    for jugador in self.jugadores:
                        if(jugador["id"] == id["id_jugador"]):
                            suma += jugador["puntos"]                                
                return (equipo, suma)            
            
            data = [add_puntos(j) for j in data]
            data = sorted(data, key=lambda x : x[1])
                       
        else:
            data = [j for j in self.jugadores if j["id"] in self.selected]        
            data = sorted(data, key=lambda a : a["puntos"])


        for i in range(0, len(data) - 1, 2):                    
            if self.mostrar_equipo:
                matches.append([data[i][0], data[i + 1][0], None])
            else:
                matches.append([data[i], data[i + 1], None])
        
        #El None sera el id del ganador

        rondas = (len(matches) // 2)
        
        self.torneo["rondas"] = []
        self.torneo["rondas"].append(matches)  
        for i in range(1, rondas + 1):
            mult = (len(self.torneo["rondas"][i - 1]) // 2)
            self.torneo["rondas"].append([])
            for j in range(mult):
                self.torneo["rondas"][i].append([])
        

        res = create_torneo(self.torneo)
        if res is None:
            AlertDialog(
                self.parent.winfo_toplevel(), 
                "Ya existe un torneo con este nombre.", 
                success=False, on_close=self.__show_list
            )
            return
        AlertDialog(
            parent=self.parent.winfo_toplevel(),
            message="Torneo creado.",
            on_close=self.volver(),
        )        
                        
    
    def __valid_format__(self, fecha : str):        
        if(len(fecha) <= 0):
            return False
        if(fecha.count("/") < 1): #Se puede hacer por separado pero pq me dieron ganas asi
            return False
            
        fecha = fecha.split("/")#Arreglando por si solo puso 1/6/2025 ejemplo
        if(len(fecha[0]) < 2):
            fecha[0] = '0' + fecha[0]    
        if(len(fecha[1]) < 2): #Arreglando por si solo puso 25/6/2025 ejemplo
            fecha[1] = '0' + fecha[1]                
        fecha = str.join("/", fecha)
        return True


    def on_save_equipo_edit(self, equipo_id, nombre, jugadores, lider_id):
        equipos = self.equipos
        if not nombre.strip():
            AlertDialog(
                self.parent.winfo_toplevel(), "El nombre del equipo no puede estar vacío.", success=False, on_close=self.__show_list
            )
            return
        if not jugadores:
            AlertDialog(self.parent.winfo_toplevel(), "Selecciona al menos un equipo.", success=False, on_close=self.__show_list)
            return
        if not lider_id or not any(j["id_jugador"] == lider_id for j in jugadores):
            AlertDialog(self.parent.winfo_toplevel(), "Selecciona un líder válido.", success=False, on_close=self.__show_list)
            return
        if any(
            e["nombre"].strip().lower() == nombre.strip().lower()
            and e["id"] != equipo_id
            for e in equipos
        ):
            AlertDialog(
                self.parent.winfo_toplevel(), "Ya existe un equipo con ese nombre.", success=False, on_close=self.__show_list
            )
            return
        update_equipo(equipo_id, nombre, jugadores)
        AlertDialog(
            self.parent.winfo_toplevel(),
            "Equipo actualizado exitosamente.",
            success=True,
            on_close=self.__show_list,
        )
    
    def on_save_jugador_edit(self, nombre, puntos, id):
                nombre = nombre.strip()
                if not nombre:
                    AlertDialog(
                        self.frame, "El nombre no puede estar vacío", success=False
                    )
                    return
                nombre_lower = nombre.lower()
                for j in self.jugadores:
                    if j["nombre"].lower() == nombre_lower and j["id"] != id:
                        AlertDialog(
                            self.frame,
                            "Ya existe un jugador con ese nombre",
                            success=False,
                            on_close=self.__show_list
                        )
                        return
                try:
                    update_jugador(id, nombre, puntos)
                    AlertDialog(
                        self.frame,
                        "Dato actualizado exitosamente",
                        success=True,
                        on_close=self.__show_list                  
                    )
                except Exception as e:
                    AlertDialog(
                        self.frame,
                        "Ha ocurrido un error",
                        success=False,
                        on_close=self.__show_list
                    )
        
    def show_jugador_edit_view(self, jugador_id):
        self.actualizar_torneo()       

        jugadores = self.jugadores
        jugador = next((e for e in jugadores if e["id"] == jugador_id), None)

        if not jugador:
            return
        
        for widget in self.frame.winfo_children():
                widget.destroy()

        JugadorFormView(
            parent=self.frame,
            on_save=lambda nombre, puntos, id : self.on_save_jugador_edit(nombre, puntos, id),
            initial_name=jugador["nombre"],
            initial_points=jugador["puntos"],
            jugador_id=jugador["id"]
        )

    def show_equipo_edit_view(self, equipo_id):
        self.actualizar_torneo()       

        equipos = self.equipos
        equipo = next((e for e in equipos if e["id"] == equipo_id), None)

        if not equipo:
            return

        for widget in self.frame.winfo_children():
                widget.destroy()

        EquipoFormView(
            self.frame,
            self.jugadores,
            equipo=equipo,
            on_save=lambda nombre, jugadores, lider: self.on_save_equipo_edit(
                equipo["id"], nombre, jugadores, lider
            ),
        ) 

    def mostrar_equipos(self):
        self.mostrar_equipo = not self.mostrar_equipo
        self.selected.clear()
        self.seleccion_tabla()

    def seleccion_tabla(self):
        self.canvas.yview_moveto(0)

        self.curr_selec.configure(text="Equipos" if self.mostrar_equipo else "Jugadores")
        self.op_selec.set_text("Un Jugador" if self.mostrar_equipo else "Por Equipos")

        def toggle_equipo(jid):
            if self.equipo_vars[jid].get():
                self.selected.add(jid)
            else:
                self.selected.discard(jid)                

        
        self.data = self.equipos if self.mostrar_equipo else self.jugadores

        for widget in self.data_frame.winfo_children():
            widget.destroy()


        for idx, equipo in enumerate(self.data):
            col = idx % 3
            row = idx // 3
            # Card con borde redondeado
            card_j = Canvas(
                self.data_frame, width=250, height=80, bg="white", highlightthickness=0
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
            var = IntVar(value=1 if equipo["id"] in self.selected else 0)
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
                    command=lambda id = id : (self.show_equipo_edit_view(id) if self.mostrar_equipo else self.show_jugador_edit_view(id))
                )
                return btn

            action_button(equipo["id"], btns, "Editar").pack(side="left", padx=(8, 0))

    def __init__(self, parent, jugadores, equipos, on_save):
        self.parent = parent
        self.frame = Frame(parent, bg="#EDEDED")
        self.torneo = None
        self.frame.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.equipos = equipos
        self.jugadores = jugadores

        self.mostrar_equipo = True

        self.volver = on_save

        self.selected = set()
        self.equipo_vars = {}                

        self.__show_list()


    def __show_list(self):
        for widget in self.frame.winfo_children():
                widget.destroy()


        header_bg = Frame(self.frame, bg="#F6F6F6")
        header_bg.pack(fill="x", padx=0, pady=(0, 0))
        titulo = "Crear torneo"
        Label(
            header_bg,
            text=titulo,
            font=("Consolas", 28, "bold"),
            bg="#F6F6F6",
            fg="#222",
            anchor="w",
        ).pack(fill="x", padx=60, pady=(36, 18))

        Frame(self.frame, height=18, bg="#EDEDED").pack()

        card_w, card_h = 900, 560
        card = Frame(self.frame, bg="white", width=card_w, height=card_h)
        card.place(x=60, y=120)
        card.pack_propagate(False)
        input_frame = Frame(card, bg="white", width=card_w, height=200)
        input_frame.pack(fill="x")
        input_frame.columnconfigure([0, 1], weight=1)
        Label(
            input_frame,
            text="Nombre del Torneo",
            font=("Consolas", 14, "bold"),
            bg="white",
            fg="#1A1832",
            anchor="w",
        ).grid(column=0, row=0, padx=20, pady=(30, 6), sticky="WE")        
        
        self.name_var = StringVar(value=self.torneo["nombre"] if self.torneo else "")
        StyledEntry(
            input_frame,
            textvariable=self.name_var,
            font=("Consolas", 12),
            placeholder="Nombre del torneo...",
            border_radius=16,
            width=350
        ).grid(column=0, row=1, padx=20, pady=(0, 24), sticky="WE")

        self._on_mousewheel_callback = lambda e: _on_mouse_wheel(e)
        self.juego_selec = StringVar(value=self.torneo["juego"] if self.torneo else "")
        self.combo = StyledCombobox(
            parent=input_frame,
            values=[
                "Overwatch",
                "Valorant",
                "Counter-Strike",
                "League of Legends",
                "Dota 2",
                "Fortnite",
                "Rocket League",
                "Rainbow Six Siege",
                "Apex Legends",
                "PUBG",
                "Call of Duty Warzone",
                "Street Fighter",
                "Tekken",
                "Super Smash Bros",
                "FIFA",
                "NBA 2K",
                "Hearthstone",
                "Magic: The Gathering Arena",
                "StarCraft II",
                "Splatoon",
                "Escape from Tarkov",
                "Battlefield",
                "Team Fortress 2",
                "Paladins",
                "Quake Champions",
                "World of Warcraft Arena",
                "Guild Wars 2 PvP",
                "Age of Empires IV",
                "Company of Heroes",
                "Smite",
                "Brawlhalla",
                "Mortal Kombat",
                "Gran Turismo",
                "iRacing",
                "Assetto Corsa Competizione",
                "TrackMania",
                "Chess.com",
                "Legends of Runeterra",
                "Gwent",
                "Yu-Gi-Oh! Master Duel",
                "Halo Infinite",
                "Destiny 2",
                "Dead by Daylight",
                "For Honor",
                "Naraka: Bladepoint",
                "Among Us",
                "Fall Guys",
                "Tetris 99",
                "Pokémon Unite",
                "Clash Royale",
                "Clash of Clans",
                "Boom Beach Frontlines",
                "Crossfire",
                "Warface",
                "Planetside 2",
                "Sea of Thieves Arena",
                "Mario Kart 8 Deluxe",
                "Splatoon 3",
                "Puyo Puyo Tetris",
                "King of Fighters",
                "Diabotical",
                "Warframe Conclave",
                "Chivalry 2",
                "Mordhau",
                "Crab Game",
                "Rust",
                "ARK: Survival of the Fittest",
                "DayZ",
                "Insurgency: Sandstorm",
                "Squad",
                "Hunt: Showdown",
                "War Thunder",
                "World of Tanks",
                "World of Warships",
                "EVE Online PvP",
                "Ultima Online PvP",
                "Street Fighter 6",
                "Virtua Fighter 5",
                "BlazBlue",
                "Guilty Gear",
                "Dark Souls PvP",
                "Elden Ring PvP",
                "Mortal Online 2",
                "Gloria Victis",
                "Mount & Blade II: Bannerlord",
                "Forza Horizon 5",
                "Rivals of Aether",
                "Nickelodeon All-Star Brawl",
                "MultiVersus",
                "Roller Champions",
                "Knockout City",
                "Hyper Scape",
                "SpellBreak",
                "Realm Royale",
                "Heroes of the Storm",
                "Heroes of Newerth",
            ],
            textvariable=self.juego_selec,
            placeholder=self.juego_selec.get() if self.torneo else "Videojuego",
            width=200,        
            height=30,
            mousewheel_callback=self._on_mousewheel_callback,            
        ).grid(column=1, row=1, sticky="EW")

        Label(
            input_frame,
            text="VideoJuego",
            font=("Consolas", 14, "bold"),
            bg="white",
            fg="#1A1832",
            anchor="w",
        ).grid(column=1, row=0, padx=20, pady=(0, 24), sticky="EW")

        selec_tabla_frame = Frame(card, bg="white", width=card_w)
        selec_tabla_frame.pack(fill="x")
        self.curr_selec = Label(
            selec_tabla_frame,
            text="Equipos",
            font=("Consolas", 22, "bold"),
            bg="white",
            fg="#888",
            anchor="w",
        )
        self.curr_selec.pack(padx=20, pady=(0, 10), side="left")
        self.op_selec = RoundedButton(
            selec_tabla_frame,
            text="Un solo jugador",
            font=("Consolas", 16, "bold"),            
            command=self.mostrar_equipos
        )
        self.op_selec.pack(padx=20, pady=(0, 10), side="left")
        
        fechas_frame = Frame(selec_tabla_frame, bg="white")
        fechas_frame.pack(side="right")

        Label(
            fechas_frame,
            text="Fecha de Inicio",
            font=("Consolas", 14, "bold"),
            bg="white",
            fg="#1A1832",
            anchor="w",
        ).grid(column=0, row=0, padx=20, pady=(30, 6))
        Label(
            fechas_frame,
            text="Fecha de Fin",
            font=("Consolas", 14, "bold"),
            bg="white",
            fg="#1A1832",
            anchor="w",
        ).grid(column=1, row=0, padx=20, pady=(30, 6))

        self.inicio = StringVar(value=self.torneo["inicio"] if self.torneo else "")
        StyledEntry(
            fechas_frame,
            textvariable=self.inicio,
            font=("Consolas", 12),
            placeholder="DD/MM/YYYY",
            border_radius=16,
            width=200
        ).grid(column=0, row=1,padx=20, pady=(0, 24))

        self.fin = StringVar(value=self.torneo["fin"] if self.torneo else "")
        StyledEntry(
            fechas_frame,
            textvariable=self.fin,
            font=("Consolas", 12),
            placeholder="DD/MM/YYYY",
            width=200,
            border_radius=16,
        ).grid(column=1, row=1,padx=20, pady=(0, 24))

        
        
        data_frame_container = Frame(card, bg="white")
        data_frame_container.pack(fill="both", padx=20, expand=True)
        self.canvas = Canvas(
            data_frame_container, bg="white", highlightthickness=0, height=220
        )
        self.canvas.pack(side="left", fill="both", expand=True)
        scrollbar = Scrollbar(
            data_frame_container, orient="vertical", command=self.canvas.yview
        )
        scrollbar.pack(side="right", fill="y")
        self.canvas.configure(yscrollcommand=scrollbar.set)
        self.data_frame = Frame(self.canvas, bg="white")
        self.canvas.create_window((0, 0), window=self.data_frame, anchor="nw")

        def on_configure(event):
            self.canvas.configure(scrollregion=self.canvas.bbox("all"))

        self.data_frame.bind("<Configure>", on_configure)


        def _on_mouse_wheel(e):    
            if not hasattr(self, 'combo') or not hasattr(self.combo, 'dropdown') or not self.combo.dropdown:
                self.canvas.yview_scroll(int(-1*(e.delta/120)), "units")
        
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel_callback)

        self.seleccion_tabla()
        
        RoundedButton(
            card,
            text="Guardar",
            width=320,
            height=44,
            radius=18,
            font=("Consolas", 13, "bold"),
            command=self.on_save            
        ).pack()