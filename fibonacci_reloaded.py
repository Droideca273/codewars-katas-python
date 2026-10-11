def fib(n):
    resultado=0
    numeros_fibonacci=[0,1]
    while len(numeros_fibonacci)<n:
        numeros_fibonacci.append(numeros_fibonacci[-1]+numeros_fibonacci[-2])
    return(numeros_fibonacci[n-1])
fib(5)