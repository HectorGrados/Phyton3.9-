"""
Clase persona
"""
class Persona:
    #Constructor
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    #Funcion mostrar
    def mostra_datos(self):
        print('Nombre: ', self.nombre)
        print('Edad: ', self.edad)
    #Funcion para mostrar el estado del objeto
    def __str__(self):
        return f'Nombre: {self.nombre} \nEdad: {self.edad}'