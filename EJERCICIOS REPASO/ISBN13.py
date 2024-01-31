"""A partir de l'any 2006 els ISBN van passar a tenir 13 dígits i es va adaptar per a què fos compatible amb el sistema
de codi de barres EAN-13.

Volem verificar si un codi ISBN és correcte. Mitjançant el dígit de control que és el dígit número 13. Es calcula de la
manera següent:

Es multiplica el primer dígit dels 12 dígits

per 1, el segon per 3, el tercer per 1, el quart per 3, i així successivament fins al número 12;

El dígit de control és el valor que s'ha d'afegir a la suma de tots aquests productes per fer-la divisible per 10. Si

el resultat de la suma ja fos múltiple de 10, el dígit de control seria 0.

Aquest ISBN 978-84-92493-70-8 ens el donarien de la manera següent, indica si el dígit de control és correcte."
"""
def validar_digito_control(isbn):
    # Verificar que la longitud del ISBN sea 13
    if len(isbn) != 13:
        return False

    # Inicializar la suma
    suma = 0

    # Multiplicar cada dígito por 1 o 3 según la posición y sumar los resultados
    for i in range(12):
        digito = int(isbn[i])
        multiplicador = 1 if i % 2 == 0 else 3
        suma += digito * multiplicador

    # Calcular el dígito de control
    digito_control = (10 - (suma % 10)) % 10

    # Verificar si el dígito de control es correcto
    return digito_control == int(isbn[12])

# Entrada del usuario
codigo = input("Ingrese los 13 dígitos del ISBN separados por espacios: ")

# Convertir la entrada a una lista de dígitos
isbn_digitos = list(map(int, codigo.split()))

# Verificar el dígito de control
resultado = validar_digito_control(isbn_digitos)

# Imprimir el resultado
print(resultado)



