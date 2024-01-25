"""
Exercici 1:
Fer un programa de càlcul de temperatures del mar. Les tasques a fer són:
Calcular per a l’any  2022: temperatura màxima, mínima i mitjana
Calcular per període 2000 a 2022: temperatura màxima, mínima i mitjana

Óscar Córdoba | Adrián Zamora | Gabriel Ghiorghita
ASIXc1C
"""

mesos = ["Gener", "Febrer", "Març", "Abril", "Maig", "Juny", "Juliol", "Agost", "Setembre", "Octubre", "Novembre", "Desembre",]
temperatures_2022 = [13.6, 13.4, 13.2, 13.4, 13.9, 13.7, 13.7, 13.8, 14.0, 14.3, 16.0, 15.1,]
temperatures_2000_a_2022=[13.6, 13.4, 13.2, 13.4, 13.9, 13.7, 13.7, 13.8, 14.0, 14.3, 16.0, 15.1, 14.0,
                          13.3, 12.9, 13.5, 13.5, 13.7, 13.8, 13.8, 13.8, 14.2, 14.6, 16.8, 14.7, 14.1,
                          14.4, 13.9, 13.6, 13.5, 13.7, 13.9, 13.9, 14.0, 14.3, 14.7, 15.6, 14.6, 14.2,
                          13.9, 12.5, 13.3, 13.4, 14.0, 13.9, 13.8, 13.9, 14.5, 14.9, 15.5, 15.4, 14.1,
    13.2, 12.7, 12.3, 12.9, 13.8, 13.9, 14.0, 14.1, 14.3, 17.9, 17.7, 15.9, 14.4,
    13.7, 12.8, 13.4, 13.9, 14.0, 14.0, 13.9, 14.0, 14.0, 14.6, 14.8, 13.3, 13.9,
    14.1, 13.6, 12.9, 13.5, 14.0, 13.9, 14.0, 14.0, 14.2, 16.3, 16.5, 15.6, 14.4,
    14.1, 12.6, 12.9, 13.5, 14.3, 13.9, 13.7, 13.8, 14.1, 15.8, 15.8, 15.1, 14.1,
    13.7, 13.2, 13.6, 13.6, 14.7, 14.2, 13.9, 14.0, 14.5, 15.7, 16.5, 16.0, 14.5,
    13.2, 12.2, 12.0, 13.1, 13.5, 14.1, 13.7, 13.6, 13.6, 15.3, 15.9, 13.6, 13.7,
    13.9, 12.4, 12.6, 13.3, 13.7, 13.5, 13.5, 13.7, 13.9, 14.8, 15.8, 13.9, 13.8,
    13.0, 12.5, 12.5, 13.6, 13.5, 14.0, 14.1, 13.7, 13.8, 15.2, 17.6, 15.9, 14.1,
    12.6, 11.9, 12.2, 12.8, 13.7, 13.6, 13.5, 13.5, 13.9, 15.6, 15.5, 14.0, 13.6,
    13.3, 12.5, 12.6, 12.8, 14.2, 13.7, 13.7, 13.8, 14.0, 16.2, 15.9, 14.5, 13.9,
    13.2, 13.0, 12.9, 12.8, 13.3, 13.6, 13.7, 13.8, 13.9, 14.3, 15.5, 13.8, 13.7,
    14.3, 13.4, 13.2, 13.4, 14.4, 13.8, 13.8, 13.8, 14.0, 15.5, 15.5, 13.9, 14.1,
    12.5, 12.3, 12.1, 12.9, 13.1, 13.4]


maxima_2022 = temp_max = temp_min = temperatures_2022[0]

for temperatura in temperatures_2022:
    if temperatura < temp_max:
        temp_max = temperatura
    elif temperatura > temp_min:
        temp_min = temperatura

suma_numeros = 0
for numeros in temperatures_2022:
    suma_numeros += numeros

media_2022 = suma_numeros / len(temperatures_2022)

temp_max_total = temp_min_total = temperatures_2000_a_2022[0]
for temperatura in temperatures_2000_a_2022:
    if temperatura > temp_max_total:
        temp_max_total = temperatura
    elif temperatura < temp_min_total:
        temp_min_total = temperatura

suma_numeros_total = 0
for numeros2 in temperatures_2000_a_2022:
    suma_numeros_total += numeros2

media_total = suma_numeros_total / len(temperatures_2000_a_2022)

print ("●Any 2022")
print (f"   ⊚Màxima:{temp_min:.2f}")
print (f"   ⊚Mínima:{temp_max:.2f}")
print (f"   ⊚Mitjana:{media_2022:.2f}")
print ("\n")
print("●Període 2000 a 2022")
print(f"    ⊚Màxima: {temp_max_total:.2f}")
print(f"    ⊚Mínima: {temp_min_total:.2f}")
print(f"    ⊚Mitjana: {media_total:.2f}")