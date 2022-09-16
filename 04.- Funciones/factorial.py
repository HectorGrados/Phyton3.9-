"""
Aplicación 03: 
Crear una función que se recursiva para sacar la factorial de un número.
"""
#Funcion factorial
def factorial(n):
    #print('Valor inicial =>', n)
    if n > 1:
        n = n * factorial(n - 1)
    #print('Valor final => ', n)
    return n
n = int(input('Ingrese un número: '))
f = factorial(n)
print(f'Su Fatorial de {n} es: ', f)