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

 # Mostrar un frame para Equipos
def mostrar_equipos():
    # Limpiamos el contenido actual del frame interac
    for widget in interac.winfo_children():
        widget.destroy()

    # Creamos un nuevo contenido para la sección de equipos
    Label(interac, text="Gestión de Equipos", font=("Arial", 16, "bold"), bg="white").pack(pady=20)


close_button = Button(titlebar, text=" X ", foreground="black", background="white", relief="sunken", command=root.destroy, bd=0, activebackground="red")
close_button.grid(column=1, row=0, sticky="NES")
close_button.bind("<Enter>", hover_closebutton)
close_button.bind("<Leave>", unhover_closebutton)

logo_torneo = PhotoImage(file="images/control_logo.png")
logo_equipo = PhotoImage(file="images/equipo_logo.png")
logo_jugador = PhotoImage(file="images/jugador_logo.png")

torneos_button = Button(slider, text="TORNEOS", image=logo_torneo, compound="right", background="#3DADFF", relief="flat")
equipos_button = Button(slider, text="EQUIPOS", image=logo_equipo, compound="right", background="#3DADFF", relief="flat", command=mostrar_equipos)
jugadores_button = Button(slider, text="JUGADORES", image=logo_jugador, compound="right", background="#3DADFF", relief="flat")


torneos_button.grid(column=0, row=1, columnspan=10, pady=5)
equipos_button.grid(column=0, row=2, columnspan=10, pady=5)
jugadores_button.grid(column=0, row=3, columnspan=10, pady=5)

root.mainloop()