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
# Casos tests
if __name__ in '__main__':
  assert first_n_smallest ([1,2,3,4,5],3) == [1,2,3]
  assert first_n_smallest([5,4,3,2,1],3 )== [3,2,1] 
  assert first_n_smallest([1,2,3,1,2],3) == [1,2,1]
  assert first_n_smallest([1,2,3,-4,0],3) == [1,-4,0]
  assert first_n_smallest([1,2,3,4,5],0) == []
  assert first_n_smallest([1,2,3,4,5],5) == [1,2,3,4,5]
  assert first_n_smallest([1,2,3,4,2],4) == [1,2,3,2]
  assert first_n_smallest([2,1,2,3,4,2],2) == [2,1]
  assert first_n_smallest([2,1,2,3,4,2],3) == [2,1,2]
  assert first_n_smallest([2,1,2,3,4,2],4) == [2,1,2,2]
  print("Felicidades")