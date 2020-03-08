#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Created on 2020-03-01 by Asmita Gautam
Assignment 06: Graphing-data-with-python
Using Numpy and Matplotlib to plot graphs

Modified for comments on 2020-03-08
"""

"""
Importing the required module :
    numpy:
    matplotlib:
"""
import matplotlib.pyplot as plt
import numpy as np

# Computing to input the name of the data file to be plotted and it's output
print('Input the file name  plot:')
file_name = str(input())
print('Determining the output filename:')
file_out = str(input())

# Reading the given datafile
obs=np.genfromtxt(file_name+'.txt', skip_header=1,                               # Skip the 1st line since it is header
                  dtype=["int","float","float","float","float","float","float"],
                  delimiter="\t",                                                # Since the input file is txt
                  names=['Year','Mean','Max','Min','StdDev','Tqmean','RBindex'], # Naming each column 
                  )

year = obs['Year']
mean = obs['Mean']
max_streamflow = obs['Max']
min_streamflow = obs['Min']

# Generate three plots
# 1st plot for Streamflow

plt.figure(figsize=(7,7))
plt.subplot(311)
l1=plt.plot(year,mean,label='Mean',color='black')
l2=plt.plot(year,max_streamflow,label='Max',color='red')
l3=plt.plot(year,min_streamflow,label='Min',color='blue')
plt.legend(loc='upper left')                                   #To show the legend box at the upper left position  
plt.ylabel('Streamflow (cfs)')

# 2nd plot for Tqmean
plt.subplot(312)
t1=plt.plot(year,obs['Tqmean']*100, 'g^')
plt.ylabel('Tqmean (%)')

# 3rd for R-B index
plt.subplot(313)
r1=plt.bar(year,obs['RBindex'])
plt.ylabel('R-B Index (ratio)')

# Output as pdf
plt.savefig(file_out+'.pdf')