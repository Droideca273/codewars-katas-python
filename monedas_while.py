def calcular_cambio(dinero_inicial):

    if type(dinero_inicial) is not int: return (0, 0, 0, 0, 0)
    if dinero_inicial <= 0: return (0, 0, 0, 0, 0)

    cantidad_introducida = dinero_inicial
    tiposDeMonedas = [20, 10, 5, 2, 1]
    numeroDeMonedas = [0] * len(tiposDeMonedas)
    indice = 0

    while cantidad_introducida > 0:
        numeroDeMonedas[indice] = cantidad_introducida // tiposDeMonedas[indice]
        cantidad_introducida -= numeroDeMonedas[indice] * tiposDeMonedas[indice]
        indice += 1

    return tuple(numeroDeMonedas)


    

assert calcular_cambio(8) == (0, 0, 1, 1, 1), "Error en caso TEST"
assert calcular_cambio(5) == (0, 0, 1, 0, 0), "Error en caso TEST"
assert calcular_cambio(200) == (10, 0, 0, 0, 0), "Error en caso TEST"
assert calcular_cambio(11) == (0, 1, 0, 0, 1), "Error en caso TEST"
assert calcular_cambio(0) == (0, 0, 0, 0, 0), "Error en caso TEST"
assert calcular_cambio(-1) == (0, 0, 0, 0, 0), "Error en caso TEST"
assert calcular_cambio(2.45333) == (0, 0, 0, 0, 0), "Error en caso TEST"
assert calcular_cambio("s") == (0, 0, 0, 0, 0), "Error en caso TEST"