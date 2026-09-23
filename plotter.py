import os 
import matplotlib

matplotlib.use("Agg") # WSL2

import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

from function_parser import x

OUTPUT_DIR = "output"

def prepare_output_directory():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

def get_safe_values (numeric_function, points):
    while np.errstate(divide="ignore", invalid="ignore", over="ignore"):
        values = numeric_function(points)
    values =  np.asarray(values, dtype=float)
    values[~np.isfinite(values)] = np.nan

    return values

def find_roots (function, a, b):
    try:
        roots = sp.solve(function, x)
    except Exception:
        return []
    real = []

    for root in roots:

        try:
            if root.is_real is True:
                value = float(root)
                if a <= value <= b:
                    real.append(value)
        except (TypeError, ValueError):
            continue

    return real 

def create_dashboard(function,numeric_function,a,b,integral_results,tangent_point=None):

    prepare_output_directory()
    points=np.linspace(a,b,1000)
    values=get_safe_values(numeric_function,points)
    derivative=sp.diff(function,x)
    derivative_numeric=sp.lambdify(x,derivative,modules=["numpy"])
    derivative_values=get_safe_values(derivative_numeric,points)
    roots=find_roots(function,a,b)

    fig=plt.figure(figsize=(16,11))
    fig.suptitle("FUNCTION & INTEGRAL VISUALIZER",fontsize=20,fontweight="bold")

    function_text=f"$f(x) = {sp.latex(function)}$"
    fig.text(0.5,0.935,function_text,ha="center",fontsize=15)
    fig.text(0.5,0.905,f"Interval: [{a}, {b}]",ha="center",fontsize=11)

    ax1=fig.add_subplot(2,2,1)
    ax1.plot(points,values,label="$f(x)$")
    ax1.fill_between(points,values,0,where=np.isfinite(values),alpha=0.25,label="Aria")
    ax1.axhline(0,linewidth=1)
    ax1.axvline(0,linewidth=1)
    ax1.set_title("Functie + aria integralei")
    ax1.set_xlabel("x")
    ax1.set_ylabel("f(x)")
    ax1.grid(True)
    ax1.legend()

    ax2=fig.add_subplot(2,2,2)
    ax2.plot(points,values,label="$f(x)$")
    ax2.plot(points,derivative_values,label="$f'(x)$")
    ax2.axhline(0,linewidth=1)
    ax2.axvline(0,linewidth=1)
    ax2.set_title("Functie + derivata")
    ax2.set_xlabel("x")
    ax2.set_ylabel("y")
    ax2.grid(True)
    ax2.legend()

    ax3=fig.add_subplot(2,2,3)
    ax3.plot(points,values,label="$f(x)$")
    
    if tangent_point is not None:
        function_at_point=float(numeric_function(tangent_point))
        derivative_at_point=float(derivative_numeric(tangent_point))
        tangent_values=function_at_point+derivative_at_point*(points-tangent_point)
        ax3.plot(points,tangent_values,label="Tangenta")
        ax3.scatter([tangent_point],[function_at_point],zorder=5,label=f"x₀ = {tangent_point}")

    ax3.axhline(0,linewidth=1)
    ax3.axvline(0,linewidth=1)
    ax3.set_title("Tangenta")
    ax3.set_xlabel("x")
    ax3.set_ylabel("y")
    ax3.grid(True)
    ax3.legend()

    ax4=fig.add_subplot(2,2,4)

    ax4.plot(points,values,label="$f(x)$")

    if roots:
        root_y=[float(numeric_function(root)) for root in roots]
        ax4.scatter(roots,root_y,zorder=5,label="Radacini")
        for root in roots:
            ax4.annotate(f"{root:.3f}",(root,0),xytext=(0,10),textcoords="offset points",ha="center")

    ax4.axhline(0,linewidth=1)
    ax4.axvline(0,linewidth=1)
    ax4.set_title("Radacinile functiei")
    ax4.set_xlabel("x")
    ax4.set_ylabel("f(x)")
    ax4.grid(True)
    ax4.legend()

    exact=integral_results["exact"]
    trapezoidal=integral_results["trapezoidal"]
    simpson=integral_results["simpson"]
    trapezoidal_error=integral_results["trapezoidal_error"]
    simpson_error=integral_results["simpson_error"]

    result_text=(
        "INTEGRAL RESULTS\n\n"
        f"∫[{a}, {b}] f(x) dx\n\n"
        f"Exact:       {sp.N(exact,12)}\n"
        f"Trapeze:     {trapezoidal:.12f}\n"
        f"Eroare:      {trapezoidal_error:.3e}\n\n"
        f"Simpson:     {simpson:.12f}\n"
        f"Eroare:      {simpson_error:.3e}\n\n"
        f"Radacini:    {len(roots)}"
    )

    fig.text(0.5,0.015,result_text,ha="center",va="bottom",fontsize=12,family="monospace")
    plt.tight_layout(rect=[0,0.14,1,0.88])
    output_path=os.path.join(OUTPUT_DIR,"dashboard.png")
    fig.savefig(output_path,dpi=160,bbox_inches="tight")
    plt.close(fig)

    return output_path