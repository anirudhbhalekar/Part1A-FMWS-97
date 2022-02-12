# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT

from .utils import sorted_by_key

def stations_level_over_threshold(stations, tol): 

    stot_list = []
    for station in stations: 
        if station.latest_level != None: 
            if station.latest_level > tol: 
                stot_list.append((station, station.latest_level))
            else: pass 
        
    stot_list = sorted_by_key(stot_list, 1)
    return stot_list
        


