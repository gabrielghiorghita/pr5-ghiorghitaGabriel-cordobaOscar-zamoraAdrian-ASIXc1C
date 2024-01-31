"""Programa una funció que donat un tauler d'escacs, i una posició, ens mostri per pantalla quines són les possibles
posicions a les quals es pot moure una torre.

Primer caldrà llegir la posició de la torre, que simbolitzarem en el tauler amb el valor 2, les posicions on aquesta es
pugui moure les simbolitzarem amb el valor 1 i la resta de posicions amb el valor 0.

El moviment de la torre és el següent: Es pot moure al llarg d'una fila o d'una columna (però no successivament en una
mateixa jugada); se la pot fer avançar tantes caselles com es vulgui.

Per imprimir la torre còpia la línia següent: TORRE = "♖"
"""

TORRE = "♖"

def mostrar_tablero(tablero):
    for fila in tablero:
        for casilla in fila:
            print(casilla, end=" ")
        print()

def letra_a_numero(letra):
    return ord(letra.lower()) - ord('a')

def posiciones_posibles_torre(tablero, fila, columna):
    # Marcar las posiciones a lo largo de la fila
    for i in range(len(tablero)):
        if i != fila:
            tablero[i][columna] = 1

    # Marcar las posiciones a lo largo de la columna
    for j in range(len(tablero[0])):
        if j != columna:
            tablero[fila][j] = 1

    # Marcar la posición de la torre
    tablero[fila][columna] = TORRE

    # Mostrar el tablero con las posiciones marcadas
    mostrar_tablero(tablero)

# Ejemplo de uso
tablero_ajedrez = [[0 for _ in range(8)] for _ in range(8)]

# Entrada del usuario para la posición de la torre
columna_letra = input("Ingrese la letra de la columna (a-h): ")
fila_torre = int(input("Ingrese el número de la fila (1-8): "))

# Verificar que las coordenadas estén dentro del rango
if 1 <= fila_torre <= 8 and 'a' <= columna_letra <= 'h':
    columna_torre = letra_a_numero(columna_letra)
    posiciones_posibles_torre(tablero_ajedrez, fila_torre - 1, columna_torre)
else:
    print("Coordenadas fuera del rango.")


