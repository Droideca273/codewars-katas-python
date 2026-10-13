def permute_a_palindrome(string):
    string=string.lower()
    string=string.split (" ")
    string=''.join(string)
    lista_letras_impares = []
    for i in range (len(string)):
        if string[i] in lista_letras_impares:
            lista_letras_impares.remove(string[i])
        else:
            lista_letras_impares.append(string[i])
    if len(string)%2 == 1 and len(lista_letras_impares)==1:
        return True
    elif len(string)%2 == 0 and len(lista_letras_impares)==0:
        return True
    else :
        return False