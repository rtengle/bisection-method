import numpy as np
import src.bisection as bs

# Defines some function f(x)
def f(x):
    return np.cos(x) + x/2

# Returns the x-position and x-value after converging or reaching the iteration limit
print(bs.bisection(f, -2, 2))