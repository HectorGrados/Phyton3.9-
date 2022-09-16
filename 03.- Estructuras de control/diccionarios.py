"""
Diccionarios en python
"""
#Diccionarios
numeros = {}
print(numeros)
#Agregando clave y valor
numeros={'uno':1 , 'dos':2 , 'tres':3 , 'cuatro':4}
print(numeros)
#Valor de la clave
print(numeros['uno'])
#Agregar
numeros['cinco']=5
print(numeros)
#Buscar un valor con clave
print(numeros.get('cuatro','No se encontro'))
#Imprimir todas las claves
print(numeros.keys())
#Imprimir todos los valores
print(numeros.values())
#Imprimir clave y valor
print(numeros.items())
#Eliminar
numeros.pop('cinco','No se encontro')
print(numeros)
#Eliminar diccionario
numeros.clear()
print(numeros)
#Iterar diccionario (clave)
numeros={'uno':1 , 'dos':2 , 'tres':3 , 'cuatro':4}
for numero in numeros:
    print(numero)
#Iterar diccionario (valores)
numeros={'uno':1 , 'dos':2 , 'tres':3 , 'cuatro':4}
for numero in numeros.values():
    print(numero)    
#Iterar diccionario (valores) (clave)
numeros={'uno':1 , 'dos':2 , 'tres':3 , 'cuatro':4}
for clave,valor in numeros.items():
    print(clave,valor)    

