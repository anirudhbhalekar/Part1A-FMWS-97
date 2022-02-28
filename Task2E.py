from distutils.command.build import build
from floodsystem.utils import sorted_by_key
from floodsystem.stationdata import build_station_list
from floodsystem.plot import plot_water_levels
from datetime import datetime, timedelta

def run(): 
    stations = build_station_list()
    print(stations[0])
    stations = sorted_by_key(stations, 1, reverse=True)

    today = datetime.today()
    dates = []
    for i in range(10):
        dates.append(datetime(today.year ,today.month, today.day - i))
        

    levels = []
    

    plot_water_levels(build_station_list(), dates, levels)

if __name__ == "__main__":
    run()