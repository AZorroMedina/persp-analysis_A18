# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 00:46:22 2018

@author: Angela
"""

def smallest_factor(n):
    """Return the smallest prime factor of the positive integer n."""
    if n==1: return 1
    for i in range(2, int(n**.5)):
        if n % i == 0: return i
        return n
    
#Test for zero and negative values
def test_smallest_factor():
    assert smallest_factor(0)==None, "error"
    assert smallest_factor(-1)==None, "error"