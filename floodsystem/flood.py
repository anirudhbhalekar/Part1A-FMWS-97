# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

from hashlib import new
from .utils import sorted_by_key

def stations_level_over_threshold(stations, tol): 

    stot_list = []
    for station in stations: 
        if station.latest_level != None: 
            high = station.typical_range[1]
            low = station.typical_range[0]
            rel_level = (station.latest_level - low)/(high - low)
            if rel_level > tol: 
                stot_list.append((station.name, rel_level))
            else: pass 
        
    stot_list = sorted_by_key(stot_list, 1, reverse=True)
    return stot_list
        
def stations_highest_rel_level(stations, N):
    level_list = []
    for i in range(N):
        level_list.append(stations_level_over_threshold(stations,-1000)[i])
    station_list = []
    for tup in level_list:
        for station in stations: 
            if station.name == tup[0]:
                station_list.append(station)
    return station_list



    