from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list

coords = (52.2053, 0.1218) # coordinates in tuple form
stations = build_station_list()

def ten_sorted(stations,p,closest = True): 
    
    x = stations_by_distance(stations,p)
    if closest == True: return x[:10]
    else: return x[-10:]

if __name__ == "__main__":
    print("*** Task 1A: CUED Part IA Flood Warning System ***\n")
    print("Closest stations: \n")
    print(ten_sorted(stations,coords),"\n") # prints closest 10 stations
    print("Farthest stations: \n")
    print(ten_sorted(stations,coords, closest= False)) # prints farthest 10 stations    