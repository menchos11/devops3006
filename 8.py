# option a:
# import fibo
#
# fibo.fib(100)

# option b
# from fibo import fib
#
# fib(100)
# or
from fibo import fib as my_fib
from fibo_aharon import fib as aharon_fib
from fibo import a

my_fib(100)
aharon_fib(100)
print(a)