"""
Herencia
"""
from persona import Cliente, Empleado
print('='*25)
print('Clientes')
print('='*25)
#Primer cliente(nombre,edad)
cliente1 = Cliente('Hector' , 18)
#Segundo cliente (nombre,edad)
cliente2 = Cliente('Emanuel', 19)
#Devuelve el dato del cliente
cliente1.detalle_persona()
cliente2.detalle_persona()
print('='*25)
print('Empleados')
print('='*25)
#Primer empleado(nombre,edad,sueldo)
empleado1 = Empleado('Maria', 45, 1500)
#Segundo empleado(nombre,edad,sueldo)
empleado2 = Empleado('Nilton', 45, 2000)
#Devuelve el dato del empleado
empleado1.detalle_persona()
empleado1.detalle_empleado()
print('='*25)