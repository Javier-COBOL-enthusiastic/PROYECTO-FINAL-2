from datetime import datetime
import re
from ui.elements import GUIEntry

class NombreInvalido(Exception):
    def __init__(self):
        pass

class FormatoFechaInvalido(Exception):
    def __init__(self):
        pass        

class FechaInvalida(Exception):
    def __init__(self):
        pass

class JuegoInvalido(Exception):
    def __init__(self):
        pass    

class Torneo:    
    def __init__(self, data : GUIEntry):
        self.clean_data = data.get()
        self.clean_data[1] = self.clean_data[1][2:-4]
        print(self.clean_data)     
        
        #toca agregar algo pa ver si el nombre no es repetido?? @20220270
        if(len(self.clean_data[0]) == 0):
            raise NombreInvalido


        if(len(self.clean_data[1]) == 0): #Son las 12AM tengo hueva de hacer las dialogwindows con los warnings/errores
            raise JuegoInvalido


        try:
            self.__valid_format__(self.clean_data[2])
            self.__valid_format__(self.clean_data[3])
        except:
            raise FormatoFechaInvalido
        
        f_1 = datetime.strptime(self.clean_data[2], "%d/%m/%Y")
        f_2 = datetime.strptime(self.clean_data[3], "%d/%m/%Y")
        
            

    
        if(f_2 < f_1): #el inicio es despues del fin xd????
            raise FechaInvalida
            
        if(not self.clean_data[-1].isdecimal()): #ver si es numero      
            raise ValueError

        self.clean_data[-1] = int(self.clean_data[-1]) #equipos de 0 personas epicos
        if(self.clean_data[-1] < 1):
            raise ValueError
    
    
    def __valid_format__(self, fecha : str):        
        if(len(fecha) <= 0):
            raise FechaInvalida
        if(fecha.count("/") < 1): #Se puede hacer por separado pero pq me dieron ganas asi
            raise FormatoFechaInvalido
            
        fecha = fecha.split("/")#Arreglando por si solo puso 1/6/2025 ejemplo
        if(len(fecha[0]) < 2):
            fecha[0] = '0' + fecha[0]    
        if(len(fecha[1]) < 2): #Arreglando por si solo puso 25/6/2025 ejemplo
            fecha[1] = '0' + fecha[1]                
        fecha = str.join("/", fecha)
                