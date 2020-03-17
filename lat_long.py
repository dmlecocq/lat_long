# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 09:28:52 2020

@author: dlecocq
"""
from math import sin, cos, sqrt, atan2, radians
def latlong_diff(lat1, long1, lat2, long2, unit='miles'):
    lat1 = radians(lat1)
    lon1 = radians(long1)
    lat2 = radians(lat2)
    lon2 = radians(long2)  
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    dist=c*6373.0 
    
    if unit=='miles':
        dist=dist* 0.621371
    return dist