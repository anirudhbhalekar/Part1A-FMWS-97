from floodsystem.plot import plot_water_levels_with_fit
from floodsystem.plot import plot_water_levels
from floodsystem.stationdata import build_station_list
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import update_water_levels
from floodsystem.flood import stations_highest_rel_level
from Task2C import return_name_and_level

import datetime 

def make_plots(name,dt,p):
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

    plot_water_levels_with_fit(station_cam, dates, levels, p, extension=0.25)

if __name__ == "__main__":
    stations = build_station_list()
    update_water_levels(stations)

    #make_plots("Barnes",2, 4)
    for i in stations_highest_rel_level(stations, 5):
        if i.name == "Letcombe Bassett": # this station has not had a reading in 2 days - causing problems
            pass
        else:
            make_plots(i.name, 1, 4)
