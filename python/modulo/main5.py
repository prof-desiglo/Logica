from fib import fib1 
from fib import fib2 

print(fib1.fib(5))
print(fib2.fib(5))

from fib import fib3

print(fib3.fib(6))
print(fib3.fib_r(6))

import timeit

# Experimento 1
setup = 'from fib import fib1'
run = 'fib1.fib(100)'
print(timeit.timeit(setup=setup,stmt=run, number=10))

# Experimento 2
setup = 'from fib import fib3'
run = 'fib3.fib(101)'
print(timeit.timeit(setup=setup,stmt=run, number=10))

# Experimento 3
setup = 'from fib import fib2 '
run = 'fib2.fib(100)'
print(timeit.timeit(setup=setup,stmt=run, number=10))

# Experimento 4
setup = 'from fib import fib3 '
run = 'fib3.fib_r(20)'
print(timeit.timeit(setup=setup,stmt=run, number=1))