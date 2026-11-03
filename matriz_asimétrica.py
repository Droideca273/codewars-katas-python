def esAntisimetrica(matriz):
    if len(matriz) < 2:
        return False
    for i in matriz:
        if len(i) != len(matriz):
            return False
    for lista in range(len(matriz)):
        for elemento in range(len(matriz)):
            if lista != elemento and matriz[lista][elemento] != -(matriz[elemento][lista]):
                return False
    return True

if __name__ == '__main__':
    # Test Cases:

    assert esAntisimetrica([ [0, 1, 2],
                             [-1, 0, 3],
                             [-2, -3, 0]]) is True

    assert esAntisimetrica([[0, 0, 0],
                             [0, 0, 0],
                             [0, 0, 0]]) is True

    assert esAntisimetrica([ [0, 1, 2],
                             [-1, 0, -2],
                             [2, 2, 3]]) is False

    assert esAntisimetrica([ [1, 2, 5],
                             [0, 1, -9],
                             [0, 0, 1]]) is False
    
    assert esAntisimetrica([ [1, 2,  5],
                             [-2, 1, -9],
                             [-5, 0, 1]]) is False


    # casos test que no satisfacen la precondicion de que la matriz sea cuadrada:
    matriz5 = [[1, 0, 0, 0],
               [0, 1, 1, 0],
               [0, 0, 0, 1]]

    assert esAntisimetrica(matriz5) is False

    matriz6 = [[1, 0, 0, 0, 0, 0, 0, 0, 0]]

    assert esAntisimetrica(matriz6) is False

    matriz7 = [[1, 0, 0, 0],
               [0, 1, 0],
               [0, 0, 0, 1]]

    assert esAntisimetrica(matriz7) is False
