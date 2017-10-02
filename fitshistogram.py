# Code to plot a histogram of a .fits file

### for array operations
import numpy as np

### for plotting
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


### for operations on FITS images
from astropy.io import fits

### statistics functions
from scipy import stats
from scipy.stats import norm


# Open .fits file to inspect
bias_frame = fits.open(input('Enter .fits file to inspect: '))

# Convert image into numpy array
imagedata = bias_frame[0].data

# Check dimensions of 2d array:
print('Dimenstions of 2d numpy array: ', imagedata.shape)

# Convert 2d numpy array into 1d list for plotting the histogram
countvalues = imagedata.flatten()

#Check dimenstions of 1d list:
print('Dimensions of 1d list: ', countvalues.shape)

#Max and min counts:
print('Max counts: ', np.max(countvalues))
print('Min counts: ', np.min(countvalues))

#Plot histogram (Using Logarithmic y-axis)
plt.hist(countvalues,bins=100);
plt.yscale('log')
