# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
from distutils.command.build_clib import build_clib
from haversine import haversine, Unit
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

def rivers_with_station(stations):
    """returns a container (set) with the names of the rivers with a monitoring station"""
    
    r_w_s = {station.river for station in stations}

    return r_w_s

def stations_by_river(stations):
    """maps river names (the ‘key’) to a list of station objects on a given river"""

    rivers = rivers_with_station(stations)
    river_dict = {}
    for river in rivers:
        river_dict[river] = []

    for station in stations:
        river_dict[station.river].append(station.name)

    for river in river_dict:
        river_dict[river].sort()

    return river_dict

def rivers_by_station_number(stations, N):
    """determines the N rivers with the greatest number of monitoring stations, returns a list of (river name, number of stations) tuples, sorted by the number of stations"""

    rivers = rivers_with_station(stations)
    s_b_r = stations_by_river(stations)
    river_list = []

    for river in rivers:
        num = len(s_b_r[river])
        river_list.append((river, num))

    river_list.sort(key=lambda x:x[1], reverse=True) #sort list by second value of tuple and sort descending

    cutoff_number = river_list[N-1][1]
    cutoff_index = 0
    
    i = 0
    while(river_list[i][1]>= cutoff_number):
        cutoff_index = i
        i+= 1

    #return river_list
    return river_list[0:cutoff_index+1]