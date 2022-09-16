"""
Clase con encapsulamiento
"""
class Persona:
    #Atributos privados(__)
    __nombre = None
    __edad = None
    #Constructor
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
    #Metodo privado    
    def __metodo_privado(self):
        print('Soy un método privado')
    #Getter y Setter    
    def get_nombre(self):
        return self.__nombre
    def set_nombre(self, nombre):
        self.__nombre = nombre
    def get_edad(self):
        return self.__edad
    def set_edad(self, edad):
        self.__edad = edad
    #Estado del objeto    
    def __str__(self):
        return f'Nombre: {self.__nombre} \nEdad: {self.__edad}' 
        