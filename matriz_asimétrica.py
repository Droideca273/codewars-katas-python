def esAntisimetrica(matriz):
    if len(matriz) < 2 or len(matriz) != len(matriz[0]):
        return False
    for lista in range(len(matriz)):
        for elemento in range(len(matriz)):
            if lista != elemento and matriz[lista][elemento] != -(matriz[elemento][lista]):
                return False
    return True


# Casos Test:

assert esAntisimetrica([[0, 1, 2], [-1, 0, 3], [-2, -3, 0]]) == True, "Fallo caso 1"
# >>> True

assert esAntisimetrica([[0, 0, 0], [0, 0, 0], [0, 0, 0]]) == True, "Fallo caso 2"
# >>> True

assert esAntisimetrica([[0, 1, 2], [-1, 0, -2], [2, 2, 3]]) == False, "Fallo caso 3"
# >>> False

assert esAntisimetrica([[1, 2, 5], [0, 1, -9], [0, 0, 1]]) == False, "Fallo caso 4"
# >>> False

matriz4 = [[1, 0, 0, 0], [0, 1, 1, 0], [0, 0, 0, 1]]

assert esAntisimetrica(matriz4) == False, "Fallo caso 5"
# >>>False

matriz5 = [[1, 0, 0, 0, 0, 0, 0, 0, 0]]

assert esAntisimetrica(matriz5) == False, "Fallo caso 6"
# >>>False
