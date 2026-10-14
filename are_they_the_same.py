def comp(array1, array2):
    if array1 is None or array2 is None:
        return False

    array1 = sorted(array1, key=abs)
    array2 = sorted(array2)

    if len(array1) != len(array2):
        return False

    for i in range(len(array1)):
        if array1[i] * array1[i] == array2[i]:
            None
        else:
            return False
    return True
