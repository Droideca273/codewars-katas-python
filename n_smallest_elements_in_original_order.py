def first_n_smallest(arr, n):
    if n <= 0:
        return []
    if n >= len(arr):
        return arr[:]

    # Obtenemos los n elementos más pequeños
    smallest = sorted(arr)[:n]

    # Filtramos la lista original preservando el orden de aparición
    resultado = []
    for numero in arr:
        if numero in smallest:
            smallest.remove(numero)
            resultado.append(numero)

    return resultado
