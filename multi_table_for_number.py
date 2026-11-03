def multiTable(multiplicando):
    tabla_de_multiplicar = []
    for multiplicador in range(1, 11):
        resultado = multiplicador * multiplicando
        tabla_de_multiplicar.append(f"{multiplicador} * {multiplicando} = {resultado}")
    return "\n".join(tabla_de_multiplicar)


print(multiTable(5))
