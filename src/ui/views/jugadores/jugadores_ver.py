from tkinter import *
from ui.elements import TableView, TableActionButton
from ui.mocks import get_torneos, get_equipos
from datetime import datetime


class JugadorFormViewNoEdit:
    def __init__(self, parent, jugador):
        frame = Frame(parent, bg="#EDEDED")
        frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        header_bg = Frame(frame, bg="#F6F6F6")
        header_bg.pack(fill="x", padx=0, pady=(0, 0))
        titulo = f"Historal de {jugador['nombre']}"
        Label(
            header_bg,
            text=titulo,
            font=("Consolas", 28, "bold"),
            bg="#F6F6F6",
            fg="#222",
            anchor="w",
        ).pack(fill="x", padx=60, pady=(36, 18))

        Frame(frame, height=18, bg="#EDEDED").pack()

        table_card_w, table_card_h = 980, 380
        table_card_container = Frame(
            frame, bg="#EDEDED", width=table_card_w, height=table_card_h
        )
        table_card_container.pack(
            anchor="n", padx=40, pady=(0, 0), fill=None, expand=False
        )
        

       
        headers = ["ID", "Torneo", "Inicio", "Fin", "Estado", "Resultado"]


        torneos = get_torneos()
        
        equipos = get_equipos()

        equipo_part = []
        equipos_id = []

        for equipo in equipos:
            for jug in equipo["jugadores"]:
                if jug["id_jugador"] == jugador["id"]:
                    equipo_part.append(equipo)
                    equipos_id.append(equipo["id"])
        
        torneo_part = []
        for torneo in torneos:
            for partida in torneo["rondas"][0]:
                if((partida[0] in equipo_part or partida[0]["id"] == jugador["id"]) or (partida[1] in equipo_part or partida[1]["id"] == jugador["id"])):
                    torneo_part.append(torneo)

        data = []

        actual = datetime.now()
        cmp = datetime(actual.year, actual.month, actual.day)

        for torneo in torneo_part:
            a = torneo["inicio"]
            b = torneo["fin"]
            f_1 = datetime.strptime(a, "%d/%m/%Y")            
            f_2 = datetime.strptime(b, "%d/%m/%Y")
            
            estado = ""
            res_jg = ""
            if(f_1 <= cmp and f_2 >= cmp and not(len(torneo["rondas"][-1][0]) == 3 and torneo["rondas"][-1][0][2] != None)):
                estado = "Iniciado"                                

            elif(len(torneo["rondas"][-1][0]) == 3 and torneo["rondas"][-1][0][2] != None):
                estado = "Finalizado"

                if(torneo["rondas"][-1][0][0].get("jugadores") != None and torneo["rondas"][-1][0][2] in equipos_id):
                    res_jg = "Ganador"
                elif(torneo["rondas"][-1][0][0].get("jugadores") == None and torneo["rondas"][-1][0][2] == jugador["id"]):
                    res_jg = "Ganador"
                else:
                    res_jg = "Perdedor"

            else:
                estado = "Pendiente"


            if(res_jg != ""):
                data.append([torneo["id"], torneo["nombre"], torneo["inicio"], torneo["fin"], estado, res_jg])
                continue
            
            for ronda in torneo["rondas"]:
                for partida in ronda:
                    if(len(partida) < 3 and res_jg != "Perdedor"):
                        res_jg = "Por definirse"
                        break
                    if not((partida[0] in equipo_part or partida[0]["id"] == jugador["id"]) or (partida[1] in equipo_part or partida[1]["id"] == jugador["id"])):
                        continue
                    if(len(partida[0]) == 1 and partida[2] == j["id"] for j in equipo_part):
                        res_jg = "Por definirse"
                    elif(len(partida[0]) != 1 and partida[2] == jugador["id"]):
                        res_jg = "Por definirse"
                    else:
                        res_jg = "Perdedor"
                        break

            data.append([torneo["id"], torneo["nombre"], torneo["inicio"], torneo["fin"], estado, res_jg])

        # data = [
        #     [f"{i:02}", f"Torneo {i}", "01/01/24", "05/01/24", "Pendiente", "Ganador" if i % 2 else "Perdedor"]
        #     for i in range(1, 10)
        # ]    

        col_widths = [60, 150, 100, 100, 130, 220]

        table = TableView(
            table_card_container,
            headers,
            data,            
            title="Torneos participados",
            count=len(data),                        
            card_w=table_card_w,
            card_h=table_card_h,
            col_widths=col_widths,            
            anchor_cols="center",
        )
        table.pack(padx=0, pady=(10, 0), fill="both", expand=True)
        