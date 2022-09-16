"""
Aplicación 02:
Crear una función que realice la suma de n números.
"""
#Funcion suma
def sumar(*args, **kwargs):
    suma = 0
    for n in args:
        suma += n
    return suma, kwargs
suma_total, datos = sumar(10,20,3, 100, nombre = 'Hector', edad = 19)
print('La suma total es: ', suma_total)
print(datos) 