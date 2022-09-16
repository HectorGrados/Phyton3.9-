"""
Creando objetos
"""
from persona import Persona
#Primer objeto
persona1 = Persona('Hector', 18)
#Modificar el nombre
persona1.nombre = 'Blaze'
#Modificar edad
persona1.edad = 19
#Mostrar en pantalla
persona1.mostra_datos()

#Segundo objeto
persona2 = Persona('Emanuel', 20)
#Modificar el nombre
persona2.nombre = 'Grados'
#Modificar edad
persona2.edad = 21
#Mostrar en pantalla
persona2.mostra_datos()

#Funcion para mostrar el estado del objeto
print(persona1)