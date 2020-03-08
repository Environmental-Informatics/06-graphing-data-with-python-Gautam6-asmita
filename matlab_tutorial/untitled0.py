#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 17:53:03 2020

@author: gautam6
"""
import numpy as np
import matplotlib.pyplot as plt
obs  = np.genfromtxt('Tippecanoe_River_at_Ora.Annual_Metrics.txt', skip_header=1,
                     dtype=["float","float","float","float","float","float"],
                     delimiter=[4,8,9,8,8,9],
                     names = ['Year', 'Mean', 'Max', 'Min', 'StdDev', 'Tqmean', 'RBindex'],
                     usecols = (0,1,2,3,5)
                     )
names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]

plt.figure(figsize=(9, 3))

plt.subplot(131)
plt.bar(names, values)
plt.subplot(132)
plt.scatter(names, values)
plt.subplot(133)
plt.plot(names, values)
plt.suptitle('Categorical Plotting')
plt.show()