def encoder(data):
    diccionario = {"" : 0}
    combinacion_anterior = ""
    combinacion_actual = ""
    resultado = ""
    for letra in data:
        combinacion_actual = combinacion_anterior + letra
        if combinacion_actual not in diccionario:
            diccionario[combinacion_actual] = len(diccionario)
            resultado += str(diccionario[combinacion_anterior]) + letra
            combinacion_anterior = ""
        else:
            combinacion_anterior = combinacion_actual
    if combinacion_anterior != "":
        resultado += str(diccionario[combinacion_anterior])
    return resultado

if __name__ == '__main__':
    assert encoder('ABAABABAABAB') == '0A0B1A2A4A4B'
    assert encoder('ABAABABAABABAA') == '0A0B1A2A4A4B3'
    assert encoder('ABBCBCABABCAABCAABBCAA') == '0A0B2C3A2A4A6B6'
    assert encoder('AAAAAAAAAAAAAAA') == '0A1A2A3A4A'
    assert encoder('ABCABCABCABCABCABC') == '0A0B0C1B3A2C4C7A6'
    assert encoder('ABCDDEFGABCDEDBBDEAAEDAEDCDABC') == '0A0B0C0D4E0F0G1B3D0E4B2D10A1E4A10D9A2C'

def decoder(data):
    diccionario = {0: ""}
    str_indice = ""
    resultado = ""
    for caracter in data:
        if caracter.isdigit():
            str_indice += caracter ## guarda los dígitos para introducirlos luego en el diccionario
        else:
            indice = int(str_indice) ## pasa los digitos a numero para poder usarlo en el diccionario

            nueva_palabra = diccionario[indice] + caracter ## nueva_palabra es la combinacion codificada más la última letra
            diccionario[len(diccionario)] = nueva_palabra ## se añade la nueva_palabra al diccionario para las proximas combinaciones
            resultado += nueva_palabra ## se añade a resultado

            str_indice = "" ## reiniciamos digitos

    if str_indice != "":
        resultado += diccionario[int(str_indice)]
    return(resultado)

if __name__ == '__main__':
    assert decoder('0A0B1A2A4A4B') == 'ABAABABAABAB'
    assert decoder('0A0B1A2A4A4B3') == 'ABAABABAABABAA'
    assert decoder('0A0B2C3A2A4A6B6') == 'ABBCBCABABCAABCAABBCAA'
    assert decoder('0A1A2A3A4A') == 'AAAAAAAAAAAAAAA'
    assert decoder('0A0B0C1B3A2C4C7A6') == 'ABCABCABCABCABCABC'
    assert decoder('0A0B0C0D4E0F0G1B3D0E4B2D10A1E4A10D9A2C') == 'ABCDDEFGABCDEDBBDEAAEDAEDCDABC'
             
