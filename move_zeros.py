def move_zeros(lst):
    lista=lst[:]
    cantidad_zeros=0
    for posicion in range(len(lista)-1,-1,-1):
        if lista[posicion]==0:
            lista.pop(posicion)
            cantidad_zeros=cantidad_zeros+1
    for añadir_ceros in range(cantidad_zeros):
        lista.append(0)
    return(lista)