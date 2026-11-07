from preloaded import MORSE_CODE

def decode_morse(morse_code):
    resultado = ""
    
    for palabra in morse_code.strip().split('   '):
        for letra_morse in palabra.split(' '):
            resultado += MORSE_CODE[letra_morse]
        resultado += " "    
    return resultado.strip()
if __name__ == '__main__':
    assert decode_morse('.... . -.--   .--- ..- -.. .') == 'HEY JUDE'
    assert decode_morse('.-') == 'A'
    assert decode_morse('--.') == 'G'
    assert decode_morse('... --- ...') == 'SOS'
    assert decode_morse('.   .') == 'E E'
    assert decode_morse('      .-      ') == 'A'