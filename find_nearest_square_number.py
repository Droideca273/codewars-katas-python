def nearest_sq(n):
    limite = int(n**0.5) + 1 # Raíz cuadrada de n más 1 para tener en cuenta el número por encima de él
    cuadrado_debajo=(limite-1)*(limite-1)
    cuadrado_encima=limite*limite
    if n==cuadrado_encima:
        return n
    else:
        if n<cuadrado_encima:
            mayor=cuadrado_encima-n
            menor=n-cuadrado_debajo
            if mayor>menor:
                return cuadrado_debajo
            elif menor>mayor:
                return cuadrado_encima