import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Load in visibility file
filename = 'lab3_visibilities.txt'
baseline, vis, baserr, viserr = np.loadtxt(filename, unpack=True)

# Define sinc function
def vis_sinc(b):
    a = 0.009
    return (1/a)*abs(np.sin(np.pi*b*a)/(np.pi*b))

extra_baseline = []
vis_expected = []

n = 0

while n <= 300:
    extra_baseline.append(n)
    vis_expected.append(vis_sinc(n))
    n = n+1
    
#for i in range(0, len(baseline)):
#    print(baseline[i], vis[i])
#    print('alpha = ', alpha(baseline[i],vis[i]))

plt.errorbar(baseline, vis, xerr=baserr, yerr=viserr, linestyle='none',marker='o', label="Measured Values")
plt.ylim(0.0,0.4)
plt.xlim(50.0,270.0)
plt.xlabel('Baseline (cm)')
plt.ylabel('Visibility Amplitude')
plt.plot(extra_baseline, vis_expected, linestyle="-", label="Expected sinc function")
plt.legend()
plt.show()
plt.savefig('Visibilities.png')
