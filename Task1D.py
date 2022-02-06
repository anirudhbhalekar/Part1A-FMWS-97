from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river
from floodsystem.stationdata import build_station_list


def run():
    stations = build_station_list()
    
    rivers = rivers_with_station(stations)

    rivers = sorted(rivers)

    print("First 10 rivers with stations (alphabetically): ", rivers[0:10], "\n")

    river_dict = stations_by_river(stations)
    print("River Aire: ", river_dict["River Aire"], "\n")
    print("River Cam: ", river_dict["River Cam"], "\n")
    print("River Thames: ", river_dict["River Thames"], "\n")
    

if __name__ == "__main__":
   run()
