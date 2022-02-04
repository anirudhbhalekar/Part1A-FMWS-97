# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
import haversine
from floodsystem.stationdata import build_station_list
from .utils import sorted_by_key  # noqa

def stations_by_distance(stations, p):
    
    distance_list = [] # initialised list for storing distances and names (in tuple form)
    for station in stations: # iterating through each item in the stations list
        name = station.name # storing the name of the station
        for coord2 in station.coord: # iterating over the coordinates 
            distance_list.append((name,haversine(coord2,p))) # haversine function computes the distance between two coordinates on earth
    
    return sorted_by_key(distance_list,1) # sort by 2nd entry in tuple 


         





