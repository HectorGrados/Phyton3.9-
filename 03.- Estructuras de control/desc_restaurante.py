"""
Practica 01: 
Un restaurante ofrece un descuento del 10% para consumo de hasta s/. 100.00 y un descuento del 20 %
para consumos mayores, para ambos casos se aplica un impuesto del 19%.
Determinar el monto del descuento, el impuesto y el importe a pagar.
"""
# Entrada 
consumo = float(input('Ingrese el consumo del cliente: '))
if consumo >= 0:
    #Proceso 
    if consumo <= 100:
        # Descuento de 10%
        dato_descuento = '10%'
        descuento = consumo * 0.10
    elif consumo > 100 and consumo <= 200:
        #Descuento de 20%
        dato_descuento = '20%'
        descuento = consumo * 0.20
    elif consumo > 200:
        #Descuento de 30%
        dato_descuento = '30%'
        descuento = consumo * 0.30
    monto_descuento = consumo - descuento
    igv = monto_descuento * 0.19 
    total_pagar = monto_descuento + igv
    #Salida de datos 
    print('='*30)
    print('----- FACTURA DE CONSUMO -----')
    print('Descuento que se aplica:', dato_descuento)
    print('='*30)
    print('Consumo: ', consumo)
    print('Descuento: ', descuento)
    print('Monto con descuento: ', monto_descuento)
    print('IGV: ', igv)
    print('Total a Pagar: ', total_pagar)
    print('='*30)
else:
    print('Error al Ingresar el consumo') 