"""En una botiga volem convertir tot de preus sense a IVA al preu amb IVA. Per afegir l'IVA a un preu hem de sumar-hi
el 21% del seu valor.

L'usuari introduirà el preu de 10 articles. Imprimeix per pantalla el preu amb l'IVA afegit amb el següent format
indicat a continuació. El programa no pot imprimir res fins que hagi llegit tots els valors.

Cal considerar que, IVA és un valor constant, fins que no es modifiquin la normativa/llei
"""
# Constante para el porcentaje de IVA
IVA_PORCENTAJE = 21

# Inicializar una lista para almacenar los precios con IVA
precios_con_iva = []

# Solicitar al usuario ingresar el precio de 10 artículos
entrada_usuario = input("Ingrese los precios sin IVA de los 10 artículos separados por espacios: ")

# Convertir la entrada a una lista de precios
precios_sin_iva = list(map(float, entrada_usuario.split()))

# Control de errores para garantizar que no haya más de 10 artículos
if len(precios_sin_iva) > 10:
    print("No se permiten más de 10 artículos.")
else:
    # Calcular los precios con IVA y mostrar los resultados
    for precio_sin_iva in precios_sin_iva:
        precio_con_iva = precio_sin_iva * (1 + IVA_PORCENTAJE / 100)
        print(f"{precio_sin_iva:.1f} IVA = {precio_con_iva:.2f}")


