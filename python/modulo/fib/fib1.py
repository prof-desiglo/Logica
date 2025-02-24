def fib(n):
    i = 1
    v0 = 0
    v1 = 1
    while(i<n):
        i = i + 1
        temp = v0 + v1
        v0 = v1
        v1 = temp
    return v1