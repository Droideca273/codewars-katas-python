def stock_list(stocklist, categories):
    if not stocklist or not categories:
        return ""
    libros = {}
    resultado = []
    for letra in categories:
        libros[letra] = 0
    for book in stocklist:
        codigo = book.split()
        if codigo[0][0] in libros:
            libros[codigo[0][0]] = str(int(libros[codigo[0][0]]) + int(codigo[1]))
        else:
            continue
    for key, valor in libros.items():
        resultado.append(f"({key} : {valor})")
    return (" - ").join(resultado)
if __name__ == '__main__':
    assert stock_list(["ABART 20", "CDXEF 50", "BKWR 25", "BTSQ 89", "DRTY 60"], ["A", "B", "C", "W"]) == "(A : 20) - (B : 114) - (C : 50) - (W : 0)"
    assert stock_list(["CBART 20", "CDXEF 50", "BKWR 25", "BTSQ 89", "DRTY 60"], ["A", "B", "C", "W"]) == "(A : 0) - (B : 114) - (C : 70) - (W : 0)"
    assert stock_list(["BBAR 150", "CDXEF 50", "BKWR 25", "BTSQ 89", "DRTY 60"], ["A", "B", "C", "D"]) == "(A : 0) - (B : 264) - (C : 50) - (D : 60)"
    assert stock_list([], ["A", "B"]) == ""
    assert stock_list(["ABART 20"], []) == ""