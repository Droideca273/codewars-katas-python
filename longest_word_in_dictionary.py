def find_longest_word(palabra, lista):
    # Ordenamos la lista por longitud y alfabético
    lista.sort(key=lambda x: (-len(x), x))
    
    letras_clave = {}
    for letra in palabra:
        letras_clave[letra] = palabra.count(letra)
        
    for cand in lista:

        es_valida = True
        for letra in set(cand):
            if cand.count(letra) > letras_clave.get(letra, 0):
                es_valida = False
                break
                
        if es_valida:
            return cand
            
    return ""

if __name__ == "__main__":
    assert find_longest_word("abpcplea", ["ale", "apple", "monkey", "plea"]) == "apple"
    assert find_longest_word("abpcplea", ["a", "b", "c"]) == "a"
    assert find_longest_word("abpcplea", ["ale", "apple", "monkey", "plea", "abpl"] ) == "apple"
    assert find_longest_word("apple", ["z", "p", "l"]) == "l"
    assert find_longest_word("abpcplea", ["b", "cat", "dog"]) == "b"
    assert find_longest_word("a", ["a", "b"]) == "a"
    assert find_longest_word("abpcplea", ["ale", "apple", "monkey", "plea", "pleas"]) == "apple"
