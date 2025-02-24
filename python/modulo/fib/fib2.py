import math

def fib(n):
    golden_ratio = (1 + 5 ** 0.5) / 2
    #print(golden_ratio)
    return int(((golden_ratio ** n) - ((1-golden_ratio)**n)) / math.sqrt(5))