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
   # verify if is instance of SymPy
   return (isinstance(function, sp.Expr) and function.has(x))

def create_numeric_function (function):
    # transform in numerical function
    return sp.lambdify(x, function, modules=["numpy"])


def get_function (expression):
    pass # return the math function

