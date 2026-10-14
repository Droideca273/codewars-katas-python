def find_uniq(arr):
    lista = arr[:]
    lista = sorted(lista)
    ultimo_numero = len(lista) - 1
    if lista[0] != lista[1]:
        return lista[0]
    else:
        return lista[ultimo_numero]
