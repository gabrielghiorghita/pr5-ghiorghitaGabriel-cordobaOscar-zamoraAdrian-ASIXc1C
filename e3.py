"""
Exercici 3:
Programa de traducció d’insults. Crear una estructura de dues dimensions amb els insults en català
i afegir la traducció en castellà, anglès i klingon.

El programa, demanarà a l’usuari que escrigui per teclat un insult, en català,
 i el mostrarà traduït a castellà, anglès i klingon.

Óscar Córdoba | Adrián Zamora | Gabriel Ghiorghita
ASIXc1C
"""
CAT = 0  #català
ESP = 1  #castellà
ENG = 2  #anglès

#Estructura pels insutls i idiomes
insults = [
    ['Mocós', 'Capsigrany', 'Pixapins', 'Tros d’ase'],
    ['Mocoso', 'Cabezón', 'Mea pinos', 'Trozo de asno'],
    ['Brat', 'Pigheaded', 'Piss pines', 'Piece of donkey'],
]



def triar_insult():
    print("Tria un insult:")
    for i, insult in enumerate(insults[CAT]):
        print(f'{i}. {insult}')

    try:
        index = int(input("Introdueix el número de l'insult que vols traduir: "))

        if 0 <= index < len(insults[CAT]):
            insult_cat = insults[CAT][index]
            insult_esp = insults[ESP][index]
            insult_eng = insults[ENG][index]


            print(f'Traducció a castellà: {insult_esp}')
            print(f'Traducció a anglès: {insult_eng}')
        else:
            print("Índex no vàlid.")
    except ValueError:
        print("Si us plau, introdueix un número vàlid.")



triar_insult()
