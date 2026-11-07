def solution(n):
    numero = n
    traduccion = ""
    diccionario = {1000: "M",900: "CM", 500: "D",400: "CD", 100: "C", 90: "XC", 50: "L",40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"}
    if numero in diccionario:
        return diccionario[numero]
    else:
        for key, value in diccionario.items():
            if numero >= key:
                cantidad = numero//key
                numero -= key * cantidad
                traduccion += value * cantidad
    return traduccion
if __name__ == '__main__':
    assert solution(1) == 'I'
    assert solution(4) == 'IV'
    assert solution(9) == 'IX'
    assert solution(21) == 'XXI'
    assert solution(50) == 'L'
    assert solution(90) == 'XC'
    assert solution(400) == 'CD'
    assert solution(1000) == 'M'
    assert solution(1994) == 'MCMXCIV'
    assert solution(2008) == 'MMVIII'