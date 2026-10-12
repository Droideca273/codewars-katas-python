def century(year):
    año_texto=str(year)
    if len(año_texto)==3:
        siglo=año_texto[0:1]
    else:
        siglo=año_texto[0:2]
    if year<100:
        return 1
    else:
        if year%100!=0:
            return int(siglo)+1
        else:
            return int(siglo)