from distutils.command.build import build
from re import S
from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations


def sort_tuple(tup):  
   tup.sort(key = lambda x: x[0])
   return tup

def inconsistent_builder(stations): 
    n_list = []
    i_list = inconsistent_typical_range_stations(stations)
    for station in i_list: 
        n_list.append(station.name)
    return sort_tuple(n_list)

if __name__ == "__main__": 
    print(inconsistent_builder(build_station_list()))