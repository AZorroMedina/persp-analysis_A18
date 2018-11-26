# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 18:18:41 2018

@author: Angela
"""

#Import packages
import numpy as np

def get_r(K, L, alpha, Z, delta):
    '''
    This function generates the interest rate or vector of interest rates
    '''
    K = np.array(K)
    L = np.array(L)
    r = alpha*Z*np.divide(L,K)**(1-alpha)-delta
    return r



