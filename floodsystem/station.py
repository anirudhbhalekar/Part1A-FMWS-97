# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d
    
    def typical_range_consistent(self):
        
        flag  = True
        t1 = self.typical_range
        if t1 == None: flag = False
        elif (t1[1] - t1[0]) < 0: flag = False
        else: pass
        return flag 

    def relative_water_level(self): 
        if self.typical_range_consistent():
            typical_low = self.typical_range[0]
            typical_high = self.typical_range[1]
            water_level = self.latest_level
            if water_level != None: 
                frac = (water_level - typical_low)/(typical_high - typical_low)
                return frac
            else: return None

        else: return None 


def inconsistent_typical_range_stations(stations): 
    
    inconsistent_list = []
    for station in stations: 
        if (MonitoringStation.typical_range_consistent(station)) == False: 
            inconsistent_list.append(station)

    return inconsistent_list



