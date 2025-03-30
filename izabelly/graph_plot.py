from sympy import *

## run this on google colab (no need to download the sympy), but if you wanna run that on your machine use the commad: pip install sympy(windows)
## and no need to use another lib to make the graphl

x = Symbol('x')
y = Symbol('y')

func = (2*x)/(x-3)
plot(func)

lim1 = limit(func, x, 3)
print(lim1)
f5 = func.subs(x, 3)
print(f5)