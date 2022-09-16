"""
Aplicación 01:
Determinar si un número entero es par positivo, impar positivo, par negativo, impar negativo o neutro.
"""
#Entrada de Datos
n=int(input('Ingrese un numero entero: '))
#Operaciones
if n!=0: 
    if n>0:
        if n%2==0:
            print("Numero es par positivo")
        else:
            print("Numero es impar positivo") 
    else:
        if n%2==0:
            print("Numero es par negativo")
        else:
            print("Numero es impar negativo") 
else:
    print('El numero es neutro')



  