def spin_words(sentence):
    sentence_alterada = sentence.split(" ")
    resultado = ""
    if len(sentence_alterada[0]) >= 5:
        resultado = sentence_alterada[0][::-1]
    else:
        resultado = sentence_alterada[0]
    for posicion in range(1, len(sentence_alterada)):
        if len(sentence_alterada[posicion]) >= 5:
            resultado = resultado + " " + sentence_alterada[posicion][::-1]
        else:
            resultado = resultado + " " + sentence_alterada[posicion]
    return resultado
