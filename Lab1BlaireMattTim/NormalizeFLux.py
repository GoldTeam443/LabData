#imports various libraries
from matplotlib import pyplot as plt
import numpy as np
import math
import csv
from csv import reader

def Extract_Data(filename):

    #Opens the csv file associated with the main star and reads the time, flux, and error
    f =  open(filename)
    file = csv.reader(f)

    #extracts data from file
    time = []
    flux = []
    err = []

    for row in file:
        time.append(row[0])
        flux.append(row[1])
        err.append(row[2])

    time_new = time[1:-1]
    flux_new = flux[1:-1]
    err_new = err[1:-1]

    #turns values into lists
    time_list = list(map(float, time_new))
    flux_list = list(map(float, flux_new))
    err_list = list(map(float, err_new))

    #finds the average
    u_flux = np.mean(flux_list)

    #Normalizes date
    norm_flux = [x / u_flux for x in flux_list]
    norm_err = [x / u_flux for x in err_list]

    return time_list, flux_list, err_list, norm_flux, norm_err


#calls the extraction sub_function to return all needed values
time_main, flux_main, err_main, norm_flux_main, norm_err_main = Extract_Data('Flux_Values_Main.txt')
time_1, flux_1, err_1, norm_flux_1, norm_err_1 = Extract_Data('Flux_Values_1.txt')
time_2, flux_2, err_2, norm_flux_2, norm_err_2 = Extract_Data('Flux_Values_2.txt')
time_3, flux_3, err_3, norm_flux_3, norm_err_3 = Extract_Data('Flux_Values_3.txt')
time_4, flux_4, err_4, norm_flux_4, norm_err_4 = Extract_Data('Flux_Values_4.txt')
time_5, flux_5, err_5, norm_flux_5, norm_err_5 = Extract_Data('Flux_Values_5.txt')
time_6, flux_6, err_6, norm_flux_6, norm_err_6 = Extract_Data('Flux_Values_6.txt')
time_7, flux_7, err_7, norm_flux_7, norm_err_7 = Extract_Data('Flux_Values_7.txt')
time_8, flux_8, err_8, norm_flux_8, norm_err_8 = Extract_Data('Flux_Values_8.txt')
time_9, flux_9, err_9, norm_flux_9, norm_err_9 = Extract_Data('Flux_Values_9.txt')
time_10, flux_10, err_10, norm_flux_10, norm_err_10 = Extract_Data('Flux_Values_10.txt')

#Puts the normalized fluxes into a matrix for easy manipulation
norm_flux_m = [norm_flux_1, norm_flux_2, norm_flux_3, norm_flux_4, norm_flux_5, norm_flux_6, norm_flux_7, norm_flux_8, norm_flux_9, norm_flux_10]
norm_err_m = [norm_err_1, norm_err_2, norm_err_3, norm_err_4, norm_err_5, norm_err_6, norm_err_7, norm_err_8, norm_err_9, norm_err_10]

#Finds the weighted normalized fluxes, errors, and the ratio of the main flux and the normalized flux
norm_flux = []
norm_err = []
main_ratio = []
main_ratio_err = []
for i in range(0, len(norm_flux_1)):
    numerator = 0
    denominator = 0
    for j in range(0, 9):
        f = norm_flux_m[j][i]
        sig = norm_err_m[j][i]
        numerator = numerator + (f / (sig**2.0))
        denominator = denominator + (1.0/(sig**2.0))
    norm_flux.append(numerator/denominator)
    norm_err.append((1.0/denominator)**0.5)
    
    main_ratio.append(flux_main[i]/norm_flux[i])
    main_ratio_err.append(((err_main[i]/norm_flux[i])**(2.0)+(flux_main[i]*norm_err[i]/norm_flux[i]**(2.0))**(2.0))**(0.5))

#Claculates the baseflux from the first and last images
base_flux = []
base_err = []
for i in range(0, 134):
    base_flux.append(flux_main[i])
for i in range(548, len(flux_main)):
    base_flux.append(flux_main[i])

baseline_flux = sum(base_flux)/len(base_flux)

#Finds the normalized flux of the main star
norm_flux_final = []
norm_err_final = []
for i in range(0, len(main_ratio)):
    norm_flux_final.append(main_ratio[i]/baseline_flux)
    norm_err_final.append(main_ratio_err[i]/baseline_flux)

#Method to average data
norm_flux_final = norm_flux_final[0:619]
norm_err_final = norm_err_final[0:619]
average_flux_final = []
average_err_final = []
new_time = []
for i in range(0, 609, 10):
    f = norm_flux_final[i]+norm_flux_final[i+1]+norm_flux_final[i+2]+norm_flux_final[i+3]+norm_flux_final[i+4]+norm_flux_final[i+5]+norm_flux_final[i+6]+norm_flux_final[i+7]+norm_flux_final[i+8]+norm_flux_final[i+9]
    average_flux_final.append(f/10)
    new_time.append(time_main[i+4])

    e = norm_err_final[i]+norm_err_final[i+1]+norm_err_final[i+2]+norm_err_final[i+3]+norm_err_final[i+4]+norm_err_final[i+5]+norm_err_final[i+6]+norm_err_final[i+7]+norm_err_final[i+8]+norm_err_final[i+9]
    a = e/10.0
    diff = 0.0
    for j in range(0,9):
        diff = diff + ((a-norm_err_final[j+i])**2.0)

    average_err_final.append(((diff/9.0)**0.5)/(10.0**0.5))

#Finds averaged fluxes before, during, and after transient
norm_f_before = []
norm_f_during = []
norm_f_after = []
err_f_before = []
err_f_during = []
err_f_after = []

for i in range(0, 134):
    norm_f_before.append(main_ratio[i]/baseline_flux)
    err_f_before.append(main_ratio_err[i]/baseline_flux)
for i in range(200, 400):
    norm_f_during.append(main_ratio[i]/baseline_flux)
    err_f_during.append(main_ratio_err[i]/baseline_flux)
for i in range(548, len(main_ratio)):
    norm_f_after.append(main_ratio[i]/baseline_flux)
    err_f_after.append(main_ratio_err[i]/baseline_flux)

avg_f_before = sum(norm_f_before)/len(norm_f_before)
avg_err_before = sum(err_f_before)/len(err_f_before)/(len(err_f_before)**0.5)

avg_f_during = sum(norm_f_during)/len(norm_f_during)
avg_err_during = sum(err_f_during)/len(err_f_during)/(len(err_f_during)**0.5)

avg_f_after = sum(norm_f_after)/len(norm_f_after)
avg_err_after = sum(err_f_after)/len(err_f_after)/(len(err_f_after)**0.5)

print('Average normalized flux before:', avg_f_before, '+', avg_err_before)
print('Average normalized flux during:', avg_f_during, '+', avg_err_during)
print('Average normalized flux after:', avg_f_after, '+', avg_err_after)




#Plots all fluxes and the averaged flux
plt.figure(1)
plt.plot(time_main,norm_flux_main, label = 'Main')
plt.xlabel('Time [min]')
plt.ylabel('Normalized Flux')
plt.plot(time_1,norm_flux_1, label = '1')
plt.plot(time_2,norm_flux_2, label = '2')
plt.plot(time_3,norm_flux_3, label = '3')
plt.plot(time_4,norm_flux_4, label = '4')
plt.plot(time_5,norm_flux_5, label = '5')
plt.plot(time_6,norm_flux_6, label = '6')
plt.plot(time_7,norm_flux_7, label = '7')
plt.plot(time_8,norm_flux_8, label = '8')
plt.plot(time_9,norm_flux_9, label = '9')
plt.plot(time_10,norm_flux_10, label = '10')
plt.plot(time_main, norm_flux, label = 'avg')
plt.legend(loc = 'best')
plt.show()

#Plots Normalized flux of main star
plt.figure(2)
plt.errorbar(new_time,average_flux_final, yerr=average_err_final, fmt='o',  label = 'Main')
plt.xlabel('Time [min]')
plt.ylabel('Normalized Flux')
plt.legend(loc = 'best')
plt.show()
