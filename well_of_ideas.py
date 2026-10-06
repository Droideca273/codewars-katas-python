def well(x):
    g=0
    b=0
    for i in range(0,len(x),1):
        if x[i]=="good":
            g=g+1
        else:
            b=b+1
    if g==1 or g==2:
        git="Publish!"
    elif g>=3:
        git="I smell a series!"
    else:
        git="Fail!"
    return(git)