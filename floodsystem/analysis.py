import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import dates

def polyfit(dates, levels, p):
    x = matplotlib.dates.date2num(dates)
    y = levels

    if len(x) != 0: 
        p_coeff = np.polyfit(x - x[0],y,p)
        poly = np.poly1d(p_coeff)
        return poly, x[0]
    else: 
        raise ValueError("Date array has 0 length")
