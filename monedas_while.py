def euros(n):
    monedas=[5,2,1]
    cantidad_monedas=[0,0,0]
    moneda=0
    while n>0:
        if n//monedas[moneda]>=0:
            cantidad_monedas[moneda]=n//monedas[moneda]
            n=n%monedas[moneda]
        else:
            moneda+=1
    return (tuple(cantidad_monedas))