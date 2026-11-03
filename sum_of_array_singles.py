def repeats(array):
    conjunto_numeros_impares = set()
    for i in range(len(array)):
        if (array[i]) in conjunto_numeros_impares:
            conjunto_numeros_impares.remove(array[i])
        else:
            conjunto_numeros_impares.add(array[i])
    return sum(conjunto_numeros_impares)
