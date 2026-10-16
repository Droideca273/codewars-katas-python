def alphabet_position(text):
    alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    palabra_codificada = ""
    text_alterado = text.lower()
    text_alterado = text_alterado.split(" ")
    text_alterado = "".join(text_alterado)
    for posicion_texto in range(len(text_alterado)):
        if text_alterado[posicion_texto] in alfabeto:
            for posicion_alfabeto in range(len(alfabeto)):
                if (
                    alfabeto[posicion_alfabeto] == text_alterado[posicion_texto]
                    and palabra_codificada == ""
                ):
                    palabra_codificada = palabra_codificada + str(posicion_alfabeto + 1)
                elif alfabeto[posicion_alfabeto] == text_alterado[posicion_texto]:
                    palabra_codificada = (
                        palabra_codificada + " " + str(posicion_alfabeto + 1)
                    )
        else:
            None
    return palabra_codificada
