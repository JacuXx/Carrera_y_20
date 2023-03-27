def sumar_numero(suma_parcial, jugador, numero):
    if int(numero) <= 2:
        print("El jugador", jugador, "eligió: ", numero)
        resultado = int(numero)
        suma_parcial += resultado
        print("La suma ahora es:", suma_parcial)
    return suma_parcial
