def evil(n):
    o=0
    res=f"{n:b}"
    tra=len(res)
    for i in range(0,tra,1):
        if (res[i]=="1"):
            o=o+1
    if o % 2 == 0:
        men = "It's Evil!"
    else:
        men = "It's Odious!"
    return(men)