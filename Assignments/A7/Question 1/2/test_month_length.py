# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 23:43:00 2018

@author: Angela
"""
def leap_year (year):
    return (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)

def month_length(month, year):
    """Return the number of days in the given month."""
    if month in {"September", "April", "June", "November"}:
        return 30
    elif month in {"January", "March", "May", "July",
                   "August", "October", "December"}:
        return 31
    elif month=="February" and leap_year(year)==True:
        return 29
    elif month=="February" and leap_year(year)==False:
            return 28

def test_month_length():
 
    assert month_length("February", 2003)==28, "February problem"
    assert month_length("September", 2003)==30, "Regular month problem"
    assert month_length("January", 2004)==31, "Regular month problem"
    assert month_length("February", 2004)==29, "February problem"
    assert month_length("September", 2004)==30, "Regular month problem"
    
 
    