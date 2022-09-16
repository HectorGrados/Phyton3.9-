"""
Funciones de cadena
"""
#Funcion upper = Todo a mayuscula
hola='Hola mundo'.upper()
print(hola)
#Funcion lower = Todo a minuscula
hola='Hola mundo'.lower()
print(hola)
#Funcion capitalize = Tipo oracion
hola='Hola mundo'.capitalize()
print(hola)
#Funcion title = Tipo titulo
hola='Hola mundo'.title()
print(hola)
#Funcion count = Cuenta la cantidad de caracteres hay en la cadena
hola='Hola mundo'.count('o')
print(hola)
#Funcion replace = reemplaza caracteres 
palabra = 'Python'
palabra = palabra.replace('P','S')
print(palabra)
#Funcion replace = reemplaza espacios
palabra= 'P y t h o n'.replace(' ','')
print(palabra)
#Funcion strip = elimina espacios
mundo='  Hola Mundo  '.strip()
print(mundo)
#Funcion strip = elimina elementos especificos
mundo='--------Hola -- Mundo------'.strip('-')
print(mundo)
#Funcion split = convierte a lista
mundo='Hola Mundo'.split()
print(mundo)
#Funcion split = convierte a lista
mundo='Hola,Mundo,de,python'.split(',')
print(mundo)
#Funcion islower = verifica si es pura minuscula
hola='Hola'.islower()
print(hola)
#Funcion isupper = verifica si es pura mayuscula
hola='HOLA'.isupper()
print(hola)