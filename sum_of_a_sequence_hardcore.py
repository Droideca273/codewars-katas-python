def sequence_sum(begin_number, end_number, step):
    numeros_secuencia = (end_number - begin_number) // step + 1
    if numeros_secuencia <= 0:
        return 0
    last_number = begin_number + (numeros_secuencia - 1) * step
    return numeros_secuencia * (begin_number + last_number) // 2
