def euros(n):
    monedas=[5,2,1]
    cantidad_monedas=[0,0,0]
    for moneda in range(len(monedas)):
        if n//monedas[moneda]>=1:
            cantidad_monedas[moneda]=n//monedas[moneda]
            n=n%monedas[moneda]
    return (tuple(cantidad_monedas))