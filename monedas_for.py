def euros(n):
    monedas=[5,2,1]
    cantidad_monedas=[0,0,0]
    for i in range(len(monedas)):
        if n//monedas[i]>=1:
            cantidad_monedas[i]=n//monedas[i]
            n=n%monedas[i]
    return (tuple(cantidad_monedas))