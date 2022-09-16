"""
Descripciones y metodos en listas
"""
#Lista
datos=['Hector',19,'Peru']
print(datos)
#Agregar a la lista
datos.append("Grados")
print(datos)
#Extender la lista
datos.extend(datos)
print(datos)
#Insert = colocar nuevo dato en un lugar especifico
datos.insert(0,100)
print(datos)
#Funcion remove = elimina un elemento
datos=['Hector','Grados',19,'Peru']
datos.remove('Grados')
print(datos)
#Funcion pop = eliminar el ultimo elemento
datos=['Hector','Grados',19,'Peru']
datos.pop()
print(datos)
#Funcion clear = eliminar 
datos=['Hector','Grados',19,'Peru']
datos.clear()
print(datos)
#Funcion index = te da el indice
datos=['Hector','Grados',19,'Peru']
print(datos.index(19)) 
#Funcion count = cuenta elementos iguales en una lista
datos=['Hector','Grados',19,19,19]
print(datos.count(19))
#Funcion sort = ordena
letras=['naranja','aguacate','pera']
letras.sort()
print(letras)
#Funcion reverse
datos=[1,2,3,4,5]
datos.reverse()
print(datos) 