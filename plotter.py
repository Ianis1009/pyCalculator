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

