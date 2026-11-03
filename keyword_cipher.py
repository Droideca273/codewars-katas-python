def keyword_cipher(msg, keyword):
    import string

    mensaje = msg[:]
    mensaje = mensaje.lower()
    abecedario = string.ascii_lowercase
    abecedario_codificado = string.ascii_lowercase
    letras_contrasena = ""
    palabra_codificada = ""
    for letra in keyword:
        if letra in abecedario_codificado:
            abecedario_codificado = abecedario_codificado.replace(letra, "")
        if letra not in letras_contrasena:
            letras_contrasena = letras_contrasena + (letra)
    abecedario_codificado = letras_contrasena + abecedario_codificado
    for letra_msg in mensaje:
        if letra_msg == " ":
            palabra_codificada = palabra_codificada + " "
        else:
            for letra in range(len(abecedario)):
                if letra_msg == abecedario[letra]:
                    palabra_codificada = (
                        palabra_codificada + abecedario_codificado[letra]
                    )
    return palabra_codificada