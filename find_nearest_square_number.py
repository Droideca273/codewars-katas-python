def nearest_sq(n):
    limite = int(n**0.5) + 2
    for i in range(0,limite,1):
        r=i-1
        resw=r*r
        res=i*i
        if n==res:
            return n
        else:
            if n<res:
                may=res-n
                men=n-resw
                if may>men:
                    return resw
                elif men>may:
                    return res