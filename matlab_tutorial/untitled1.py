#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 16:27:43 2020

@author: gautam6
"""
import matplotlib.pyplot as plt
import numpy as np

data_file=np.genfromtxt("Wildcat_Creek_at_Lafayette.Annual_Metrics.txt", 
                        skip_header=1) # Skip the line 1 so the header will be remomved
                    
Year=data_file[:,0]
mean_temp=data_file[:,1]
min_temp=data_file[:,2]
max_temp=data_file[:,3]

data_file1=np.genfromtxt("Wildcat_Creek_at_Lafayette.Annual_Metrics.txt", 
                         skip_header=1,
                        names=['year','mean','max','min','stdec,tqmean','rbindex'])

plt.figure(figsize=(9, 3))
plt.subplot(131)
plt.plot(Year, mean_temp,'r', Year, min_temp, 'b',Year, max_temp, 'y')
plt.subplot(231)
plt.plot(Year, min_temp)
plt.subplot(331)
plt.plot(Year, max_temp)
plt.suptitle('Categorical Plotting')
plt.show()
