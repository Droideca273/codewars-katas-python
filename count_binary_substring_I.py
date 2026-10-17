def count_binary(s1, s2):
    ultima_posicion = 0
    ocurrencias_encontradas = 0
    while True:
        ultima_posicion = s2.find(s1, ultima_posicion)
        if ultima_posicion == -1:
            break       
        ocurrencias_encontradas += 1
        ultima_posicion += 1
    return ocurrencias_encontradas