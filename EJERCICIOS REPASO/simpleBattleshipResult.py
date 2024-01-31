"""Donada la següent configuració del joc Enfonsar la flota, indica si a la posició x, y hi ha aigua o un vaixell (tocat)

Configuració:

On x són vaixells i els 0 aigua, casella superior esquerra és la 0,0 i la superior dreta la 0,6"""


# Configuración del tablero
tablero = [
    [0, 0, 0, 'x', 'x', 'x', 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 'x', 0, 0, 0, 'x', 0],
    ['x', 'x', 'x', 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 'x', 0],
    [0, 'x', 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
]

# Entradas del usuario
x = int(input("Ingrese la coordenada x: "))
y = int(input("Ingrese la coordenada y: "))

# Verificar la posición en el tablero
if 0 <= x < 7 and 0 <= y < 7:
    if tablero[x][y] == 0:
        print("aigua")
    elif tablero[x][y] == 'x':
        print("tocat")
else:
    print("Posición no válida. Las coordenadas deben estar entre 0 y 6.")
