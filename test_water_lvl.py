from turtle import st
from floodsystem.analysis import polyfit
from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_highest_rel_level
import datetime
import numpy as np
from floodsystem.flood import stations_level_over_threshold
from Task2G import generate_towns_list
from Task2G import stations_in_town


def test_relative_water_lvl(): 
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    s.latest_level = 5

    s_id2 = "test-s-id"
    m_id2 = "test-m-id"
    label2 = "some station"
    coord2 = (-2.0, 4.0)
    trange2 = (1.3, 45)
    river2 = "River X2"
    town2 = "My Town2"
    k = MonitoringStation(s_id2, m_id2, label2, coord2, trange2, river2, town2)
    k.latest_level = 10

    s_id3 = "test-s-id"
    m_id3 = "test-m-id"
    label3 = "some station"
    coord3 = (-2.0, 4.0)
    trange3 = (0,0)
    river3 = "River Y"
    town3 = "My Town"
    j = MonitoringStation(s_id3, m_id3, label3, coord3, trange3, river3, town3)
    j.latest_level = 3

    s_id4 = "test-s-id"
    m_id4 = "test-m-id"
    label4 = "some station"
    coord4 = (-2.0, 4.0)
    trange4 = (1,2)
    river4 = "River Y"
    town4 = "My Town"
    z = MonitoringStation(s_id4, m_id4, label4, coord4, trange4, river4, town4)
    z.latest_level = 2

    stations = [s,k,j,z]
    tol = 7 
    lst = stations_level_over_threshold(stations, tol)
    lst2 = stations_highest_rel_level(stations, 2)

    assert lst[0][1] == 10
    assert lst2[1].latest_level == 10

def town_test(): 
    
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    s.latest_level = 5

    s_id2 = "test-s-id"
    m_id2 = "test-m-id"
    label2 = "some station"
    coord2 = (-2.0, 4.0)
    trange2 = (1.3, 45)
    river2 = "River X2"
    town2 = "My Town2"
    k = MonitoringStation(s_id2, m_id2, label2, coord2, trange2, river2, town2)
    k.latest_level = 10

    s_id3 = "test-s-id"
    m_id3 = "test-m-id"
    label3 = "some station"
    coord3 = (-2.0, 4.0)
    trange3 = (0,0)
    river3 = "River Y"
    town3 = "My Town"
    j = MonitoringStation(s_id3, m_id3, label3, coord3, trange3, river3, town3)
    j.latest_level = 3

    s_id4 = "test-s-id"
    m_id4 = "test-m-id"
    label4 = "some station"
    coord4 = (-2.0, 4.0)
    trange4 = (1,2)
    river4 = "River Y"
    town4 = "My Town"
    z = MonitoringStation(s_id4, m_id4, label4, coord4, trange4, river4, town4)
    z.latest_level = 2
    
    stations = [s,k,j,z]
    town_list = generate_towns_list(stations)

    assert len(town_list) == 2

def test_stations_in_town(): 
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    s.latest_level = 5

    s_id2 = "test-s-id"
    m_id2 = "test-m-id"
    label2 = "some station"
    coord2 = (-2.0, 4.0)
    trange2 = (1.3, 45)
    river2 = "River X2"
    town2 = "My Town2"
    k = MonitoringStation(s_id2, m_id2, label2, coord2, trange2, river2, town2)
    k.latest_level = 10

    s_id3 = "test-s-id"
    m_id3 = "test-m-id"
    label3 = "some station"
    coord3 = (-2.0, 4.0)
    trange3 = (0,0)
    river3 = "River Y"
    town3 = "My Town"
    j = MonitoringStation(s_id3, m_id3, label3, coord3, trange3, river3, town3)
    j.latest_level = 3

    s_id4 = "test-s-id"
    m_id4 = "test-m-id"
    label4 = "some station"
    coord4 = (-2.0, 4.0)
    trange4 = (1,2)
    river4 = "River Y"
    town4 = "My Town"
    z = MonitoringStation(s_id4, m_id4, label4, coord4, trange4, river4, town4)
    z.latest_level = 2
    
    stations = [s,k,j,z]
    stat_list = stations_in_town(stations,"My Town2")
    
    assert stat_list[0].latest_level == 10
    assert len(stat_list) == 1

def test_derivative_severity(): 
    now = datetime.datetime.utcnow()
    dates = np.linspace(0, 2, 10)
    levels = [10]*len(dates)
    
    poly = polyfit(dates, levels, 3)
    d_poly = np.polyder(poly)
    some_val = d_poly(2)
    assert some_val <= 0.1




