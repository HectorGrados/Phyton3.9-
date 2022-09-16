"""
Aplicación 04:
-Crear una función lambda que realice la suma de dos números
-Crea una función lambda que duplique un numero
-Crear funciones landa que detecte si un número es par y otro para detectar si es impar.
-Crea una función lambda que invierta una cadena de caracteres.
"""
#Funcion lambda Sumar
sumar = lambda a,b:a+b
#Funcion lambda Publicar un numero
doblar = lambda n: n * 2
#Funcion lambda Par
par = lambda n: n % 2 == 0
#Funcion lambda Impar
impar = lambda n: n%2 != 0
#Funcion lambda Invertir cadena
revertir = lambda cadena: cadena[::-1]
#Salida de Datos
print(sumar(10, 20))
print(doblar(10))
print(par(5))
print(impar(5))
print(revertir('hola')) 
