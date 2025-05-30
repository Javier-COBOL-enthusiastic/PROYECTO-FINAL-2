"""
REGISTRO DE JUGADORES / EQUIPOS

#ID = str (pero para que quede mas bonito y se diferencie ID xD)


JUGADOR ->
USERNAME -> str
POR JUEGO ELO -> dict (ID : int)

EQUIPOS
TEAM NAME -> str
JUGADORES -> list (JUGADORES)
POR JUEGO ELO -> dict (ID : int (PROMEDIO DE JUGADORES ?)

PARTIDA
JUEGO -> ID
TIPO -> EQUIPO VS EQUIPO / JUGADOR VS JUGADOR
ESTADO -> FINALIZADO, POR JUGARSE, EN JUEGO
RESULTADO -> (SOLO CUANDO ESTE FINALIZADO) ~ (AGREGAR FORMA DE ACTUALIZAR DURANTE LA PARTIDA (DIFICIL))

TORNEO
NOMBRE -> str
FASES -> dict -> ("FASE DE GRUPOS" : list (PARTIDOS))
ESTADO -> FINALIZADO, EN PROGRESO, POR INICIAR?
RESULTADO -> (SOLO CUANDO ESTE FINALIZADO (ES DECIR EL GANADOR))

EMPAREJAMIENTO AUTOMATICO

SEGUN PARTIDA GANADA O PERDIDA -> SUMAR O RESTAR ELO (JUGADOR/EQUIPO)
BUSCAR EN UN RANGO DE (ELO + 50) SI NO SE ENCUENTRA AUMENTAR RANGO POR 25, SI ELO DEL CONTRICANTE ES 200 PUNTOS MAYOR A EL JUGADOR
SE DEJA EN MANOS DEL USUARIO

REGISTRO DE RESULTADO

INCLUIDO EN LA PARTE DE PARTIDA

VISUALIZACIÓN DEL PROGRESO


MOSTRAR UN TIPO "ARBOL" CON EL PROGRESO DEL TORNEO
"""

def hover_closebutton(e):
    close_button["background"] = "red"
def unhover_closebutton(e):
    close_button["background"] = "white"

def move_window(e):
    root.geometry(f"+{e.x_root}+{e.y_root}")

from tkinter import *
from tkinter import ttk
root = Tk()
root.title("KeyPlayer Manager")
root.configure(bd=2, highlightthickness=2)
root.resizable(False, False)
root.overrideredirect(True)

titlebar = Frame(root, width=720, height=20, bg="white", bd=3, relief="raised")
slider = Frame(root, width=200, height=576, bg="#3DADFF", bd=1, relief="groove", highlightcolor="#3DADFF")
interac = Frame(root, width=520, height=576, bg="white", relief="flat")



titlebar.grid(column=0, row=0, columnspan=2, sticky="WNSE")
slider.grid(column=0, row=1, sticky="NWSE")
interac.grid(column=1, row=1, sticky="NSWE")

titlebar.bind("<B1-Motion>", move_window)

text_titlebar = Label(titlebar, text="KeyPlayer Manager")
text_titlebar.configure(background="white")
text_titlebar.grid(column=0, row=0, columnspan=2, padx=300)



close_button = Button(titlebar, text=" X ", foreground="black", background="white", relief="sunken", command=root.destroy, bd=0, activebackground="red")
close_button.grid(column=1, row=0, sticky="NES")
close_button.bind("<Enter>", hover_closebutton)
close_button.bind("<Leave>", unhover_closebutton)


torneos_button = Button(slider, text="TORNEOS", background="#3DADFF", relief="flat")
equipos_button = Button(slider, text="EQUIPOS", background="#3DADFF", relief="flat")
jugadores_button = Button(slider, text="JUGADORES", background="#3DADFF", relief="flat")

logo_torneo = PhotoImage(file="images/control_logo.png")
logo_equipo = PhotoImage(file="images/equipo_logo.png")
logo_jugador = PhotoImage(file="images/jugador_logo.png")



torneo_logo = Label(slider, image=logo_torneo, background="#3DADFF")
equipo_logo = Label(slider, image=logo_equipo, background="#3DADFF")
jugador_logo = Label(slider, image=logo_jugador, background="#3DADFF")

torneos_button.grid(column=0, row=1)
torneo_logo.grid(column=1, row=1)

equipos_button.grid(column=0, row=2)
equipo_logo.grid(column=1, row=2)

jugadores_button.grid(column=0, row=3)
jugador_logo.grid(column=1, row=3)




root.mainloop()









    
        
