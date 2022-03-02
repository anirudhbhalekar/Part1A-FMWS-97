import matplotlib.pyplot as plt
from datetime import datetime, timedelta


def plot_water_levels(station, dates, levels):
   

    # Plot
    plt.plot(dates, levels)

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('Date')
    plt.ylabel('Water Level (m)')
    plt.xticks(rotation=45);
    plt.title("{} data".format(station.name))

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()