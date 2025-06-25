"""
Modelo de datos para la entidad Torneo
Este módulo contiene la clase Torneo y las excepciones personalizadas
para validar los datos de un torneo antes de su creación.
"""

from datetime import datetime
import re
from ui.elements import GUIEntry

class NombreInvalido(Exception):
    """
    Excepción que se lanza cuando el nombre del torneo está vacío o es inválido
    """
    def __init__(self):
        pass

class FormatoFechaInvalido(Exception):
    """
    Excepción que se lanza cuando el formato de fecha no es válido (dd/mm/yyyy)
    """
    def __init__(self):
        pass        

class FechaInvalida(Exception):
    """
    Excepción que se lanza cuando las fechas no son lógicas (fecha fin antes que inicio)
    """
    def __init__(self):
        pass

class JuegoInvalido(Exception):
    """
    Excepción que se lanza cuando no se selecciona un juego para el torneo
    """
    def __init__(self):
        pass    

class Torneo:    
    """
    Clase que representa un torneo en el sistema
    Se encarga de validar todos los datos del torneo antes de su creación
    """
    
    def __init__(self, data : GUIEntry):
        """
        Constructor de la clase Torneo
        
        Args:
            data (GUIEntry): Objeto que contiene los datos del formulario del torneo
            
        Raises:
            NombreInvalido: Si el nombre está vacío
            JuegoInvalido: Si no se selecciona un juego
            FormatoFechaInvalido: Si el formato de fecha es incorrecto
            FechaInvalida: Si las fechas no son lógicas
            ValueError: Si el número de equipos no es válido
        """
        # Obtener los datos limpios del formulario
        self.clean_data = data.get()
        # Limpiar el formato del juego (remover caracteres extra)
        self.clean_data[1] = self.clean_data[1][2:-4]
        print(self.clean_data)     
        
        # Validar que el nombre no esté vacío
        if(len(self.clean_data[0]) == 0):
            raise NombreInvalido

        # Validar que se haya seleccionado un juego
        if(len(self.clean_data[1]) == 0):
            raise JuegoInvalido

        # Validar formato de fechas
        try:
            self.__valid_format__(self.clean_data[2])
            self.__valid_format__(self.clean_data[3])
        except:
            raise FormatoFechaInvalido
        
        # Convertir fechas a objetos datetime para validación
        f_1 = datetime.strptime(self.clean_data[2], "%d/%m/%Y")
        f_2 = datetime.strptime(self.clean_data[3], "%d/%m/%Y")
        
        # Validar que la fecha de fin no sea anterior a la de inicio
        if(f_2 < f_1):
            raise FechaInvalida
            
        # Validar que el número de equipos sea un número válido
        if(not self.clean_data[-1].isdecimal()):
            raise ValueError

        # Convertir a entero y validar que sea mayor a 0
        self.clean_data[-1] = int(self.clean_data[-1])
        if(self.clean_data[-1] < 1):
            raise ValueError
    
    
    def __valid_format__(self, fecha : str):
        """
        Método privado para validar el formato de fecha
        
        Args:
            fecha (str): Fecha en formato string
            
        Raises:
            FechaInvalida: Si la fecha está vacía
            FormatoFechaInvalido: Si el formato no es válido
        """
        # Validar que la fecha no esté vacía
        if(len(fecha) <= 0):
            raise FechaInvalida
        # Validar que contenga al menos un separador "/"
        if(fecha.count("/") < 1):
            raise FormatoFechaInvalido
            
        # Normalizar formato de fecha (agregar ceros si es necesario)
        fecha = fecha.split("/")
        if(len(fecha[0]) < 2):
            fecha[0] = '0' + fecha[0]    
        if(len(fecha[1]) < 2):
            fecha[1] = '0' + fecha[1]                
        fecha = str.join("/", fecha)
                