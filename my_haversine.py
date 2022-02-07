from math import radians
from haversine import haversine
import numpy as np

def my_haversine_func(coord1, coord2): 
    R = 6372.8 # radius of the earth in km 
    lat1, lon1 = coord1[0], coord1[1]
    lat2, lon2 = coord2[0], coord2[1]

    dLat = np.double(radians(lat2 - lat1))
    dLon = np.double(radians(lon2 - lon1))
    lat1 = np.double(radians(lat1))
    lat2 = np.double(radians(lat2))

    a = np.sin(dLat/2)**2 + np.cos(lat1)*np.cos(lat2)*np.sin(dLon/2)**2
    c = 2*np.arcsin(np.sqrt(a))

    return R * c

if __name__ == "__main__":
    print()