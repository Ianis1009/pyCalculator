import sympy as sp

x = sp.symbols("x")

def parse_function (expression):
    # function -> math expression SymPy
    expression = expression.replace("^", "**")
    try:
        function = sp.sympify(expression)
    except (sp.SympifyError, TypeError):
        raise ValueError("Expresia introdusa nu este valida.")

    if not function.has(x):
        raise ValueError("Introdu o functie dependenta de variabila x.")

    return function

def validate_function (function):
    pass # verify if is instance of SymPy

def create_numeric_function (function):
    pass # transform in numerical function

def get_function (expression):
    pass # return the math function

