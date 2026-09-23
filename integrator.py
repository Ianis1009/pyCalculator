import numpy as np 
import sympy as sp 

from function_parser import x

def analytical_integral(function, a, b):
    return sp.integrate(function, (x, a, b))

def trapezoidal_integral(numeric_function, a, b, n=1006):
    points = np.linspace(a, b, n + 1)
    values = numeric_function(points)
    h = (b - a) / n 
    result = h * (0.5 * values[0] + np.sum(values[1:-1]) + 0.5 * values[-1])
    return float(result)

def simpson_integral(numeric_function, a, b, n = 1006):
    if n % 2 != 0:
        raise ValueError("n trebuie sa fie par pentru metoda Simpson.")
    points = np.linspace(a, b, n + 1)
    values = numeric_function(points)
    h = (b - a) / n 
    result = (h / 3 * (values[0] + values[-1]+ 4*np.sum(values[1:-1:2]) + 2 * np.sum(values[2:-1:2]))) 
    return float(result)

def calculate_error (exact_value, approximate_value):

    exact = float(sp.N(exact_value))
    return abs(exact_value - approximate_value)

def calculate_integrals (function, numeric_function, a, b, n =1006):
    exact = analytical_integral(function, a, b)
    trapezoidal = trapezoidal_integral(numeric_function, a, b, n)
    simpson = simpson_integral(numeric_function, a, b, n)
    trapezoidal_error = calculate_error(exact, trapezoidal)
    simpson_error = calculate_error(exact, simpson)

    return {
        "exact": exact,
        "trapezoidal": trapezoidal,
        "simpson": simpson,
        "trapezoidal_error": trapezoidal_error,
        "simpson_error": simpson_error,
    }
