def check_sudoku(sudoku):
    longitud_sudoku = len(sudoku)
    comparacion = list(range(1, longitud_sudoku + 1))
    
    for fila in sudoku:
        if len(fila) != longitud_sudoku:
            return False
            
        for val in fila:
            if type(val) != int:
                return False
            
        if sorted(fila) != comparacion:
            return False
            
    for col in range(longitud_sudoku):
        columna = [sudoku[fila][col] for fila in range(longitud_sudoku)]
        if sorted(columna) != comparacion:
            return False
            
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

incorrect5 = [ [1, 1.5],
               [1.5, 1]]
if __name__ == "__main__":
    assert check_sudoku(correct) == True
    assert check_sudoku(incorrect) == False
    assert check_sudoku(incorrect2) == False
    assert check_sudoku(incorrect3) == False
    assert check_sudoku(incorrect4) == False
    assert check_sudoku(incorrect5) == False