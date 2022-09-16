"""
Colas en python
"""
from collections import deque
#Crear cola
cola=deque(['Hector','Grados','Correa'])
print(cola)
#Agregar
cola.append('Blaze')
print(cola)
#popleft = elimina elemento de la izquierda
cola.popleft()
print(cola) 