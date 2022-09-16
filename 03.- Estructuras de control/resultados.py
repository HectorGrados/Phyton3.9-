"""
Practica 03:
Guardar resultados de pares e impares
Crea 2 listas y una tupla que tendrá números de 1 a 9.
La primera lista se llamará pares y el segundo impar, ambos estarán vacíos.
Después multiplica cada uno de los números de la tupla por un número aleatorio entre 1 y 100,
si el resultado es par guarda ese número en la lista de pares y si es impar en la lista de impares.
Muestra por consola: 
la multiplicación junto con su resultado con el formato 2 x 3 = 6 y la lista pares e impares
"""
import random
pares = []
impares = []
numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9)
for n in numeros:
    numero_random = random.randint(1,100)
    resultado = n * numero_random
    if resultado % 2 == 0:
        print(f'{n} x {numero_random} = {resultado}')
        pares.append(resultado)
    else:
        print(f'{n} x {numero_random} = {resultado}')
        impares.append(resultado)
print('LISTA DE PARES: ', pares)
print('LISTA DE IMPARES: ', impares)