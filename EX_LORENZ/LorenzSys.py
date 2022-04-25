# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 16:28:55 2022

@author: Jens
"""

def LorenzSys(SIGMA, RHO, BETA, t, x, u):
    xdot = [[SIGMA*(-x[0]+x[1])+u],
            [RHO*x[0]-x[1]-x[0]*x[2]],
            [-BETA*x[2]+x[0]*x[1]],
             ]
    return xdot