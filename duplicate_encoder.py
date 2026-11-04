def duplicate_encode(word):
    palabra = word[:].lower()
    letras_codificacion = {}
    palabra_codificada = ""
    for letra in palabra:
        if letra not in letras_codificacion:
            letras_codificacion[letra] = "("
        else:
            letras_codificacion[letra] = ")"
    for letra in palabra:
        palabra_codificada = palabra_codificada + letras_codificacion[letra]
    return "".join(palabra_codificada)

if __name__ == '__main__':
    assert duplicate_encode("din") == "((("
    assert duplicate_encode("recede") == "()()()"
    assert duplicate_encode("Success") == ")())())"
    assert duplicate_encode("(( @") == "))(("
    print("Bien hecho")
