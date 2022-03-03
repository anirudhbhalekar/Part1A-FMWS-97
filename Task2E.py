from distutils.command.build import build
from floodsystem.utils import sorted_by_key
from floodsystem.stationdata import build_station_list
from floodsystem.plot import plot_water_levels
import datetime 
from floodsystem.stationdata import update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from Task2C import return_name_and_level

def run(name, dt): 
    stations = build_station_list()
    station_name = name

    station_cam = None
    for station in stations:
        if station.name == station_name:
            station_cam = station
            break

    # Check that station could be found. Return if not found.
    if not station_cam:
        print("Station {} could not be found".format(station_name))
        return
    dates, levels = fetch_measure_levels(station_cam.measure_id, dt=datetime.timedelta(days=dt))

    plot_water_levels(station_cam, dates, levels)


if __name__ == "__main__":
    dt = 10
    limit = 6 # letcomb bassett being problematic as usual
    stations = build_station_list()
    update_water_levels(stations)

    it_list = []
    for i in return_name_and_level(stations, limit):
        it_list.append(i[0])
    
    for i in it_list: 
        run(i,dt)

    