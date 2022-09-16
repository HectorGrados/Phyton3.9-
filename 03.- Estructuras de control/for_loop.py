"""
Aplicación 04:
Iterar una lista obtén todos lo elementos de una lista usando fot loop y whike loop
"""
#Entrada de Datos
datos=['Hector','Grados',19,1.74,True]
#Operaciones con forr loop
print('Desarrollo con for loop')
for dato in datos:
    print(dato)
#Operacion con while
print('Desarrollo con while')
c=0
while c<len(datos):
    print(datos[c])
    c+=1     