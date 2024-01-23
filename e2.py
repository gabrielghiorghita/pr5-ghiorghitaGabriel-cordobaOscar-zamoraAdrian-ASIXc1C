"""
Exercici 2:
Programa que generi una llista de 100 nombres aleatoris entre 1 i 50. Obtenir la mitja dels nombres que es
troben a les posicions parelles i la mitja del nombre de les posicions senars.

Óscar Córdoba | Adrián Zamora | Gabriel Ghiorghita
ASIXc1C
"""
#import random
#print(random.randint(1,50))

import random
aleatorios = [random.randint(0,50) for _ in range(50)]
print(aleatorios)