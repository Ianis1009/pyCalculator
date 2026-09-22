import numpy as np 
import sympy as sp 

from function_parser import x

def analytical_integral(function, a, b):
    return sp.integrate(function, (x, a, b))

def trapezoidal_integral(numeric_function, a, b, n=1005):
    points = np.linspace(a, b, n + 1)
    values = numeric_function(points)
    h = (b - a) / n 
    result = h * (0.5 * values[0] + np.sum(values[1:-1]) + 0.5 * values[-1])
    return float(result)

def simpson_integral(numeric_function, a, b, n = 1005):
    pass

def calculate_error (exact_value, approximate_value):
    pass

def calculate_integrals (function, numeric_function, a, b, n =1005):
    pass 