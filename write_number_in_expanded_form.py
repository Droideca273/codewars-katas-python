def expanded_form(num):
    num_texto = str(num)
    longitud = len(num_texto)
    partes = []

    for i, digito in enumerate(num_texto):
        if digito != "0":
      # Calculamos los ceros que le corresponden según su posición
            ceros = "0" * (longitud - i - 1)
            partes.append(digito + ceros)
    return " + ".join(partes)