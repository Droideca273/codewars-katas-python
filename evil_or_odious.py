def evil(n):
    cantidad_unos=0
    numero_binario=f"{n:b}"
    medida_binario=len(res)
    for i in range(0,medida_binario,1):
        if (numero_binario[i]=="1"):
            cantidad_unos=cantidad_unos+1
    if cantidad_unos % 2 == 0:
        resultado = "It's Evil!"
    else:
        resultado = "It's Odious!"
    return(resultado)