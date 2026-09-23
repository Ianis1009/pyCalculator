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

