# chatgpt generated
def fib(n):
    if n <= 0:
        raise ValueError("O número deve ser maior que zero.")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    
    a, b = 0, 1
    for _ in range(n - 2):
        a, b = b, a + b
    return b

def fib_r(n):
    if n <= 0:
        raise ValueError("O número deve ser maior que zero.")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    return fib_r(n - 1) + fib_r(n - 2)