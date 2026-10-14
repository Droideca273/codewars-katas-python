def comp(array1, array2):
    if array1 is None or array2 is None:
        return False

    array1_ordenado = sorted(array1, key=abs)
    array2_ordenado = sorted(array2)

    if len(array1) != len(array2):
        return False

    for i in range(len(array1_ordenado)):
        if array1_ordenado[i] * array1_ordenado[i] == array2_ordenado[i]:
            None
        else:
            return False
    return True
