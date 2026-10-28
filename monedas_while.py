def devolver_cambio(dinero_inicial):

    if type(dinero_inicial) is not int: return (0, 0, 0, 0, 0)
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


    

assert devolver_cambio(8) == (0, 0, 1, 1, 1), "Error en caso TEST"
assert devolver_cambio(5) == (0, 0, 1, 0, 0), "Error en caso TEST"
assert devolver_cambio(200) == (10, 0, 0, 0, 0), "Error en caso TEST"
assert devolver_cambio(11) == (0, 1, 0, 0, 1), "Error en caso TEST"
assert devolver_cambio(0) == (0, 0, 0, 0, 0), "Error en caso TEST"
assert devolver_cambio(-1) == (0, 0, 0, 0, 0), "Error en caso TEST"
assert devolver_cambio(2.45333) == (0, 0, 0, 0, 0), "Error en caso TEST"
assert devolver_cambio("s") == (0, 0, 0, 0, 0), "Error en caso TEST"



print(devolver_cambio(5))
# >>> (0, 0, 1, 0, 0)  
print(devolver_cambio(29))
# >>> (1, 0, 1, 2, 0)  
print(devolver_cambio(0))
# >>> (0, 0, 0, 0, 0) 
print(devolver_cambio(170))
# >>> (8, 1, 0, 0, 0)  
print(devolver_cambio(267))
# >>> (13, 0, 1, 1, 0)  

