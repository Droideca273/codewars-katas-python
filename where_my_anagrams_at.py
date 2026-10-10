def anagrams(word, words):
    letras_en_word=[]
    letras_en_words=[]
    palabras_validas=[]
    for i in range(len(word)):
        letras_en_word.append(word[i])
    for j in range(len(words)):
        posible_palabra_valida=words[j]
        for k in range(len(posible_palabra_valida)):
            letras_en_words.append(posible_palabra_valida[k])
        if sorted(letras_en_word)==sorted(letras_en_words):
            palabras_validas.append(words[j])
            letras_en_words=[]
        else:
            letras_en_words=[]
    return palabras_validas