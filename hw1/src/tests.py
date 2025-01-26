from src.bisection import bisection

def run_tests():
    # Runs all tests and prints out the result
    print(default_test())
    print(quartic_test())
    print(double_input_test())
    print(bad_bounds_test())
    print(step_test())

def default_test():
    # Basic test of a window w/ one zero
    a = -2
    b = 5
    def f(x):
        return x*(2**x)
    x0, y0 = bisection(f, a, b)
    return f(x0)

def quartic_test():
    # Test of a window w/ multiple zeros
    a = -0.5
    b = 3
    def f(x):
        return x**4 - 2*x**3 - x**2 + x
    
    x0, y0 = bisection(f, a, b)
    return x0, y0

def double_input_test():
    # Tests checking how many inputs a function can have
    a = -3
    b = 6
    def f(x, y):
        return x + y

    try: 
        bisection(f, a, b)
        return "Failed"
    except Exception as e:
        return e
    
def bad_bounds_test():
    # Tests the bound-checking
    a = 4
    b = 1
    def f(x):
        return x + 3
    
    try: 
        bisection(f, a, b)
        return "Failed"
    except Exception as e:
        return e
    
def step_test():
    # Tests what happens if there's no zero in the window
    a = -5
    b = 4

    def f(x):
        if x < 0:
            return -1
        else:
            return 1
        
    x0, y0 = bisection(f, a, b)
    return x0, y0