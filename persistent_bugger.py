def persistence(n):
    numero = n
    numero_texto = str(numero)
    resultado_multiplicacion = 1
    contador_loops = 0
    while len(numero_texto) != 1:
        lista_digitos = list(numero_texto)
        for numero in lista_digitos:
            resultado_multiplicacion = resultado_multiplicacion * int(numero)
        numero = resultado_multiplicacion
        numero_texto = str(numero)
        resultado_multiplicacion = 1
        contador_loops += 1
    return contador_loops