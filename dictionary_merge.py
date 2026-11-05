def merge(*dicts):
    resultado = {}
    for diccionario in dicts:
        for clave, valor in diccionario.items():
            if clave not in resultado:
                resultado[clave] = [valor]
            else:
                resultado[clave].append(valor)
    
    return resultado
print(merge({"A": 1, "B": 2, "C": 3}, {"A": 5, "D": 6}, {"E": 7, "F": 8}, {"E": 9, "A": 1}))
'''
if __name__ == '__main__':
    assert merge({"A": 1, "B": 2, "C": 3}, {"A": 5, "D": 6}, {"E": 7, "F": 8}, {"E": 9, "A": 1}) == {"A": [1, 1, 5], "B": [2], "C": [3], "D": [6], "E": [9, 7], "F": [8]}
'''