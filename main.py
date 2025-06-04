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
from tkinter import ttk

from torneos_gestion import *
from torneo import *

from Elements import *
"""
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
    
    except FechaInvalida: messagebox.showerror(title="Fecha invalida", message="La fecha de fin es antes que la fecha de fin...")
    except FormatoFechaInvalido: messagebox.showerror(title="Formato de fecha invalido", message="El formato de la fecha es invalido, formato valido: DD/MM/YYYY")        
    except JuegoInvalido: messagebox.showerror(title="Juego invalido", message="El juego seleccionado es invalido")     
    except NombreInvalido: messagebox.showerror(title="Nombre invalido", message="El nombre del torneo es invalido")     
"""

#/----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------/

def set_main(who : Frame):
    if(mainmenu.cget("background") == bg1):
        mainmenu.configure(background=bg2)
        mainmenu.pack_configure(padx=0, anchor="nw", side="left", fill="y", after=None)
        close_button.pack_configure(anchor="ne", side="right", expand=True)
        bienvenida.grid_remove()
        logo.grid_configure(column=0, row=0, pady=30)
        logo.configure(background=bg2)
        jugador_button.grid_configure(column=0, row=1, pady=0, sticky="NSEW")
        equipos_button.grid_configure(column=0, row=2, pady=0, sticky="NSEW")
        torneo_button.grid_configure(column=0, row=3, pady=0, sticky="NSEW")
        

    views = [torneo_view, jugadores_view, equipos_view]
    views.pop(views.index(who))    
    for frame in views:
        frame.pack_forget()
    who.pack(side="right")    


root = Tk()
root.title("KeyPlayer Manager")
root.geometry("680x420+0+0")
root.resizable(False, False)
root.overrideredirect(True)

bg1 = "#EDEDED"
bg2 = "#9FACE8"

color_boton = "#688CCA"

bigFont = font.Font(family="Nirmala UI", size=14, weight="bold")
bigFont.config(size=20)

smallFont = font.Font(root, family="Nirmala UI")
smallFont.config(size=12)


font.nametofont("TkHeadingFont").configure(family="Nirmala UI", weight="bold")



mainmenu = Frame(root, background=bg1)
close_button = Button(root, text=" X ", relief="groove", font=smallFont, bg="#EE5454", command=root.destroy)
close_button.pack(anchor="ne")
mainmenu.pack(padx=82, expand=True, anchor="n", after=close_button)


bienvenida = Label(mainmenu, text="Bienvenido a K.E.Y. player manager", font=bigFont)
bienvenida.grid(column=1, row=1, columnspan=3, ipady=50)

foto_logo = PhotoImage(file="images/logo_azul.png")
logo = Label(mainmenu, image=foto_logo)
logo.grid(column=1, row=2, columnspan=3)

torneo_view = Frame(root, background=bg1)
set_torneo_main = lambda : set_main(torneo_view)

crear_torneo_button = Button(torneo_view, text="Crear Torneo", background=color_boton)

torneo_info = GUITable(torneo_view, smallFont,(["id_torneo", "nombre_torneo", "fecha_inicio", "fecha_fin", "estado"], ["ID", "Nombre del Torneo", "Inicio", "Fin", "Estado"]))
torneo_info.configure_width_columns(30, 150, 100, 100, 100)
torneo_info.insert_item("1", "Brazil Vs Key", "03/05/2025", "04/05/2025", "Finalizado")

torneo_info.show()
crear_torneo_button.pack(anchor="nw")

torneo_button = Button(mainmenu, text="Torneo", font=smallFont, relief="groove", bg=color_boton, command=set_torneo_main)
torneo_button.grid(column=1, row=3, pady=50)



equipos_view = Frame(root, background=bg1)
set_equipos_view = lambda : set_main(equipos_view)

equipos_info = GUITable(equipos_view, smallFont, (["id_equipo", "nombre_equipo", "numero_jugadores"], ["ID", "Nombre", "Participantes"]))
equipos_info.configure_width_columns(30, 200, 100)
equipos_info.insert_item("1", "Equipo XD", "5")

equipos_info.show()

equipos_button = Button(mainmenu, text="Equipos", font=smallFont, relief="groove", bg=color_boton, command=set_equipos_view)
equipos_button.grid(column=2, row=3)


jugadores_view = Frame(root, background=bg1)
set_jugadores_view = lambda : set_main(jugadores_view)

jugadores_info = GUITable(jugadores_view, smallFont, (["id_jugador", "nombre_jugador"], ["ID", "Nombre"]))
jugadores_info.configure_width_columns(30, 200)
jugadores_info.insert_item("1", "Yair17")

jugadores_info.show()

jugador_button = Button(mainmenu, text="Jugadores", font=smallFont, relief="groove", bg=color_boton, command=set_jugadores_view)
jugador_button.grid(column=3, row=3)
















root.mainloop()
#/----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------/

