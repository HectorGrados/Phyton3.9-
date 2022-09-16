"""
Aplicación 03:
Suma de n números anteriores
"""
#Entrada de Datos
n= int(input('Ingrese un numero: '))
#Operaciones
suma=0
menores_n=0
while menores_n<n:
    suma=menores_n+suma
    menores_n+=1
print('Las suma es: ',suma)