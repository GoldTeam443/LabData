import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Load in visibility file
filename = 'lab3_visibilities.txt'
baseline, vis, baserr, viserr = np.loadtxt(filename, unpack=True)

# Define sinc function
def vis_sinc(b,a):
    #a = 0.009 (expected value)
    return abs(np.sin(np.pi*b*a)/(np.pi*b*a))

extra_baseline = []
vis_fit = []

n = 0

popt, pcov = curve_fit(vis_sinc, baseline, vis, sigma=viserr, p0=0.009)
perr = np.sqrt(np.diag(pcov))
print("alpha=",popt, "alpha_error=",perr)

# Calculate expected values
while n <= 300:
    extra_baseline.append(n)
    vis_fit.append(vis_sinc(n,*popt))
    n = n+1

# Plot values
plt.errorbar(baseline, vis, xerr=baserr, yerr=viserr, linestyle='none',marker='o', label="Measured Values")
plt.ylim(0.0,0.4)
plt.xlim(20.0,120.0)
plt.xlabel('B_lambda') #Unitless, is the baseline(cm)/lambda(cm)
plt.ylabel('Visibility Amplitude')
plt.plot(extra_baseline, vis_fit, linestyle="-", label="Fit visibility function")
plt.legend()
#plt.show()
plt.savefig('vis_fit.png')
print("Saved to vis_fit.png")
