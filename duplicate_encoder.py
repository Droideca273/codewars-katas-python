def duplicate_encode(word):
    letras_independientes=set()
    letras_duplicadas=set()
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