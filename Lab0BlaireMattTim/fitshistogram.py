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
bias_frame = fits.open(raw_input('Enter .fits file to inspect: '))

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

#Compute mean, median, mode, and standard deviation:
mean = np.mean(countvalues)
median = np.median(countvalues)
mode = stats.mode(countvalues)[0][0]
std_dev = np.std(countvalues)

print('Mean = ', mean)
print('Median = ', median)
print('Mode = ', mode)
print('Standard Deviation', std_dev)

#Sigma clipping: Remove all points smaller or larger than median +/- 5(sigma)
clipmax = median + 5*std_dev

print('Cutoff = ', clipmax)

#Plot histogram overplotted with normal distribution

cmin=900
cmax=1200
nbins=100
normalization=(cmax-cmin)/nbins*len(countvalues[(countvalues>=cmin) & (countvalues<=cmax)])

clipmin = cmin
clippedvalues = countvalues[(countvalues>=clipmin) & (countvalues<=clipmax)]

mu=np.mean(clippedvalues)
sig_clipped=np.std(clippedvalues)
mode_clipped=stats.mode(clippedvalues)[0][0]

xarray=np.linspace(cmin,cmax,nbins*10)
yarray=normalization*norm.pdf(xarray,loc=mu, scale=sig_clipped)

plt.hist(countvalues,range=[cmin,cmax], bins=nbins);
plt.yscale('log')
plt.ylim([0.1,1e6])
plt.plot(xarray,yarray,color="red",linewidth=3.0)
plt.axvline(x=mode,linewidth=3.0,color="yellow")
plt.show()
