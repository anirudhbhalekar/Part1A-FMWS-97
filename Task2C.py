from distutils.command.build import build
from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import update_water_levels


def return_name_and_level(stations,N):
    list_of_stations = []
    for i in stations_highest_rel_level(stations,N):
        list_of_stations.append((i.name, i.latest_level))
    return list_of_stations

if __name__ == "__main__":

    stations = build_station_list()
    update_water_levels(stations)
    print(return_name_and_level(stations,10))