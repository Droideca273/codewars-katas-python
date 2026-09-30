def multiTable(number):
    tabla = []
    for i in range(1, 11):
        r = i * number
        tabla.append(f"{i} * {number} = {r}")
    return "\n".join(tabla)
print(multiTable(5))
