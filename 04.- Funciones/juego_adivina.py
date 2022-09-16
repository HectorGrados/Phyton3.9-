"""
Practica 05: 
Crear un juego donde el sistema genere un numero aleatorio y el jugador intente adivinar el
numero aleatorio.

Para crear este juego ten encueta los siguientes datos
-Difícil 5 intentos o vidas
-Intermedio 7 intentos o vidas
-Fácil 10 intentos o vidas

De acuerdo como va intentado el juego le debe dar una pista si el número es más grande o más pequeño.

También tiene que indicarle las vidas que le quedan.
"""
import random
def jugar(vidas):
    numero_random = random.randint(1, 100)
    numero_elegido = None
    while numero_random != numero_elegido:
        numero_elegido = int(input('Ingrese un número entre 1 y 100:'))
        if numero_random < numero_elegido:
            print("Elige un número mas pequeño")
            vidas -= 1
        elif numero_random > numero_elegido:
            print("Elige un número mas grande") 
            vidas -= 1
        if vidas == 0:
            print('GAME OVER')
            break
        print(f'Te quedan {vidas} vidas')
    if numero_elegido == numero_random:
        print("FELICIDADES GANASTE")
def main():
    while True:
        menu = """
        ADIVINA EL NÚMERO ALEATORIO
        1 - Nivel Facil 
        2 - Nivel Intermedio 
        3 - Nivel Dificil
        4 - Salir 
        INGRESE UNA OPCION: """
        opcion = input(menu)
        if opcion == '1':
            jugar(10)
        elif opcion == '2':
            jugar(7)
        elif opcion == '3':
            jugar(5)
        elif opcion == '4':
            print("CERRANDO JUEGO")
            break
        else:
            print("Opción incorrecta buelve ingresar")
if __name__ == '__main__':
    main() 
