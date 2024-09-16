import random as ran
import numpy as np
import os

#Memorama
# Es un programa que realiza una simulacion del conocido juego de mesa 'memorama'
# Herramientas:
    # randomon: libreria que nos ayuda a elegir aleatoreamente las posiciones de las cartas en el tablero
    # numpy: libreria que nos ayuda a trabajar con matrices en python
    # os: En este caso se usa para poder limpiar la terminal despues de cierto procesos

# ENRIQUE CHAVEZ VALDEZ
# SOFTWARE 07_03

baraja_base = ["😊", "😊","😂", "😂","❤️", "❤️","🙌", "🙌"]
tablero_base = np.empty((2, 4))
cartas_seleccionadas = ["", ""]
posiciones = [0, 0]

def main():
    vidas = 6
    tableroA = tablero_base.astype(str)
    llenar_tablero(tableroA, baraja_base)
    tableroB = copiar_tablero(len(tableroA), len(tableroA[0]))
    
    while(vidas > 0 and not ganaste(tableroB)):
        os.system('cls')
        print(f"V I D A S: {vidas}\n")
        print(tableroB, "\n")
        
        for i in range(2):
            posicion = elegir_posicion(i+1, tableroB)
            posiciones[i] = posicion
            cartas_seleccionadas[i] = elegir_carta(posicion, tableroA, tableroB)

            os.system('cls')
            print(tableroB, "\n")

        if (cartas_seleccionadas[0] == cartas_seleccionadas[1]):
            print("Son pares!!")
        else:
            vidas -= 1
            print("No son pares :(")
            for i in range(len(posiciones)):
                voltear_carta(posiciones[i], tableroB, tableroA)
           
        input("Presiona Enter para continuar...")


def llenar_tablero(tablero, baraja):
    for i in range(len(tablero)):
        for j in range(len(tablero[0])):
            tablero[i][j] = poner_carta(baraja)

def poner_carta(cartas):
    posicion = ran.randint(0, len(cartas)-1)
    carta = cartas[posicion]
    cartas.remove(carta)
    return carta

def copiar_tablero(filas, columnas):
    matriz = np.full((filas, columnas), 'X', dtype=str)
    return matriz

def elegir_posicion(carta_n, tablero):
    while True:
        print(f"Seleccionando la posición para la carta {carta_n}.")
        fila = solicitar_numero(f"Elija la fila de la carta {carta_n} (0 a {len(tablero) - 1}): ", len(tablero))
        columna = solicitar_numero(f"Elija la columna de la carta {carta_n} (0 a {len(tablero[0]) - 1}): ", len(tablero[0]))
        if not carta_seleccionada((fila, columna), tablero): return fila, columna
        else: print("Esa carta ya esta seleccionada, vuelve a intentarlo")

def solicitar_numero(mensaje, limite):
    while True:
        try:
            numero = int(input(mensaje))
            if 0 <= numero < limite:
                return numero
            else:
                print(f"Introduzca un número entre 0 y {limite - 1}.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número entero.")

def carta_seleccionada(posicion, tablero):
    if (tablero[posicion] != 'X'): return True
    else: return False

def elegir_carta(posicion, tablero1, tablero2):
        carta = tablero1[posicion]
        voltear_carta(posicion, tablero1, tablero2)
        return carta       

def ganaste(tablero):
    for i in range(len(tablero)):
        for j in range(len(tablero[0])):
            if (tablero[i,j] == 'X'):
                return False
    return True

def voltear_carta(posicion, tablero1, tablero2):
    fila, columna = posicion
    tablero1[fila, columna], tablero2[fila, columna] = tablero2[fila, columna], tablero1[fila, columna]

if __name__ == "__main__":
    main()
