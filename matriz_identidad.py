def esMatrizIdentidad(matrix):
    if len(matrix) < 2 or len(matriz) != len(matriz[0]):
            return False
    for lista in range(len(matriz)):
        for elemento in range(len(matriz)):
            if lista == elemento:
                if matriz[lista][elemento] != 1:
                    return False
            else:
                if matriz[lista][elemento] != 0:
                    return False
    return True



# Casos test:

matrix1 = [[1,0,0,0],
           [0,1,0,0],
           [0,0,1,0],
           [0,0,0,1]]
assert esMatrizIdentidad(matrix1) == True
#>>>True

matrix2 = [[1,0,0],
           [0,1,0],
           [0,0,0]]

assert esMatrizIdentidad(matrix2) == False
#>>>False

matrix3 = [[2,0,0],
           [0,2,0],
           [0,0,2]]

assert esMatrizIdentidad(matrix3) == False
#>>>False

matrix6 = [[1,0,0,0],  
           [0,1,0,2],  
           [0,0,1,0],  
           [0,0,0,1]]

assert esMatrizIdentidad(matrix6) == False
#>>>False

matrix7 = [[1, -1, 1],
           [0, 1, 0],
           [0, 0, 1]]
assert esMatrizIdentidad(matrix7) == False
#>>>False           


# casos test que no satisfacen la precondicion de que la matriz sea cuadrada (assert):

matrix4 = [[1,0,0,0],
           [0,1,1,0],
           [0,0,0,1]]

assert esMatrizIdentidad(matrix4) == False
#>>>False

matrix5 = [[1,0,0,0,0,0,0,0,0]]

assert esMatrizIdentidad(matrix5) == False
#>>>False           