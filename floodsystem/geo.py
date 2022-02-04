# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
from distutils.command.build_clib import build_clib
from haversine import haversine
from .stationdata import build_station_list
from .utils import sorted_by_key  # noqa

def stations_by_distance(stations, p):
    
    distance_list = [] # initialised list for storing distances and names (in tuple form)
    
    for station in stations: # iterating through each item in the stations list
        distance_list.append((station.name,haversine(station.coord,p))) # haversine function computes the distance between two coordinates on earth   
    return sorted_by_key(distance_list,1) # sort by 2nd entry in tuple 
    
def stations_within_radius(stations, centre, r):
    
    station_within_r = []

    for station in stations: 
        d = haversine(centre, station.coord)
        if d <= r: 
            station_within_r.append(station)
    
    return station_within_r