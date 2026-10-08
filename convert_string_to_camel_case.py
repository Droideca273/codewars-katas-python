def to_camel_case(text):
    text = text.replace("_", "-")
    palabras = text.split("-")
    resultado=palabras[0]
    for i in range(1,len(palabras)):
        palabra_mayuscula=palabras[i].capitalize()
        resultado=resultado+palabra_mayuscula
    return resultado