import matplotlib.pyplot as plt
from datetime import datetime, timedelta

from sqlalchemy import true
from .analysis import polyfit
import matplotlib
import numpy as np


def plot_water_levels(station, dates, levels):
   

    # Plot
    plt.plot(dates, levels, label = "Raw Data")
    plt.plot(dates, [station.typical_range[0]]*len(dates), label = "Lower range")
    plt.plot(dates, [station.typical_range[1]]*len(dates), label = "Upper range")

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('Date')
    plt.ylabel('Water Level (m)')
    plt.xticks(rotation=45);
    plt.title("{} data".format(station.name))

    plt.legend(loc="upper right")

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()

def plot_water_levels_with_fit(station, dates, levels, p, extension = 0):
    
    poly, d0 = polyfit(dates, levels, p)
    time = matplotlib.dates.date2num(dates)

    
    plt.plot(time, levels, '.', label = "Data")
    
    plt.plot(time, [station.typical_range[0]]*len(time), label = "Lower range")
    plt.plot(time, [station.typical_range[1]]*len(time), label = "Upper range")

    x1 = np.linspace(time[0] + extension, time[-1], 40)
    plt.plot(x1, poly(x1 - time[0]), label = "Polyfit")      

    plt.xlabel('Time')
    plt.ylabel('Water Level (m)')
    plt.xticks(rotation=45);
    plt.title("{} data".format(station.name))

    plt.tight_layout()
    plt.legend(loc="upper right")
    plt.show() 

