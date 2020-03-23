def pattern(n):
    return '' if n < 1 else "1"+''.join([("\n" + str(l)*l) for l in range(2,n+1)])
