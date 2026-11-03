def order(sentence):
    sentencia_alterada = sentence[:] # Copia de sentencia
    sentencia_alterada = sentencia_alterada.split(" ") # Separamos las palabras para manipularlas individualmente
    lista_posiciones = []
    resultado = ""

    if sentence == "":
        return ""

    for palabra in sentencia_alterada: # Aquí nos quedamos con los números escondidos en las palabras 
        lista_letras_palabra = list(palabra)
        lista_letras_palabra = sorted(lista_letras_palabra)
        lista_posiciones.append(lista_letras_palabra[0])

    lista_posiciones_numeros = [int(posicion_lista_posicion) for posicion_lista_posicion in lista_posiciones] # Pasamos la lista de números de string a int

    for numero in range(1, len(lista_posiciones_numeros) + 1):  # Número de 1 a n para encontrar su equivalencia en lista_posiciones_numeros
        for posicion_lista_posicion in range(len(lista_posiciones_numeros)):  # Número de 0 a n que recorre las posiciones dentro de la lista lista_posiciones_numeros
            if (lista_posiciones_numeros[posicion_lista_posicion] == numero and resultado == ""):
                posicion = posicion_lista_posicion
                resultado = resultado + sentencia_alterada[posicion]
            elif (lista_posiciones_numeros[posicion_lista_posicion] == numero and resultado != ""):
                posicion = posicion_lista_posicion
                resultado = resultado + " " + sentencia_alterada[posicion]
    return resultado