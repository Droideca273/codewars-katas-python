def well(x):
    good_ideas=0
    bad_ideas=0
    for i in range(0,len(x),1):
        if x[i]=="good":
            good_ideas=good_ideas+1
        else:
            bad_ideas=bad_ideas+1
    if good_ideas==1 or good_ideas==2:
        git="Publish!"
    elif good_ideas>=3:
        git="I smell a series!"
    else:
        git="Fail!"
    return(git)