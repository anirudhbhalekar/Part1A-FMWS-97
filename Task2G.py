"""" 5 modes to classify risks
We extend the polyfit 5 hours and only consider the past 1 day (for better curve fit)
5 hours ought to be enough to evacuate citizens - with higher extensions the graphs seem to get more exaggerated
<<<<<<< HEAD

Unlikely - value is 0-50% below upper range and is sloping down
Low - value is 0-50% below upper range and has a positive slope of less than 1
Moderate - value is 50-75% below upper range and has a positive slope of less than 1
High - value is 50-75% below upper range and has a positive slope of greater than 1 OR 
        value is between 
        
Severe - value is between 75-100% of upper range and has a positive slop greater than 1 OR
         value is above typical range

note: it is entirely possible for the value to be small (compared to upper range) but
for the derivative to be very high (in the polyfit)

% limit:derivative	    <0	        <1	        <5	        <10         >10
40>	                    Unlikely 	low	        low	        Moderate    High
60>	                    low	        low	        Moderate	High        High
80>	                    low	        Moderate	High	    High        Severe
100>	                Moderate	High	    High  	    Severe      Severe
100<	                High	    High	    Severe	    Severe      Severe


"""

from operator import mod
import numpy as np 
=======
 
Unlikely - value is 0-50% below upper range and is sloping down
Low - value is 0-50% below upper range and has a positive slope of less than 1
Moderate - value is 50-75% below upper range and has a positive slope of less than 1
High - value is 50-75% below upper range and has a positive slope of greater than 1 OR
        value is between
       
Severe - value is between 75-100% of upper range and has a positive slop greater than 1 OR
         value is above typical range
 
note: it is entirely possible for the value to be small (compared to upper range) but
for the derivative to be very high (in the polyfit)
 
% limit:derivative      <0          <1          <5          <10         >10
40>                     Unlikely    low         low         Moderate    High
60>                     low         low         Moderate    High        High
80>                     low         Moderate    High        High        Severe
100>                    Moderate    High        High        Severe      Severe
100<                    High        High        Severe      Severe      Severe
 
"""
 
from operator import mod
import numpy as np
>>>>>>> 01ee757f07e59a73a6305868f8294094eb9efd70
import matplotlib
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.analysis import polyfit
import datetime
from Task2F import make_plots
from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels
<<<<<<< HEAD

ext = 0.2 # approximates to about 5 hours 

def der(poly):
    return np.polyder(poly)

def average(lst):
    return sum(lst)/len(lst)

=======
 
ext = 0.2 # approximates to about 5 hours
 
def der(poly):
    return np.polyder(poly)
 
def average(lst):
    return sum(lst)/len(lst)
 
>>>>>>> 01ee757f07e59a73a6305868f8294094eb9efd70
def polyvalues(station, dt, p, extension):
    flag = True
    dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
    time = matplotlib.dates.date2num(dates)
    poly, d0 = polyfit(dates, levels, p)
<<<<<<< HEAD

=======
 
>>>>>>> 01ee757f07e59a73a6305868f8294094eb9efd70
    if poly != 0:
       
        d_poly = der(poly)
        poly_list = [] # stores average value of polynomial
<<<<<<< HEAD
        d_poly_list = [] # stores average value of derivative 
        
        # now to calculate average value for time = now to time = 5 hours later
        
=======
        d_poly_list = [] # stores average value of derivative
       
        # now to calculate average value for time = now to time = 5 hours later
       
>>>>>>> 01ee757f07e59a73a6305868f8294094eb9efd70
        for i in range(11):
            delta = extension/10 * i
            poly_list.append(poly(delta))
            d_poly_list.append(d_poly(delta))
<<<<<<< HEAD

    

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
=======
 
   
 
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
    severity_matrix = [
>>>>>>> 01ee757f07e59a73a6305868f8294094eb9efd70
                        ["Unlikely", "Low", "Low", "Moderate", "High"],
                        ["Low", "Low", "Moderate", "High", "High"],
                        ["Low", "Moderate", "High", "High", "Severe"],
                        ["Moderate", "High", "High", "Severe", "Severe"],
                        ["High", "High", "Severe", "Severe", "Severe"],
    ]
<<<<<<< HEAD

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
=======
 
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
>>>>>>> 01ee757f07e59a73a6305868f8294094eb9efd70
    elif val_der <=1:
        col = 1
    elif val_der <=5:
        col = 2
    elif val_der <= 10:
        col = 3
<<<<<<< HEAD
    elif val_der >  10: 
        col = 4
    
    return row, col

def test_graph(station_name, dt, p):
    make_plots(station_name, dt, p)

def iterate_thru(stations, dt, p, ext, severity_index = "Severe"):
    list_stations = []
    
    """ IMPORTANT - limiting the number of data entries to test - otherwise it takes too much time"""
    stations = stations[:25] 
    """ IMPORTANT - limiting the number of data entries to test - otherwise it takes too much time"""

    for station in stations: 
=======
    elif val_der >  10:
        col = 4
   
    return row, col
 
def test_graph(station_name, dt, p):
    make_plots(station_name, dt, p)
 
def iterate_thru(stations, dt, p, ext, severity_index = "Severe"):
    list_stations = []
   
    """ IMPORTANT - limiting the number of data entries to test - otherwise it takes too much time"""
    stations = stations[:25]
    """ IMPORTANT - limiting the number of data entries to test - otherwise it takes too much time"""
 
    for station in stations:
>>>>>>> 01ee757f07e59a73a6305868f8294094eb9efd70
        if station.name == "Letcombe Bassett":
            pass
        elif classify_severity(station, dt, p, ext) == severity_index:
            list_stations.append((station.name, station.latest_level))
<<<<<<< HEAD
    
=======
   
>>>>>>> 01ee757f07e59a73a6305868f8294094eb9efd70
    return list_stations
if __name__ == "__main__":
   
    stations = build_station_list()
    station = stations[20]
<<<<<<< HEAD
    
=======
   
>>>>>>> 01ee757f07e59a73a6305868f8294094eb9efd70
    dt = 1
    p = 4
    ext = 0.2
    severity_index = "High"
    update_water_levels(stations)
<<<<<<< HEAD

    stat_risk_list = iterate_thru(stations, dt, p, ext, severity_index = severity_index)

=======
 
    stat_risk_list = iterate_thru(stations, dt, p, ext, severity_index = severity_index)
 
>>>>>>> 01ee757f07e59a73a6305868f8294094eb9efd70
    print("\n")
    print("STATIONS AT {} RISK LISTED BELOW (WITH LATEST WATER LEVEL DATA)".format(severity_index.upper()))
    print("\n")
    print(stat_risk_list)
<<<<<<< HEAD
    
    
=======
   
   
>>>>>>> 01ee757f07e59a73a6305868f8294094eb9efd70
    """
    print(station.name)
    print(polyvalues(station, dt, p, ext))
    print(classify_severity(station, dt, p, ext))
<<<<<<< HEAD

    #test_graph(station.name, dt, p)

    """
    

       


=======
 
    #test_graph(station.name, dt, p)
 
    """
>>>>>>> 01ee757f07e59a73a6305868f8294094eb9efd70
