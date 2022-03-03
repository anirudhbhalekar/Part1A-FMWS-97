"""" 5 modes to classify risks
We extend the polyfit 5 hours and only consider the past 1 day (for better curve fit)
5 hours ought to be enough to evacuate citizens - with higher extensions the graphs seem to get more exaggerated

Each station will have a severity score - for each town the severity will be computed by taking the average of 

Unlikely - Average severity score   < 2
Low - Average severity score        < 4
Moderate - Average severity score   < 6
High - Average severity score       < 8
Severe - Aeverage severity score    > 8


This is for the towns, the way to classify them is to average the severity scores across 
each of its stations

For each station the severity score is calculated as follows: 

1 - value is 0-50% below upper range and is sloping down
2 - value is 0-50% below upper range and has a positive slope of less than 1
3 - value is 50-75% below upper range and has a positive slope of less than 1
4 - value is 50-75% below upper range and has a positive slope of greater than 1 OR 
        value is between        
5 - value is between 75-100% of upper range and has a positive slop greater than 1 OR
         value is above typical range

note: it is entirely possible for the value to be small (compared to upper range) but
for the derivative to be very high (in the polyfit)

% limit:derivative	    <0	        <1	        <5	        <10         >10
40>	                    1	        2	        3	        4	        5
60>                     2	        3	        4	        5	        6
80>                     3	        4	        5	        6	        7
100>                    4	        5	        6	        7	        8
100<                    5	        6	        7	        8	        9


"""

from operator import mod
import numpy as np 
import matplotlib
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.analysis import polyfit
import datetime
from Task2F import make_plots
from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels

ext = 0.2 # approximates to about 5 hours 

def der(poly):
    return np.polyder(poly)

def average(lst):
    return sum(lst)/len(lst)

def polyvalues(station, dt, p, extension):
    flag = True
    dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
    time = matplotlib.dates.date2num(dates)
    poly, d0 = polyfit(dates, levels, p)
    if poly != 0:
       
        d_poly = der(poly)
        poly_list = [] # stores average value of polynomial
        d_poly_list = [] # stores average value of derivative 
        
        # now to calculate average value for time = now to time = 5 hours later
        
        for i in range(11):
            delta = extension/10 * i
            poly_list.append(poly(delta))
            d_poly_list.append(d_poly(delta))

    

        return poly_list, d_poly_list
    else: 
        return [0],[0]

def classify_severity(station, dt, p, extension):
    poly_list, d_poly_list = polyvalues(station, dt, p, extension)
    
    max_poly = max(poly_list)

    # justification here - if the value anywhere between 0 and 5 hours from now is above typical range -
    # (or too close to it, a warning will go off)

    if station.typical_range == None: 
        upper_range = -100 # random negative value i 
    else: 
        upper_range = station.typical_range[1]
    
    val_percent = max_poly/upper_range # returns a percent value (well in ratio form)
    val_der = d_poly_list[-1] # returns the derivative at the end of the list

    # we can now construct a 2D matrix of values as seen in  the comment above
    # possible extension - make it so it can read csv files, that way you can make the matrix on excel
    
    severity_matrix = [ 
                        [1,2,3,4,5],
                        [2,3,4,5,6],
                        [3,4,5,6,7],
                        [4,5,6,7,8],
                        [5,6,7,8,9],
    ]

    row, col = return_row_col(val_percent, val_der)
    severity = severity_matrix[row][col]
    return severity

def return_row_col(val_percent, val_der):
    row = 0
    col = 0
    if val_percent <= 0.4: 
        row = 0
    elif val_percent <= 0.6: 
        row = 1
    elif val_percent <= 0.8: 
        row = 2
    elif val_percent <= 1: 
        row = 3
    elif val_percent > 1: 
        row = 4 

    if val_der <= 0: 
        col = 0   
    elif val_der <=1:
        col = 1
    elif val_der <=5:
        col = 2
    elif val_der <= 10:
        col = 3
    elif val_der >  10: 
        col = 4
    
    return row, col

def generate_towns_list(stations):
    towns_list = []
    for station in stations:
        if station.town in towns_list: 
            pass
        else: 
            towns_list.append(station.town)
    return towns_list

def test_graph(station_name, dt, p):
    make_plots(station_name, dt, p)

def stations_in_town(stations, town): 
    stat_list = []
    for station in stations: 
        if station.town == town: 
            stat_list.append(station)
    return stat_list

def classify_town(stations, town, dt, p, extension):
    severity = "Unlikely" # By default
    stat_list = stations_in_town(stations, town)
    score_list = []
    for station in stat_list: 
        score_list.append(classify_severity(station, dt, p, extension))
    avg_score = average(score_list)
    
    if avg_score   <  2: severity = "Unlikely".upper()
    elif avg_score <  4: severity = "Low".upper() 
    elif avg_score <  6: severity = "Moderate".upper() 
    elif avg_score <  8: severity = "High".upper() 
    elif avg_score >= 8: severity = "Severe".upper() 

    return severity

def iter_through_towns(stations, dt, p, extension, threshold = "Severe"):

    """IMPORTANT: REMOVE BELOW LINE WHEN IMPLEMENTING PROGRAM"""
    stations = stations[:100] # this is just to reduce computing time for the tests
    """IMPORTANT: REMOVE ABOVE LINE WHEN IMPLEMENTING PROGRAM"""
    
    towns_list = generate_towns_list(stations)
    town_severity_list = []

    for town in towns_list: 
        severity = classify_town(stations, town, dt, p, extension)
        if severity == threshold:
            town_severity_list.append((town, severity))
    return town_severity_list

if __name__ == "__main__":
   
    stations = build_station_list()
    
    """"CONTROL VARIABLES"""

    dt = 1
    p = 4
    ext = 0.2
    severity_index = "Severe"

    """END OF CONTROL VARIABLES"""
    
    severity_index = severity_index.upper()
    update_water_levels(stations)

    tup = iter_through_towns(stations, dt, p, ext, severity_index)
    print("TOWNS AT {} RISK".format(severity_index))
    for i in tup: 
        print('{:50}{:<5}'.format(i[0], i[1]))
    
       


