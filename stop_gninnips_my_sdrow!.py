def spin_words(sentence):
    sentence=sentence.split(" ")
    resultado=""
    if len(sentence[0])>=5:
        resultado=sentence[0][::-1]
    else:
        resultado=sentence[0]
    for i in range(1,len(sentence)):
        if len(sentence[i])>=5:
            resultado=resultado+" "+sentence[i][::-1]
        else:
            resultado=resultado+" "+sentence[i]
    return resultado