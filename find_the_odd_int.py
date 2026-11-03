def find_it(seq):
    lista_numero_impar = []
    for i in range(len(seq)):
        if seq[i] in lista_numero_impar:
            lista_numero_impar.remove(seq[i])
        else:
            lista_numero_impar.append(seq[i])
    resultado = lista_numero_impar[0]
    return resultado
