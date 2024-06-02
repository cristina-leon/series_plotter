import numpy as np
from sympy import symbols, log
from plot_func import plotter
from calc_lim import calc_limit

n = symbols('n')

func = log(n + 1)

plotter(func)

calc_limit(func)
