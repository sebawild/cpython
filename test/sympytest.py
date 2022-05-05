from sympy import expand, symbols, integrate, tan, summation
from sympy.core.cache import clear_cache

x, y, z, a, b = symbols('x y z a b')
expand((1 + x + y + z + a + b) ** 25)
