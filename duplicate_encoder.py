def duplicate_encode(word):
    letras_independientes=set()
    letras_duplicadas=set()
    palabra_encriptada=""
    palabra=word.lower()
    for i in range(len(word)):
        if palabra[i] in letras_independientes:
            letras_independientes.remove(palabra[i])
            letras_duplicadas.add(palabra[i])
        else:
            if palabra[i] in letras_duplicadas:
                None
            else:
                letras_independientes.add(palabra[i])
    for j in range(len(word)):
        if palabra[j] in letras_independientes:
            palabra_encriptada=palabra_encriptada+"("
        else:
            palabra_encriptada=palabra_encriptada+")"
    return palabra_encriptada