from function_parser import get_function
from integrator import calculate_integrals
from plotter import create_dashboard

def get_float_input (message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Valoare invalida -> ", "Introdu un numar.")

def get_function_input():
    while True:
        expression = input("\nIntrodu functia f(x): ")
        try:
            return get_function(expression)
        except ValueError as error:
            print(f"\nEroare: {error}")

