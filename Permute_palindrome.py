def permute_a_palindrome(string):
    string=string.lower()
    string=string.split (" ")
    string=''.join(string)
    lista1 = []
    for i in range (len(string)):
        if string[i] in lista1:
            lista1.remove(string[i])
        else:
            lista1.append(string[i])
    if len(string)%2 == 1 and len(lista1)==1:
        return True
    elif len(string)%2 == 0 and len(lista1)==0:
        return True
    else :
        return False