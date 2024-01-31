"""Un banc té tot de caixes de seguretat, enumerades del 0 al 10.

Volem registrar quan els usuaris obren una caixa de seguretat, i al final del dia, fer-ne un recompte.

L'usuari introduirà enters del 0 al 10 quan s'obri la caixa indicada.

Quan introdueixi l'enter -1, és que s'ha acabat el dia. Mostrar per pantalla el nombre de cops que s'ha obert.
"""

recuento_cajas = [0] * 11

# Pide al usuario que introduzca los números de las cajas de seguridad abiertas
entrada_usuario = input("Introduce los números de las cajas de seguridad abiertas (0-10), separados por espacios, y finaliza con -1: ")

# Convierte la entrada del usuario en una lista de enteros
numeros_cajas = list(map(int, entrada_usuario.split()))

try:
    for num_caja in numeros_cajas:
        if num_caja == -1:
            break
        recuento_cajas[num_caja] += 1
        print(recuento_cajas)
except: print("Deben ser mayor a 0 y menor a 11")



