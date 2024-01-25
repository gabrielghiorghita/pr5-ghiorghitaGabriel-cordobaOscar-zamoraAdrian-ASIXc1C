"""
Exercici 2:
Programa que generi una llista de 100 nombres aleatoris entre 1 i 50. Obtenir la mitja dels nombres que es
troben a les posicions parelles i la mitja del nombre de les posicions senars.

Óscar Córdoba | Adrián Zamora | Gabriel Ghiorghita
ASIXc1C
"""
pares = 0


import random
aleatorios = [random.randint(0,50) for _ in range(100)]
print(aleatorios)

suma_pares = 0


for i in aleatorios:
    if i%2==0:
        suma_pares = sum(i)
        print(suma_pares)

#numero_media_pares =