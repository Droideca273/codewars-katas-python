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
print(stock_list(["ABART 20", "CDXEF 50", "BKWRK 25", "BTSQZ 89", "DRTYM 60"],["A", "B", "C", "W"]))