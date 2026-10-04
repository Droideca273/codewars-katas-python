def roots(a,b,c):
    discriminante=b*b-4*a*c
    resultado_primero=(-b+(discriminante**0.5))/(2*a)
    resultado_segundo=(-b-(discriminante**0.5))/(2*a)
    if discriminante>=0:
        return round(resultado_primero+resultado_segundo,2)
    else:
        return None