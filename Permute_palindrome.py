def permute_a_palindrome(string):
    texto = string[:]
    texto = texto.lower()
    texto = texto.split(" ")
    texto = "".join(texto)
    lista_letras_impares = []
    for posicion in range(len(texto)):
        if texto[posicion] in lista_letras_impares:
            lista_letras_impares.remove(texto[posicion])
        else:
            lista_letras_impares.append(texto[posicion])
    if len(texto) % 2 == 1 and len(lista_letras_impares) == 1:
        return True
    elif len(texto) % 2 == 0 and len(lista_letras_impares) == 0:
        return True
    else:
        return False
