# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance
from floodsystem.geo import stations_within_radius
from floodsystem.station import inconsistent_typical_range_stations

def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town

def test_stations_by_distance():
    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    test_list = [s]     # creating a 'test' list - supposed to emulate stations 
    p = (-2.0, 4.0)     # so that distance is 0 

    x = stations_by_distance(test_list,p) # does the function 
    d = [lis[1] for lis in x][0] # takes the 2nd element from the tuple

    assert d <= 1e-5 # tolerance is kept a little high because i am not sure how haversine numerically computes

def test_station_within_radius(): 

    # Create a station
    stations = [] # empty stations list
    
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (1, 2)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    stations.append(s)
    
    p = (2, 1) # we know that this is < 200 km away from (1,2)
    return_list = stations_within_radius(stations, p, 200)
    
    assert (return_list[0] == s)


def test_typical_range_stations(): 
    
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    s_id2 = "test-s-id"
    m_id2 = "test-m-id"
    label2 = "some station"
    coord2 = (-2.0, 4.0)
    trange2 = (5.3, 3.4445)
    river2 = "River X2"
    town2 = "My Town2"
    k = MonitoringStation(s_id2, m_id2, label2, coord2, trange2, river2, town2)

    s_id3 = "test-s-id"
    m_id3 = "test-m-id"
    label3 = "some station"
    coord3 = (-2.0, 4.0)
    trange3 = None
    river3 = "River X"
    town3 = "My Town"
    j = MonitoringStation(s_id3, m_id3, label3, coord3, trange3, river3, town3)

    stations = [s,k,j]
    inconsistent_stations = [k,j]
    assert inconsistent_typical_range_stations(stations) == inconsistent_stations
    
    
