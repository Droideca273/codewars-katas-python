def esMatrizCuadrada(sudoku):
    for fila in sudoku:
        if len(fila) != len(sudoku):
            return False
    return True

def sonElementosEnteros(sudoku):
    for fila in sudoku:
        for columna in fila:
            if type(columna) != int:
                return False
    return True

def filasValidas(sudoku):
    for fila in sudoku:
        for indice in range(1, len(sudoku)+1):
            if indice not in fila:
                return False
    return True

def columnasValidas(sudoku):
    
def checkSudoku(sudoku):
    return True

correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

incorrect2 = [[1,2,3,4],
              [2,3,1,4],
              [4,1,2,3],
              [3,4,1,2]]

incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

incorrect5 = [[1, 1.5],
              [1.5, 1]]
if __name__ == "__main__":
    assert checkSudoku(correct) == True
    assert checkSudoku(incorrect) == False
    assert checkSudoku(incorrect2) == False
    assert checkSudoku(incorrect3) == False
    assert checkSudoku(incorrect4) == False
    assert checkSudoku(incorrect5) == False