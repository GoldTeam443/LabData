import numpy as np
from astropy.io import fits
from scipy import stats
from scipy.stats import norm

#  Open masterflat
masterflat = fits.open("Master_Flat.fits")
masterflat_data = masterflat[0].data

#  Open dark frame
darkframe = fits.open("Master_Dark.fits")
darkframe_data = darkframe[0].data

#  Flatten masterflat into 1d list:
counts_flat = masterflat_data
counts_flat.shape

#  Compute median and standard deviation for masterflat
flat_med = np.median(counts_flat)
flat_std = np.std(counts_flat)

#  Create array of zeroes as base for bad pixel map
bpmap = np.tile(0, (1024,1024))

#  Loop over x and y values in masterflat
for i in range(0, counts_flat.shape[0]):
    for j in range(0, counts_flat.shape[1]):
        if counts_flat[i][j] <= (flat_med - 5*flat_std):
            bpmap[i][j] = 0
        else:
            bpmap[i][j] = 1

#  Flatten dark frame into 1d list:
counts_dark = darkframe_data
counts_dark.shape

#  Compute median and standard deviation for dark frame
dark_med = np.median(counts_dark)
dark_std = np.std(counts_dark)

print(dark_med + 5*dark_std)

#  Loop over x and y values in dark frame
for i in range(0, counts_dark.shape[0]):
    for j in range(0, counts_dark.shape[1]):
        if counts_dark[i][j] >= (dark_med + 5*dark_std) or  bpmap[i][j] == 0:
            bpmap[i][j] = 0
        else:
            bpmap[i][j] = 1


#  Write bpmap to fits file to save it
bpmapfits = fits.PrimaryHDU(bpmap)
bpmapfits.writeto('bad_pixel_map.fits')


masterflat.close()
darkframe.close()
