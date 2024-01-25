"""
Exercici 2:
Programa que generi una llista de 100 nombres aleatoris entre 1 i 50. Obtenir la mitja dels nombres que es
troben a les posicions parelles i la mitja del nombre de les posicions senars.

Óscar Córdoba | Adrián Zamora | Gabriel Ghiorghita
ASIXc1C
"""
import random

nombres_parelles = []
nombres_senars = []

#Generem una llista de 100 nombres aleatoris entre 1 i 50
llista_nombres = [random.randint(1, 50) for _ in range(100)]

#Separem els nombres en parells i senars.
for i in range(len(llista_nombres)):
    if i % 2 == 0:
        nombres_parelles.append(llista_nombres[i])
    else:
        nombres_senars.append(llista_nombres[i])

#Calculem la mitja dels valors parells.
mitja_parelles = sum(nombres_parelles) / len(nombres_parelles)

#Calculem la mitja dels valors senars.
mitja_senars = sum(nombres_senars) / len(nombres_senars)

#Mostrem els resultats per pantalla.
print("Llista de nombres aleatoris:", llista_nombres)
print("Mitja de les posicions parelles:", mitja_parelles)
print("Mitja de les posicions senars:", mitja_senars)
