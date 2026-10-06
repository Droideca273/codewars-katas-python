def generate_range(start, stop, step):
    lista=[]
    for i in range(start,stop+1,step):
        lista.append(i)  # noqa: PERF402
    return lista