import numpy as np
from inspect import signature

def bisection(f, a, b, tol=1e-3, N:int=50):
    """Finds a zero of f(x) within x ∈ [a, b].
    
    Args:
        f: Input function f(x). 1D functions only.
        a: Lower bound of bisection method.
        b: Upper bound of bisection method. Must satisfy sign(f(a)) != sign(f(b)).
        tol: Convergence tolerance for bisection method. Default 1e-3, must be positive.
        N (int): Maximum number of loops. Default 50, must be positive.

    Returns:
        x0: Zero of function f(x)
    """
    if f(a) == 0:
        return a
    if f(b) == 0:
        return b
    
    validate_input(f, a, b, tol, N)

def validate_input(f, a, b, tol, N):
    """Validates the user inputs to the bisection method function based on the following criteria:

    - Does sign(f(a)) != sign(f(b))
    - Is a < b?
    - Is tol > 0?
    - Is N > 0?
    - Does f(x) only have one argument?

    If it passes all these checks, it returns nothing
    
    Args:
        f: Input function f(x). 1D functions only.
        a: Lower bound of bisection method.
        b: Upper bound of bisection method. Must satisfy sign(f(a)) != sign(f(b)).
        tol: Convergence tolerance for bisection method. Default 1e-3, must be positive.
        N (int): Maximum number of loops. Default 50, must be positive.
    """
    if np.sign(f(a)) == np.sign(f(b)):
        raise Exception("Sign of function the same at f(a) and f(b).")
    if a >= b:
        raise Exception("The input range must follow a < b.")
    if tol <= 0:
        raise Exception("Tolerance must be a positive non-zero number.")
    if N <= 0:
        raise Exception("N must be a positive integer.")
    if len(signature(f)) != 0:
        raise Exception("Function must have exactly one input.")