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
# >>> (0, 0, 1, 1, 1)  
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

