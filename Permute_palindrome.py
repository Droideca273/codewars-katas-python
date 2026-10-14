def permute_a_palindrome(string):
    texto = string[:]
    string = string.lower()
    string = string.split(" ")
    string = "".join(string)
    lista_letras_impares = []
    for posicion in range(len(string)):
        if string[posicion] in lista_letras_impares:
            lista_letras_impares.remove(string[posicion])
        else:
            lista_letras_impares.append(string[posicion])
    if len(string) % 2 == 1 and len(lista_letras_impares) == 1:
        return True
    elif len(string) % 2 == 0 and len(lista_letras_impares) == 0:
        return True
    else:
        return False
