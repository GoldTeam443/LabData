#imports various libraries
from matplotlib import pyplot as plt
import numpy as np
import math
import csv
from csv import reader

#Opens the csv file associated with the main star and reads the time, flux, and error
filename = 'Flux_Values_Main.txt'
f =  open(filename)
file = csv.reader(f)

time = []
flux = []
err = []

for row in file:
    time.append(row[0])
    flux.append(row[1])
    err.append(row[2])

time_main = time[1:-1]
flux_main = flux[1:-1]
err_main = err[1:-1]

#Does the same for other relevant stars
filename = 'Flux_Values_1.txt'
f =  open(filename)
file = csv.reader(f)

time = []
flux = []
err = []

for row in file:
    time.append(row[0])
    flux.append(row[1])
    err.append(row[2])

time_1 = time[1:-1]
flux_1 = flux[1:-1]
err_1 = err[1:-1]

filename = 'Flux_Values_4.txt'
f =  open(filename)
file = csv.reader(f)

time = []
flux = []
err = []

for row in file:
    time.append(row[0])
    flux.append(row[1])
    err.append(row[2])

time_2 = time[1:-1]
flux_2 = flux[1:-1]
err_2 = err[1:-1]

filename = 'Flux_Values_3.txt'
f =  open(filename)
file = csv.reader(f)

time = []
flux = []
err = []

for row in file:
    time.append(row[0])
    flux.append(row[1])
    err.append(row[2])

time_3 = time[1:-1]
flux_3 = flux[1:-1]
err_3 = err[1:-1]

#Plots the 4 stars on the same plot
plt.figure(1)
plt.plot(time_main,flux_main, label = 'Main')
plt.xlabel('Time [min]')
plt.ylabel('Flux [counts]')

plt.plot(time_1,flux_1)

plt.plot(time_2,flux_2)

plt.plot(time_3,flux_3)

plt.show()
