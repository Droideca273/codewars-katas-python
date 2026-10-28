def devolver_cambio(dinero_inicial):

    if dinero_inicial <= 0: return (0, 0, 0, 0, 0)

    cantidad_introducida = dinero_inicial
    tipos_de_monedas = [20, 10, 5, 2, 1]
    cantidad_de_monedas = [0] * len(tipos_de_monedas)
    indice = 0

    while cantidad_introducida > 0:
        cantidad_de_monedas[indice] = cantidad_introducida // tipos_de_monedas[indice]
        cantidad_introducida -= cantidad_de_monedas[indice] * tipos_de_monedas[indice]
        indice += 1

    return tuple(cantidad_de_monedas)


    

print(devolver_cambio(8))
# >>> (1, 1, 1)  # una de 5 cénts, una de 2 cénts y una de 1 cént.
print(devolver_cambio(5))
# >>> (1, 0, 0)  # una 5 cénts, ninguna de 2 cénts y ninguna de 1 cént.
print(devolver_cambio(29))
# >>> (5, 2, 0)  # cinco de 5 cénts, dos de 2 cénts y ninguna de 1 cént.
print(devolver_cambio(0))
# >>> (0, 0, 0) # ninguna de 5 cénts, ninguna de 2 cénts y 1 de cénts.
print(devolver_cambio(170))
# >>> (34, 0, 0)  # treinta y cuatro de 5 cénts, ninguna de 2 cénts y ninguna de 1 cént.
print(devolver_cambio(267))
# >>> (53, 1, 0)  # cincuenta y tres de 5 cénts, una de 2 cénts y ninguna de 1 cént.

