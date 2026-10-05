def permute_a_palindrome(input):
    mi_conjunto = set()
    for i in range(len(input)):
        if (input[i]) in mi_conjunto:
            mi_conjunto.remove(input[i])
        else:
            mi_conjunto.add(input[i])
    if len(input)%2==0 and len(mi_conjunto)==0:
        return True
    elif (len(input)%2==1 or len(input)==1) and len(mi_conjunto)==1:
        return True
    else:
        return False