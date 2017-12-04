import csv
import numpy as np
import math
from numpy import genfromtxt
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit


# Read in satellite and sun single dish data
sat_data = genfromtxt("single_dish_sat2.csv", delimiter=",")
satmax = np.amax(sat_data, axis=0)

# Need to mask out noise in sun and satellite data
# Flip data upside down
# Normalize sun and satellite data to respective peak values
# Scale widths bt ratio of cosines of the elevations



sun_data = genfromtxt("sun_single_1.csv", delimiter=",")
#sunx = sun_data[:,0]
#suny = sun_data[:,1]



plt.plot(sat_data)
plt.plot(sun_data)
plt.xlabel('Time')
plt.ylabel('Voltage')
plt.ylim(-2.0,7.0)
plt.show()
