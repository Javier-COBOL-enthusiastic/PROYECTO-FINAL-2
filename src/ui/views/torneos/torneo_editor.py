from tkinter import *
from ui.elements import RoundedButton
from ui.mocks import update_jugador, get_jugadores


class TorneoEdit:
    def control(self, ronda=False, sum = True):
        if not ronda and (self.partida == 0 and not sum):
            return
        elif not ronda:
            self.partida += 1 if sum else -1
            if(self.partida == len(self.torneo["rondas"][self.ronda])):
                self.partida -= 1                    
        elif self.ronda == 0 and not sum:
            return
        else:
            self.partida = 0
            self.ronda += 1 if sum else -1
            if(self.ronda == len(self.torneo["rondas"])):
                self.ronda -= 1    
            self.ronda_label.configure(text=f"{self.ronda + 1}° Ronda" if (self.ronda + 1) < len(self.torneo["rondas"]) else "Ronda Final")

        self.update()
    

    def set_ganador(self, participante):                
        siguiente = max(0, self.partida - 1)
        if(self.ronda < len(self.torneo["rondas"]) - 1):            
            if(len(self.torneo["rondas"][self.ronda + 1][siguiente]) < 2):
                self.torneo["rondas"][self.ronda + 1][siguiente].append(participante)

            if(len(self.torneo["rondas"][self.ronda + 1][siguiente]) == 2):
                self.torneo["rondas"][self.ronda + 1][siguiente].append(None)            

        if(self.torneo["rondas"][self.ronda][self.partida][2] is None):                                                
            self.torneo["rondas"][self.ronda][self.partida][2] = participante["id"]
                                                                  
        self.update()


    def guardar(self):
        for ronda in self.torneo["rondas"]:
            for partida in ronda:
                if(len(partida) < 3):
                    continue
                if(partida[2] == None):
                    continue

                perdedor = partida[0] if partida[0]["id"] != partida[2] else partida[1]
                ganador = partida[0] if partida[0]["id"] == partida[2] else partida[1]
                
                if(partida[0].get("jugadores") == None):                
                    diff = abs(ganador["puntos"] - perdedor["puntos"]) // 4
                    if(diff == 0):
                        diff = 5
                    if(diff > 100):
                        diff = 100
                    ganador["puntos"] += diff
                    perdedor["puntos"] -= diff // 4
                    perdedor["puntos"] = 0 if perdedor["puntos"] < 0 else perdedor["puntos"]
                    for n in [ganador, perdedor]:
                        update_jugador(n["id"], n["nombre"], n["puntos"])
                else:
                    jugadores = get_jugadores()
                    def equipo_puntos(equipo): #no se quito jaja
                        suma = 0
                        for id in equipo["jugadores"]:
                            for jugador in jugadores:
                                if(jugador["id"] == id["id_jugador"]):
                                    suma += jugador["puntos"]                                
                        return suma
                    g = equipo_puntos(ganador)
                    p = equipo_puntos(perdedor)
                    diff = abs(g - p) // 4
                    g_id = [j["id_jugador"] for j in ganador["jugadores"]]
                    p_id = [j["id_jugador"] for j in perdedor["jugadores"]]                    
                    for n in jugadores:
                        if(n["id"] in g_id):
                            update_jugador(n["id"], n["nombre"], n["puntos"] + diff)
                        elif(n["id"] in p_id):
                            n["puntos"] = n["puntos"] - diff if (n["puntos"] - diff // 4) >= 0 else 0
                            update_jugador(n["id"], n["nombre"], n["puntos"])              
            self.on_save(self.torneo)

    def __init__(self, parent, torneo, on_save):
        self.parent = parent
        self.torneo = torneo
        self.ronda = 0
        self.partida = 0        
        self.on_save = on_save


        frame = Frame(parent, bg="#EDEDED")
        frame.place(relx=0, rely=0, relwidth=1, relheight=1)            

        header_bg = Frame(frame, bg="#F6F6F6")
        header_bg.pack(fill="x", padx=0, pady=(0, 0))
        titulo = f"Editar Torneo"
        Label(
            header_bg,
            text=titulo,
            font=("Consolas", 28, "bold"),
            bg="#F6F6F6",
            fg="#222",
            anchor="w",
        ).pack(fill="x", padx=60, pady=(36, 18))


        Frame(frame, height=18, bg="#EDEDED").pack()

        card_w, card_h = 900, 560
        card = Frame(frame, bg="white", width=card_w, height=card_h)
        card.place(x=60, y=120)
        card.pack_propagate(False)
        input_frame = Frame(card, bg="white", width=card_w, height=200)
        input_frame.pack(fill="x")
        input_frame.columnconfigure([0, 1], weight=1)
        Label(
            input_frame,
            text=f"Torneo {self.torneo['nombre']}",
            font=("Consolas", 20, "bold"),
            bg="white",
            fg="#1A1832",
            anchor="w",
        ).grid(column=0, row=0, padx=20, pady=(30, 6), sticky="WE")        
                
                        
        Label(
            input_frame,
            text=f"VideoJuego: {self.torneo['juego']}",
            font=("Consolas", 20, "bold"),
            bg="white",
            fg="#1A1832",
            anchor="w",
        ).grid(column=1, row=0, padx=20, pady=(30, 6), sticky="EW")

        container_frame = Frame(card, bg="white", width=card_w)
        container_frame.pack(fill="x")

        rondas_frame = Frame(container_frame, bg="white")
        rondas_frame.pack(side="left")
        RoundedButton(
            rondas_frame,
            text="<",
            font=("Consolas", 30),
            command=lambda : self.control(True, False),
            fg="#9FACE8",
            bg="white",
            width=50,
        ).pack(side="left", padx=20, pady=(0, 10))
        self.ronda_label = Label(
            rondas_frame,
            text=f"{self.ronda + 1}° Ronda" if (self.ronda + 1) < len(self.torneo['rondas']) else "Ronda Final",
            font=("Consolas", 22, "bold"),
            bg="white",
            fg="#888",
            anchor="w",
        )
        self.ronda_label.pack(padx=20, pady=(0, 10), side="left")
                        
        RoundedButton(
            rondas_frame,
            text=">",
            font=("Consolas", 30),
            fg="#9FACE8",
            bg="white",
            command=lambda : self.control(ronda=True),
            width=50,
        ).pack(side="left", padx=20, pady=(0, 10))

        
        fechas_frame = Frame(container_frame, bg="white")
        fechas_frame.pack(side="right")    

        Label(
            fechas_frame,
            text=f"Fecha de Inicio\n{self.torneo['inicio']}",
            font=("Consolas", 14, "bold"),
            bg="white",
            fg="#1A1832",
            anchor="w",
        ).grid(column=0, row=0, padx=20, pady=(30, 6))
        Label(
            fechas_frame,
            text=f"Fecha de Fin\n{self.torneo['fin']}",
            font=("Consolas", 14, "bold"),
            bg="white",
            fg="#1A1832",
            anchor="w",
        ).grid(column=1, row=0, padx=20, pady=(30, 6))
                
        
        self.data_frame_container = Frame(card, bg="white")
        self.data_frame_container.pack(fill="both", padx=20, pady=(0, 12), expand=True)        
        
        self.update()



    def update(self):
        for widget in self.data_frame_container.winfo_children():
            widget.destroy()

        canvas = Canvas(
            self.data_frame_container, bg="white", highlightthickness=0, height=220
        )
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar = Scrollbar(
            self.data_frame_container, orient="vertical", command=canvas.yview
        )
        #scrollbar.pack(side="right", fill="y")
        canvas.configure(yscrollcommand=scrollbar.set)
        data_frame = Frame(canvas, bg="white")
        canvas.create_window((0,0), window=data_frame, anchor="center", width=900)
        

        def on_configure(event):
            canvas.configure(scrollregion=canvas.bbox("all"))

        data_frame.bind("<Configure>", on_configure)
        canvas.bind_all(
            "<MouseWheel>",
            lambda event: "break"
        )

        partido_container_frame=Frame(data_frame, bg="white")
        partido_container_frame.pack()
        
        partidos = self.torneo["rondas"][self.ronda][self.partida]
        if(len(self.torneo["rondas"][self.ronda]) > 1):
            RoundedButton(
                partido_container_frame,
                text="<",
                font=("Consolas", 30),
                command=lambda : self.control(sum=False),
                fg="#9FACE8",
                bg="white",
                width=50,
            ).pack(side="left", padx=20, pady=(0, 10))        
            Label(
                partido_container_frame,
                text=f"Partida {self.partida + 1}",
                font=("Consolas", 16, "bold"),
                bg="white",
                fg="#888",
                anchor="w",
            ).pack(side="left", padx=20, pady=(0, 10))
            RoundedButton(
                partido_container_frame,
                text=">",
                font=("Consolas", 30),
                fg="#9FACE8",
                bg="white",
                command=lambda : self.control(),
                width=50,
            ).pack(side="left", padx=20, pady=(0, 10))    
        else:
            Label(
                partido_container_frame,
                text=f"Partida Final",
                font=("Consolas", 16, "bold"),
                bg="white",
                fg="#888",
                anchor="w",
            ).pack(side="left", padx=20, pady=(0, 10))
        #Pa que complicarse si se pueden crear más frames ;)
        nombres_frame = Frame(data_frame, bg="white")
        nombres_frame.pack()
        #Buen text bro
        #wtf pq se guarda diferente cuando equipo o jugador ?????????

        
        npartidos = len(self.torneo["rondas"][self.ronda][self.partida])
        if(npartidos > 1):            
            nombre1 = partidos[0]["nombre"]
            nombre2 = partidos[1]["nombre"]        
        elif(npartidos > 0):            
            nombre1 = partidos[0]["nombre"]
            nombre2 = "Por definirse"            
        else:
            nombre1 = nombre2 = "Por definirse"            
        
             
        RoundedButton(
            nombres_frame,
            text=nombre1,
            width=250,
            height=250,
            radius=18,
            font=("Consolas", 13, "bold"),
            bg="#efb810" if (len(partidos) == 3 and partidos[2] is not None) and (partidos[2] == partidos[0]["id"]) else "#888aaa" if (len(partidos) == 3 and partidos[2] is None) else "#888",
            fg="white",
            hover_bg="#efb810",
            command=lambda : self.set_ganador(partidos[0]) if len(self.torneo["rondas"][self.ronda][self.partida]) > 2 else None
        ).pack(side="left")
        Label(
            nombres_frame,
            text="Vs",
            font=("Consolas", 22, "bold"),
            bg="white",
            fg="#1A1832",            
            anchor="w",
        ).pack(side="left", padx=125, pady=(30, 6))
        RoundedButton(
            nombres_frame,
            text=nombre2,
            width=250,
            height=250,
            radius=18,
            font=("Consolas", 13, "bold"),
            bg="#efb810" if (len(partidos) == 3 and partidos[2] is not None) and (partidos[2] == partidos[1]["id"]) else "#888aaa" if (len(partidos) == 3 and partidos[2] is None) else "#888",
            hover_bg="#efb810",
            fg="white",
            command=lambda : self.set_ganador(partidos[1]) if len(self.torneo["rondas"][self.ronda][self.partida]) > 2 else None      
        ).pack(side="left")

        RoundedButton(
            data_frame,
            text="Guardar",
            width=320,
            height=44,
            radius=18,
            font=("Consolas", 13, "bold"),
            command=self.guardar
        ).pack()
        
        # Label(
        #     data_frame,
        #     text=f"{self.ronda + 1}° Ronda",
        #     font=("Consolas", 14, "bold"),
        #     bg="white",
        #     fg="#1A1832",
        #     anchor="w",
        # ).grid(row=0, column=1, sticky="NSEW")

        # 
        # 
        # 
        # 
        # 
        # 
        # 
        # 
        # 
        # 
        # 
        # 
        # 
        # 
        # 
        # 
        # 
        # 


