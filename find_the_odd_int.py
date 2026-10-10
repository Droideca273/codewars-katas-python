def find_it(seq):
    lista1 = []
    for i in range (len(seq)):
        if seq[i] in lista1:
            lista1.remove(seq[i])
        else:
            lista1.append(seq[i])
    resultado=lista1[0]
    return resultado