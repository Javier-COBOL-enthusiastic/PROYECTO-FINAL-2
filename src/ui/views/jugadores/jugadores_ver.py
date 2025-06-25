from tkinter import *
from ui.elements import TableView, TableActionButton


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

        data = [
            [f"{i:02}", f"Torneo {i}", "01/01/24", "05/01/24", "Pendiente", "Ganador" if i % 2 else "Perdedor"]
            for i in range(1, 10)
        ]    

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
        