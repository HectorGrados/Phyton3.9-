#Entrada de Datos
print('Realiza una venta')
valor_venta= float(input('Ingrese valor de venta: '))

#Operaciones
igv= valor_venta*0.18
pv = valor_venta+igv

#Salida de datos
print('='*25)
print('----FACTURA DE VENTA----')
print('='*25)
print('Valor de venta:',valor_venta)
print('IGV: ',igv)
print('Precio de venta:',pv)
print('='*25)