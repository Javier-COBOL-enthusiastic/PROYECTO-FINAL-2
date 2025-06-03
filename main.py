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
from tkinter import *
from tkinter import messagebox
from tkinter import font

from torneos_gestion import *
from torneo import *

from Elements import *

def hover_closebutton(e):
    close_button["background"] = "red3"
def unhover_closebutton(e):
    close_button["background"] = "white"

mouse_x = -1 
mouse_y = -1 
def move_window(e):
    global mouse_x
    global mouse_y
    if(mouse_x == -1 and mouse_y == -1):
        mouse_x = e.x_root
        mouse_y = e.y_root
        return
    
    a = list(map(lambda x : int(x), root.winfo_geometry().split("+")[-2:]))    
    dst_x = (e.x_root - mouse_x) + a[0]
    dst_y = (e.y_root - mouse_y) + a[1]

    root.geometry(f"+{dst_x}+{dst_y}")
    mouse_x = e.x_root
    mouse_y = e.y_root

def reset_mouse_pos(e):
    global mouse_x
    global mouse_y
    mouse_y = mouse_x = -1    

def set_main(who : Frame):
    views = [torneo_view, jugadores_view]
    views.pop(views.index(who))
    if(len(who.grid_info()) == 0):
        for frame in views:
            frame.grid_remove()
        who.grid(column=0, row=0, sticky="NSEW")
    else:
        who.grid_remove()


def crear_torneo():
    global torneos
    global creacion_torneo_GUI

    try:
        res = Torneo(creacion_torneo_GUI)
        torneos.append(res)
        messagebox.showinfo("Exito!", "El torneo ha sido creado con exito!")    
        creacion_torneo_GUI.clear()
    except ValueError: messagebox.showerror(title="N° de Jugadores por Equipo Invalido", message="El numero de jugadores por equipo menor o igual que 0...")
    except FechaInvalida: messagebox.showerror(title="Fecha invalida", message="La fecha de fin es antes que la fecha de fin...")
    except FormatoFechaInvalido: messagebox.showerror(title="Formato de fecha invalido", message="El formato de la fecha es invalido, formato valido: DD/MM/YYYY")        
    except JuegoInvalido: messagebox.showerror(title="Juego invalido", message="El juego seleccionado es invalido")     
    except NombreInvalido: messagebox.showerror(title="Nombre invalido", message="El nombre del torneo es invalido")     


#/----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------/

root = Tk()
root.title("KeyPlayer Manager")
root.configure(bd=2, highlightthickness=2)
root.geometry("720x576+0+0")
root.resizable(False, False)
root.overrideredirect(True)

font.Font(family="Roman", name="customFont", size=12)



color_boton = "#FFC174"

#/----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------/

titlebar = Frame(root, width=720, height=20, bg="white", bd=3, relief="raised")
titlebar.bind("<B1-Motion>", move_window)
titlebar.bind("<B1-ButtonRelease>", reset_mouse_pos)

text_titlebar = Label(titlebar, text="KeyPlayer Manager")
text_titlebar.configure(background="white")

text_titlebar.bind("<B1-Motion>", move_window)
text_titlebar.bind("<B1-ButtonRelease>", reset_mouse_pos)


close_button = Button(titlebar, text=" X ", foreground="black", background="white", relief="sunken", command=root.destroy, bd=0, activebackground="red")
close_button.bind("<Enter>", hover_closebutton)
close_button.bind("<Leave>", unhover_closebutton)

text_titlebar.grid(column=0, row=0, columnspan=2, padx=300)
close_button.grid(column=1, row=0, sticky="NES")
titlebar.pack()

#/----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------/

slider = Frame(root,  bg="#3DADFF", bd=1, relief="groove", highlightcolor="#34A1EF")
interac = Frame(root, bg="white")
slider.pack(anchor="nw", fill="both", side="left")
interac.pack(anchor="ne", fill="both", side="right", expand=True)

#/----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------/

torneo_view = Frame(interac, background="white")
set_torneo_view = lambda : set_main(torneo_view)

logo_torneo = PhotoImage(file="images/control_logo_mini.png")
torneos_button = Button(slider, text="TORNEOS", image=logo_torneo, compound="right", background="#3DADFF", relief="flat", command=set_torneo_view, font="customFont")

agregar_torneo_button = Button(torneo_view, text="Crear", command=crear_torneo)

opciones_creacion_torneo = {"Nombre del Torneo:" : "ENTRY", 
        "Juego:" : "OPTIONMENU",
        "Fecha de inicio:" : "ENTRY",
        "Fecha de fin:" : "ENTRY",  
        "N° de Personas por equipo:" : "ENTRY"}

creacion_torneo_GUI = GUIEntry(torneo_view, 1, **opciones_creacion_torneo)

juegos = [x[1] for x in ver_videojuegos()]
creacion_torneo_GUI.load_option_menu("Juego:", juegos)

creacion_torneo_GUI.show()

torneos = []

agregar_torneo_button.grid(column=0, row=0)
torneos_button.grid(column=0, row=1, sticky="NSEW")

#/----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------/


jugadores_view = Frame(interac, background="white")
set_jugadores_view = lambda : set_main(jugadores_view)

logo_jugador = PhotoImage(file="images/jugador_logo_mini.png")
jugadores_button = Button(slider, text="JUGADORES", image=logo_jugador, compound="right", background="#3DADFF", relief="flat", font="customFont", command=set_jugadores_view)

jugadores_texto = ["ID", "JUGADOR", "EDAD", "MÁS INFORAMCION"]

info_ver_jugadores =GUIInformation(jugadores_view, jugadores_texto)

info_ver_jugadores.show()
jugadores_button.grid(column=0, row=3, sticky="NSEW")

#/----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------/

logo_equipo = PhotoImage(file="images/equipo_logo_mini.png")
equipos_button = Button(slider, text="EQUIPOS", image=logo_equipo, compound="right", background="#3DADFF", relief="flat", font="customFont")

equipos_button.grid(column=0, row=2, sticky="NSEW")

#/----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------/


version = Label(slider, text="version 1.0.9", background="#3DADFF", relief="flat", font="customFont")
version.grid(column=0, row=4,sticky="SW")

root.mainloop()