# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 16:58:25 2022

@author: Jens
"""

import numpy as np

def mynoise(t, tspan):
    np.random.seed(0)
    Nt = len(tspan)
    uall = np.random.rand(Nt)
    u = uall()