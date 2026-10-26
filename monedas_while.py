def euros(n):
    dinero=n
    monedas=[5,2,1]
    cantidad_monedas=[0,0,0]
    moneda=0
    if type(dinero) is not int or dinero<0:
        return None
    while dinero>0:
        if dinero//monedas[moneda]>=0:
            cantidad_monedas[moneda]=dinero//monedas[moneda]
            dinero=dinero%monedas[moneda]
        else:
            moneda+=1
    return (tuple(cantidad_monedas))

print(euros(8))
# >>> (1, 1, 1)  # una de 5 cénts, una de 2 cénts y una de 1 cént.
print(euros(5))
# >>> (1, 0, 0)  # una 5 cénts, ninguna de 2 cénts y ninguna de 1 cént.
print(euros(29))
# >>> (5, 2, 0)  # cinco de 5 cénts, dos de 2 cénts y ninguna de 1 cént.
print(euros(0))
# >>> (0, 0, 0) # ninguna de 5 cénts, ninguna de 2 cénts y 1 de cénts.
print(euros(170))
# >>> (34, 0, 0)  # treinta y cuatro de 5 cénts, ninguna de 2 cénts y ninguna de 1 cént.
print(euros(267))
# >>> (53, 1, 0)  # cincuenta y tres de 5 cénts, una de 2 cénts y ninguna de 1 cént.
print(euros(-2))
# >>> None
print(euros(5.576))
# >>> None
print(euros("5"))
# >>> None