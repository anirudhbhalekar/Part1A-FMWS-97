import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import dates
import datetime 

def polyfit(dates, levels, p):
    now = matplotlib.dates.date2num(datetime.datetime.utcnow())
    x = matplotlib.dates.date2num(dates)
    y = levels

    if len(x) != 0: 
        p_coeff = np.polyfit(x - x[0],y,p)
        poly = np.poly1d(p_coeff)
        return poly, x[0]
    else: 
        return 0, now