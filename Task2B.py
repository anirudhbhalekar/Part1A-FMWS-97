from distutils.command.build import build
from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels

def run(): 
    tol = 0.8
    stations = build_station_list()
    update_water_levels(stations)
    list_over_tol = stations_level_over_threshold(stations, tol)
    
    print(list_over_tol)

if __name__ == "__main__":
    run()