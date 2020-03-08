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
    sys:
"""
import matplotlib.pyplot as plt
import numpy as np


# Read data
print('Input the file name being used to plot:')
file_name = str(input())
print('Determining the output filename:')
file_out = str(input())
obs=np.genfromtxt(file_name+'.txt', skip_header=1,
                  dtype=["int","float","float","float","float","float","float"],
                  delimiter="\t",
                  names=['Year','Mean','Max','Min','StdDev','Tqmean','RBindex'],
                  )

year = obs['Year']
mean = obs['Mean']
max_col = obs['Max']
min_col = obs['Min']
# Generate three plots
# 1st for Streamflow
plt.figure(figsize=(7,7))
plt.subplot(311)
l1=plt.plot(year,mean,label='Mean',color='black')
l2=plt.plot(year,max_col,label='Max',color='red')
l3=plt.plot(year,min_col,label='Min',color='blue')
plt.legend(loc='best')
plt.ylabel('Streamflow (cfs)')

# 2nd for Tqmean
plt.subplot(312)
t1=plt.plot(year,obs['Tqmean']*100, 'g^')
plt.ylabel('Tqmean (%)')

# 3rd for R-B index
plt.subplot(313)
r1=plt.bar(year,obs['RBindex'])
plt.ylabel('R-B Index (ratio)')

# Output as pdf
plt.savefig(file_out+'.pdf')
ax3.set_xlabel('Year')
ax3.set_ylabel('R-B Index (ratio)')
ax3.set_xticks(data['Year'][np.linspace(0, len(data['Year']) - 1, 15, dtype='int')])	# xticks for year

# saving figure and pdf
plt.savefig(outFilename)

