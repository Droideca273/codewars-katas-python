def alphabet_position(text):
    alfabeto=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",]
    palabra_codificada=""
    text=text.lower()
    text=text.split (" ")
    text=''.join(text)
    for i in range(len(text)):
        if text[i] in alfabeto:
            for j in range(len(alfabeto)):
                if alfabeto[j]==text[i] and palabra_codificada=="":
                    palabra_codificada=palabra_codificada+str(j+1)
                elif alfabeto[j]==text[i]:
                    palabra_codificada=palabra_codificada+" "+str(j+1)
        else:
            None
    return palabra_codificada