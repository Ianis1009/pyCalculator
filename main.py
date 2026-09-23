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

def run_application ():
    print()
    print("=" * 60)
    print("FUNCTION VISUALIZER & CALCULATOR")
    print("=" * 60)

    function, numeric_function = (get_function_input())
    a = get_float_input("Limita inferioara a: ")
    b = get_float_input("Limita superioara b: ")

    if a >= b:
        print("\nEroare: conditie -> a < b.")
        return

    while True:
        tangent_point =  get_float_input(f"Punctul x_0 pentru tangenta " f"[{a}, {b}]: ")
        if a <= tangent_point <= b:
            break
        print("Punctul trebuie sa apartina " f"intervalului [{a}, {b}].")
    print("\nSe calculeaza...")

    integral_results = calculate_integrals(function, numeric_function, a, b)
    print()
    print("=" * 60)
    print("REZULTATE")
    print("=" * 60)

    print(f"\nf(x) = {function}")
    print(f"Interval = [{a}, {b}]")
    print("\nIntegrala exacta:")
    print(f"  {integral_results['exact']}")
    print("\nMetoda trapezelor:")
    print(f"  {integral_results['trapezoidal']:.12f}")
    print(f"  Eroare: " f"{integral_results['trapezoidal_error']:.3e}")

    print("\nMetoda Simpson:")

    print(f"  {integral_results['simpson']:.12f}")
    print(f"  Eroare: " f"{integral_results['simpson_error']:.3e}")

    # DASHBOARD
    print("\nSe genereaza dashboard-ul...")
    dashboard_path = create_dashboard(function, numeric_function, a, b, integral_results, tangent_point)
    print(f"\nDashboard salvat in: ")
    print(f"    {dashboard_path}")
    print()
    print("=" * 60)
    print("Program terminat...")
    print("=" * 60)

if __name__ == "__main__":
    run_application()