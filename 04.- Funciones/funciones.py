"""
Aplicación 01:
-Crear una función que realice un saludo y crea una variable global en la función.
-Crear funcion sumar que reciba dos numeros enteros y que retorne el resultado.
-Crear función restar que reciba dos números entero y te retorno el resultado.
"""
#Funcion saludar
def saludar(nombre):
    #global nombre
    return f'Hola, {nombre} desde la función saludar'
#Funcion sumar    
def sumar(a, b):
    return a + b
#Funcion restar    
def restar(a=None, b=None):
    if a == None or b == None:
        print('Error: deves enviar dos números a la función')
        return
    return a - b
#Saludar(parametro)    
saludo = saludar('Hector')
print(saludo)
#Sumar(a,b)
suma = sumar(10, 20)
print('La suma es:', suma)
#Restar(a,b)
resta = restar(b = 20, a = 40)
print('La resta es: ', resta)
