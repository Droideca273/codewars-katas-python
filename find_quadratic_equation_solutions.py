def raices(a, b, c):
    discriminante = b * b - 4 * a * c
    if discriminante < 0:
        return "No hay soluciones reales"
    else:
        resultado_primero = (-b + (discriminante ** 0.5)) / (2 * a)
        resultado_segundo = (-b - (discriminante ** 0.5)) / (2 * a) 
    return (round(resultado_primero, 2), round(resultado_segundo, 2)) 

# Solo se ejecuta si corres este archivo directamente
if __name__ == "__main__":
    a = float(input("Introduce a: "))
    b = float(input("Introduce b: "))
    c = float(input("Introduce c: "))
    print(raices(a, b, c))