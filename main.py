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
from tkinter import ttk
from tkinter import font
from datetime import datetime
import torneos_gestion


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

def set_torneo_main():
    if(len(torneo_view.grid_info()) == 0):
        #AGREGAR UN GRID_REMOVE DE LAS OTRAS VIEW POR FAVOR GRACIAS SALUDOS
        torneo_view.grid(column=0, row=0, sticky="NSEW")        
    else:
        torneo_view.grid_remove()


def set_crear_torneo():
    agregar_torneo_button.grid_remove()
    historial_torneo_button.grid_remove()
    n = 0
    for x in range(len(agregar_torneo_vars)):
        agregar_torneo_textos[x].grid(column=0, row=n)
        agregar_torneo_entrys[x].grid(column=1, row=n)
        n+=1
    crear_torneo_button.grid(column=2, row=n)

def validar_formato_fecha(fecha : str):
    if(len(fecha) <= 0):
        pass
    if(fecha.count("/") < 1): #Se puede hacer por separado pero pq me dieron ganas asi
        pass
        
    fecha = fecha.split("/")
    if(len(fecha[1]) < 2): #Arreglando por si solo puso 25/6/2025 ejemplo
        fecha[1] = '0' + fecha[1]    

    fecha = str.join("/", fecha)

def push_torneo_database(ops : list):
    datos_manejables = []
    for x in ops:
        datos_manejables.append(x.get())

    if(datos_manejables[1] == "(...)"): #Son las 12AM tengo hueva de hacer las dialogwindows con los warnings/errores
        pass

    validar_formato_fecha(datos_manejables[2])
    validar_formato_fecha(datos_manejables[3])
   
        
    f_1 = datetime.strptime(datos_manejables[2], "%d/%m/%Y")
    f_2 = datetime.strptime(datos_manejables[3], "%d/%m/%Y")
    
    if(f_2 < f_1): #el inicio es despues del fin xd????
        pass
    
    if(not datos_manejables[-1].isdecimal()): #ver si es numero      
        pass

    datos_manejables[-1] = int(datos_manejables[-1]) #equipos de 0 personas epicos
    if(datos_manejables[-1] < 1):
        pass
    
    #Despues de esto ya se sube estos datos a la base de datos shocked @20220270

root = Tk()
root.title("KeyPlayer Manager")
root.configure(bd=2, highlightthickness=2)
root.geometry("720x576+0+0")
root.resizable(False, False)
root.overrideredirect(True)

font.Font(family="Roman", name="customFont", size=12)



color_boton = "#FFC174"

titlebar = Frame(root, width=720, height=20, bg="white", bd=3, relief="raised")
slider = Frame(root,  bg="#3DADFF", bd=1, relief="groove", highlightcolor="#34A1EF")
interac = Frame(root, bg="white")


torneo_view = Frame(interac, background="white")


agregar_torneo_button = Button(torneo_view, relief="sunken", text="CREAR TORNEO", bd=0, background=color_boton, font="customFont", command=set_crear_torneo)
historial_torneo_button = Button(torneo_view, relief="sunken", text="HISTORIAL DE TORNEOS", bd=0, background=color_boton, font="customFont")

agregar_torneo_button.grid(column=0, row=0,sticky="NWE")
historial_torneo_button.grid(column=1, row=0, sticky="NWE")

agregar_torneo_textos = [
    Label(torneo_view, text="Nombre del Torneo:", font="customFont", justify="center", background="white"),
    Label(torneo_view, text="Juego: ", font="customFont", justify="center", background="white"),
    Label(torneo_view, text="Fecha de inicio", font="customFont", justify="center", background="white"),
    Label(torneo_view, text="Fecha de fin", font="customFont", justify="center", background="white"),
    Label(torneo_view, text="N° de Personas por equipo:", font="customFont", wraplength=150, justify="center", background="white"),
]


agregar_torneo_vars = [
    StringVar(),
    StringVar(),
    StringVar(),
    StringVar(),
    StringVar()
]

def cargar_videojuegos():
    resultados = torneos_gestion.ver_videojuegos()
    nombres = [r[1] for r in resultados]  # Solo los nombres, sin los IDs
    menu = agregar_torneo_entrys[1]["menu"]
    menu.delete(0, "end")  # Limpia opciones anteriores

    # Añadimos cada nuevo nombre
    for nombre in nombres:
        menu.add_command(label=nombre, command=lambda v=nombre: agregar_torneo_vars[1].set(v))
    
    agregar_torneo_vars[1].set("(Selecciona un juego)")

# Inicializa la variable con un valor por defecto
agregar_torneo_vars[1].set("(Selecciona un juego)")

# Luego crea el OptionMenu una sola vez (con valores vacíos al principio)
agregar_torneo_entrys = [
    Entry(torneo_view, textvariable=agregar_torneo_vars[0]),
    OptionMenu(torneo_view, agregar_torneo_vars[1], ""),
    Entry(torneo_view, textvariable=agregar_torneo_vars[2]),
    Entry(torneo_view, textvariable=agregar_torneo_vars[3]),
    Entry(torneo_view, textvariable=agregar_torneo_vars[4])
]

crear_command = lambda : push_torneo_database(agregar_torneo_vars)
crear_torneo_button = Button(torneo_view, relief="sunken", text="CREAR", bd=0, background=color_boton, font="customFont", command=crear_command)


titlebar.pack()
slider.pack(anchor="nw", fill="both", side="left")
interac.pack(anchor="ne", fill="both", side="right", expand=True)
# titlebar.grid(column=0, row=0, columnspan=2, sticky="NSEW")
# slider.grid(column=0, row=1, sticky="NS")
# interac.grid(column=1, row=1, sticky="NSEW")

titlebar.bind("<B1-Motion>", move_window)
titlebar.bind("<B1-ButtonRelease>", reset_mouse_pos)

text_titlebar = Label(titlebar, text="KeyPlayer Manager")
text_titlebar.configure(background="white")
text_titlebar.grid(column=0, row=0, columnspan=2, padx=300)

text_titlebar.bind("<B1-Motion>", move_window)
text_titlebar.bind("<B1-ButtonRelease>", reset_mouse_pos)


close_button = Button(titlebar, text=" X ", foreground="black", background="white", relief="sunken", command=root.destroy, bd=0, activebackground="red")
close_button.grid(column=1, row=0, sticky="NES")
close_button.bind("<Enter>", hover_closebutton)
close_button.bind("<Leave>", unhover_closebutton)

logo_torneo = PhotoImage(file="images/control_logo_mini.png")
logo_equipo = PhotoImage(file="images/equipo_logo_mini.png")
logo_jugador = PhotoImage(file="images/jugador_logo_mini.png")

torneos_button = Button(slider, text="TORNEOS", image=logo_torneo, compound="right", background="#3DADFF", relief="flat", command=set_torneo_main, font="customFont")
equipos_button = Button(slider, text="EQUIPOS", image=logo_equipo, compound="right", background="#3DADFF", relief="flat", font="customFont")
jugadores_button = Button(slider, text="JUGADORES", image=logo_jugador, compound="right", background="#3DADFF", relief="flat", font="customFont")


torneos_button.grid(column=0, row=1, sticky="NSEW")
equipos_button.grid(column=0, row=2, sticky="NSEW")
jugadores_button.grid(column=0, row=3, sticky="NSEW")

version = Label(slider, text="version 1.0.9", background="#3DADFF", relief="flat", font="customFont")
version.grid(column=0, row=4,sticky="SW")
cargar_videojuegos()


root.mainloop()