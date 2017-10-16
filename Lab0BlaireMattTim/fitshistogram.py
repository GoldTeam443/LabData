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
import scipy
from scipy import stats
from scipy.stats import norm


# Open .fits file to inspect
filename=(raw_input('Enter .fits file to inspect: '))
fits_file = fits.open(filename)

# Convert image into numpy array
imagedata = fits_file[0].data

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
def sigmaclipping():
    clipmax = median + 5*std_dev

    print('Cutoff = ', clipmax)

    nrejected = clipmax
    nwarm = median + 3*std_dev
    fracrejected = nrejected/len(countvalues)
    fracwarm = nwarm/len(countvalues)
    print('Fraction of hot pixels = ', fracrejected)
    print('Fraction of warm pixels = ', fracwarm)

    return clipmax

clippingchosen=0

while clippingchosen==0:
    clipping=raw_input("Do sigma clipping? (y/n) ")
    if clipping == 'y':
        clippingchosen=1
    if clipping == 'n':
        clippingchosen=2
    else:
        print("Please type either y or n.")
        continue

#Plot histogram overplotted with normal distribution

mean = np.mean(countvalues)
median = np.median(countvalues)
print(mean)
print(median)

cmin=np.min(countvalues)
cmax=np.max(countvalues)
nbins=100
normalization=(cmax-cmin)/nbins*len(countvalues[(countvalues>=cmin) & (countvalues<=cmax)])

if clippingchosen==1:
    clipmax=sigmaclipping()
    clipmin = cmin
    clippedvalues = countvalues[(countvalues>=clipmin) & (countvalues<=clipmax)]
    cmax=clipmax

    mu=np.mean(clippedvalues)
    sig_clipped=np.std(clippedvalues)

    xarray=np.linspace(clipmin,clipmax,nbins*10)
    yarray=normalization*norm.pdf(xarray,loc=mu, scale=sig_clipped)

else:
    cmax=np.max(countvalues)
    mu=np.mean(countvalues)
    sig=np.std(countvalues)
    
    xarray=np.linspace(cmin,cmax,nbins*10)
    yarray=normalization*norm.pdf(xarray,loc=mu, scale=sig)

mean = np.mean(countvalues)
print(mean)

#Construct the plot
plt.hist(countvalues,range=[cmin,cmax], bins=nbins);
#plt.yscale('log')
plt.ylim([0.1,1e6])
plt.xlabel("Number of counts")
plt.ylabel("Number of instances")
plt.title("Distribution of counts, %s"%filename)
plt.text(14000,11000,"Mean = %s \nMedian = %s \nMode = %s \nStandard Deviation = %s"%(mean,median,mode,std_dev))
if clippingchosen==1:
    plt.plot(xarray,yarray,color="red",linewidth=3.0)
    plt.axvline(x=mode,linewidth=3.0,color="yellow")
plt.show()

fits.close(filename)
