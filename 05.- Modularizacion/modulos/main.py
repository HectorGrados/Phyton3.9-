"""
Importaciones de modulos en python
"""
#Importacion simple
import febonacci
febonacci.fibo(100)
print(febonacci.fibo2(100))

#Desde el modulo febonacci importas funciones especficas
from febonacci import fibo, fibo2
fibo(100)
print(fibo2(100))

#Importar todas las funciones del modulo
from febonacci import *
fibo(100)
print(fibo2(100))

#Agregar un alias a un modulo
import febonacci as f
f.fibo(100)
print(f.fibo2(100))

#Agregar un alias a una funcion especifica
from febonacci import fibo as f1
f1(100)
#Agregar un alias a una funcion especifica
from febonacci import fibo2 as f2
print(f2(100))

#Da la informacion del modulo
print(dir(febonacci))

#Informacion del modulo sys
import sys
print(dir(sys))

#Informacion del builtins
import builtins
print(dir(builtins))

