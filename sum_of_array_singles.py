def repeats(array):
    mi_conjunto = set()
    for i in range(len(array)):
        if (array[i]) in mi_conjunto:
            mi_conjunto.remove(array[i])
        else:
            mi_conjunto.add(array[i])
    return(sum(mi_conjunto))