"""
Practica 01: Palíndromo
Crear un sistema que detecte si una palabra es palíndroma o no
"""
def palindromo(palabra):
    palabra = palabra.replace(' ', '')
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False
#Función Principal
def main():
    palabra = input('Ingrese una palabra: ')
    es_palindromo = palindromo(palabra)
    if es_palindromo:
        print('Es Palindromo')
    else:
        print('No es Palindromo')
#Punto de entrada de la aplicación 
if __name__ == '__main__':
    main()