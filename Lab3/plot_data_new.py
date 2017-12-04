# Script for overplotting single dish data for the sun and a satellite
# Written by Tim Sarro, Blaire Ness, and Matt Lee

import numpy as np
import math
from numpy import genfromtxt
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit


# Need to mask out noise in sun and satellite data
# Flip data upside down
# Normalize sun and satellite data to respective peak values
# Scale widths bt ratio of cosines of the elevations


#sunx = sun_data[:,0]
#suny = sun_data[:,1]

# Read in satellite and sun single dish data
sat_data = genfromtxt("single_dish_sat2.csv", delimiter=",")
sun_data = genfromtxt("sun_single_1.csv", delimiter=",")

#sat_data_alt = 45 deg
#sun_data_alt = 32.76 deg

#print 'sun_data max value is ', np.amax(sun_data[:,1])
#print 'sat_data max value is ', np.amax(sat_data[:,1])
#print 'sun_data min value is ', np.amin(sun_data[:,1])
#print 'sat_data min value is ', np.amin(sat_data[:,1])


#cut x values of data to the desired size
sun_data = sun_data[100:200,]
sat_data = sat_data[113:,]

#flip data functions
sun_place = 1 - sun_data[:,1]
sat_place = 1 - sat_data[:,1]

sun_flip = np.column_stack((sun_data[:,0],sun_place))
sat_flip = np.column_stack((sat_data[:,0],sat_place))


#print 'sun_flip max value is ', np.amax(sun_flip[:,1])
#print 'sat_flip max value is ', np.amax(sat_flip[:,1])
#print 'sun_flip min value is ', np.amin(sun_flip[:,1])
#print 'sat_flip min value is ', np.amin(sat_flip[:,1])


#normalize x axis of data to same length
u = sun_flip[:,0]
v = sat_flip[:,0]

E = np.amin(u)
F = np.amax(u)
G = np.amin(v)
H = np.amax(v)
c = float(0)
d = F

sunx = c + (u - E)*(d - c)/(F - E)
satx = c + (v - G)*(d - c)/(H - G)

#print 'sumx max value is ', np.amax(sunx)
#print 'satx max value is ', np.amax(satx)
#print 'sunx min value is ', np.amin(sunx)
#print 'satx min value is ', np.amin(satx)

# normalize data to peak of sun data
x = sun_flip[:,1]
y = sat_flip[:,1]

A = np.amin(x)
B = np.amax(x)
C = np.amin(y)
D = np.amax(y)
a = float(0)
b = B

suny = a + (x - A)*(b - a)/(B - A)
saty = a + (y - C)*(b - a)/(D - C)


#print 'sumy max value is ', np.amax(suny)
#print 'saty max value is ', np.amax(saty)
#print 'suny min value is ', np.amin(suny)
#print 'saty min value is ', np.amin(saty)

#normalized values of data
sun_norm = np.column_stack((sun_flip[:,0], suny))
sat_norm = np.column_stack((sat_flip[:,0], saty))


#plotting data
sat_plot= plt.plot(sat_norm, label = 'Satellite Data')
sun_plot= plt.plot(sun_norm, label = 'Sun Data')
plt.legend([sun_plot, sat_plot],['Sun Data', 'Satellite Data'])
plt.xlabel('Time')
plt.ylabel('Voltage')
plt.ylim(0,3)
plt.show()

