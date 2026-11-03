def first_n_smallest(arr, n):
    if n <= 0:
        return []
    if n >= len(arr):
        return arr[:]

    # Obtenemos los n elementos más pequeños
    smallest = sorted(arr)[:n]

    # Filtramos la lista original preservando el orden de aparición
    resultado = []
    for x in arr:
        if x in smallest:
            smallest.remove(x)
            resultado.append(x)

    return resultado
