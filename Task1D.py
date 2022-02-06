from floodsystem.geo import rivers_with_station
from floodsystem.stationdata import build_station_list


def run():
    stations = build_station_list()
    #stations = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
    
    rivers = rivers_with_station(stations)

    rivers = sorted(rivers)


    print(rivers[0:10])


if __name__ == "__main__":
   run()
