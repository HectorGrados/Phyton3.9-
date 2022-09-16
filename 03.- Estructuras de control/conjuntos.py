"""
Conjuntos en python
"""
#Conjunto
a=set()
#Definir conjunto
a={'a','b','c'}
print(a)
#Definir repetido
a={'a','b','c','a'}
print(a)
#Convertir caracter a conjunto
a=set('abracadabra')
print(a)
#Conjunto con operadores
a=set('abracadabra')
b=set('alacazam')
print(a-b) #Resta
print(a|b) #Letras en ambas
print(a&b) #Letras que esta en  a y b
print(a^b) #Letras en a o b pero no en ambas
#Agregar
a={'a','b','c'}
a.add('d')
print(a)
#Eliminar un elemento
a.discard('b')
print(a)
#Eliminar conjunto
a.clear()
print(a)