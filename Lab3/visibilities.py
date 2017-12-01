import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Load in visibility file
filename = 'lab3_visibilities.txt'
baseline, vis, baserr, viserr = np.loadtxt(filename, unpack=True)

# Define sinc function
def vis_sinc(b,a):
    return abs(np.sin(np.pi*b*a)/(np.pi*b))

popt, pcov = curve_fit(vis_sinc,baseline,vis)
print(popt)
print(pcov)

fitted_data = vis_sinc(baseline,*popt)

plt.plot(baseline, vis, linestyle='none',marker='o')
plt.xlabel('Baseline (cm)')
plt.ylabel('Visibility Amplitude')
plt.plot(baseline,fitted_data, linestyle="--")
plt.show()
