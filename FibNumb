from numpy import prod

def fib(n):
    if n == 0 or n == 1:
        return 1
    else: 
        a = []
        a.append(1)
        a.append(1)
        for i in range(2 , n+1):
            a.append(a[i-2] + a[i-1])
        return a[-1]

def productFib(prod):
    n = 0
    a = 0
    b = 1
    p = 0
    while p < prod :
        a = fib(n)
        b = fib(n+1)
        p = a * b
        n+=1

    return [a,b, p == prod]
