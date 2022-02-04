from distutils.command.build import build
from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list

centre = (52.2053, 0.1218)
r = 10

def sort_tuple(tup):  
   tup.sort(key = lambda x: x[0])
   return tup

def station_names_within_r(station, centre, r): 

    st_names = []
    st_list = stations_within_radius(station, centre, r)
    for station in st_list: 
        st_names.append(station.name)
    return sort_tuple(st_names)

if __name__ == "__main__":
   print(station_names_within_r(build_station_list(), centre, r))
