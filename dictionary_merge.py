def merge(*dicts):
    resultado = {}
    for diccionario in dicts:
        for clave, valor in diccionario.items():
            if clave not in resultado:
                resultado[clave] = [valor]
            else:
                resultado[clave].append(valor)
    
    return resultado

if __name__ == '__main__':
    assert merge({"A": 1, "B": 2, "C": 3}, {"A": 5, "D": 6}, {"E": 7, "F": 8}, {"E": 9, "A": 1}) == {"A": [1, 5, 1], "B": [2], "C": [3], "D": [6], "E": [7, 9], "F": [8]}
    assert merge({"A": 1, "B": 2, "C": 3}, {"A": 4, "D": 5}, {}, {"E": 6, "D": 7}) == {"A": [1, 4], "B": [2], "C": [3], "D": [5, 7], "E": [6]}
    assert merge({True: "A", False: "B"}, {True: "C", False: "D"}, {True: "E"}) == {True: ["A", "C", "E"], False: ["B", "D"]}
    assert merge({}, {}, {}) == {}
    assert merge({"A": 1, "B": 2, "C": 3}) == {"A": [1], "B": [2], "C": [3]}
    assert merge({"A": 1}, {"B": 2}) == {"A": [1], "B": [2]}
    assert merge({"A": 1, "B": 2, "C": 3}, {"A": 4, "D": 5}) == {"A": [1, 4], "B": [2], "C": [3], "D": [5]}
