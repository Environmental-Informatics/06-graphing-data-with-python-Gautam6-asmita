"""Created on 2020-03-01 by Asmita Gautam
Assignment 06: Graphing-data-with-python
Using Numpy and Matplotlib to plot graphs

Modified for comments on 2020-03-08
"""

"""
Importing the required module :
    numpy:a multidimensional array object, various derived objects ,
    and an assortment of routines for fast operations on arrays,
    including mathematical, logical, shape manipulation, sorting, selecting, I/O, discrete Fourier transforms, basic linear algebra, basic statistical operations, 
    which allows for doing mathematical operations
    matplotlib
"""
#example
import matplotlib.pyplot as plt
import numpy as np

#Importing the txt file using genfromtxt function from numpy module

data_file=np.genfromtxt("Wildcat_Creek_at_Lafayette.Annual_Metrics.txt", 
                        skip_header=1)       # Skip the line 1 so the header will be remomved
                    
Year=data_file[:,0]               
mean_temp=data_file[:,1]
min_temp=data_file[:,2]
max_temp=data_file[:,3]
tq=data_file[:,5]
rb=data_file[:,6]
tq_100=np.array(data_file[:,5]*100)

plt.figure(figsize=(9, 3))

plt.subplot(131)
plt.xlabel("Years")
plt.ylabel("Temp")
plt.plot(Year, mean_temp,label="Mean Temperature")
plt.plot(Year, min_temp,label="Min temp")
plt.plot(Year, max_temp,label="Max temp")
plt.legend()

plt.subplot(132)
plt.plot(Year, tq_100, label="tq")
plt.xlabel("Years")

plt.subplot(133)
plt.plot(Year, rb, label='max')
plt.show()
#obs  = np.genfromtxt('observations.dat', skip_header=1,
                    # dtype=["a11","float","float","float","a2","a2"],
                     #delimiter=[11,8,9,8,2,2],
                     #names = ['label', 'i_obs', 'lambda', 'e_obs', 'na', 'observer'],
                    # usecols = (0,1,2,3,5)
                     #)
