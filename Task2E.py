from distutils.command.build import build
from floodsystem.utils import sorted_by_key
from floodsystem.stationdata import build_station_list
from floodsystem.plot import plot_water_levels
import datetime 
from floodsystem.datafetcher import fetch_measure_levels
def run(): 
    stations = build_station_list()
    dt = 10
    station_name = "Hexham"

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
    run()