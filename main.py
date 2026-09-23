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
    