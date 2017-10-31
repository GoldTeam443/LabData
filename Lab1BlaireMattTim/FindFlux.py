#import tools
import numpy as np
import math
import os
import datetime
import  time

#remove text files if nessicary
if os.path.isfile('Flux_Values_Main.txt'):
    os.remove('Flux_Values_Main.txt')
    os.remove('Flux_Values_1.txt')
    os.remove('Flux_Values_2.txt')
    os.remove('Flux_Values_3.txt')
    os.remove('Flux_Values_4.txt')
    os.remove('Flux_Values_5.txt')
    os.remove('Flux_Values_6.txt')
    os.remove('Flux_Values_7.txt')
    os.remove('Flux_Values_8.txt')
    os.remove('Flux_Values_9.txt')
    os.remove('Flux_Values_10.txt')

#Create heading for all 10 flux text files
f = open('Flux_Values_Main.txt', 'w')
f.write('Time[min],   Flux[counts],   Err[counts]')
f.close()
f = open('Flux_Values_1.txt', 'w')
f.write('Time[min],   Flux[counts],   Err[counts]')
f.close()
f = open('Flux_Values_2.txt', 'w')
f.write('Time[min],   Flux[counts],   Err[counts]')
f.close()
f = open('Flux_Values_3.txt', 'w')
f.write('Time[min],   Flux[counts],   Err[counts]')
f.close()
f = open('Flux_Values_4.txt', 'w')
f.write('Time[min],   Flux[counts],   Err[counts]')
f.close()
f = open('Flux_Values_5.txt', 'w')
f.write('Time[min],   Flux[counts],   Err[counts]')
f.close()
f = open('Flux_Values_6.txt', 'w')
f.write('Time[min],   Flux[counts],   Err[counts]')
f.close()
f = open('Flux_Values_7.txt', 'w')
f.write('Time[min],   Flux[counts],   Err[counts]')
f.close()
f = open('Flux_Values_8.txt', 'w')
f.write('Time[min],   Flux[counts],   Err[counts]')
f.close()
f = open('Flux_Values_9.txt', 'w')
f.write('Time[min],   Flux[counts],   Err[counts]')
f.close()
f = open('Flux_Values_10.txt', 'w')
f.write('Time[min],   Flux[counts],   Err[counts]')
f.close()

#Imports time data from text file where time was copied over using fits
time_data = np.loadtxt('ImageTimes.txt', usecols=(1), dtype=str)

#Iterate through all data files
for i in range (29, 656):
    
    #depending on which iteration we are on get the filename
    if i<100:
        filename = "wasp-93-b-r-band-data.000000" + str(i) + "_final.cat"
    else:
        filename = "wasp-93-b-r-band-data.00000" + str(i) + "_final.cat"

    #import data from the file and find how many values there are
    data  = np.loadtxt(filename, skiprows = 17)
    last_line = data[:][-1]
    last_value = int(last_line[0])

    #defines an error range in which our ra and dec must be within
    e_ra = 0.0007
    e_dec = 0.0007

    #counts will be used to check and make sure for each data file we have extracted 1 and only one parameter
    count = 0
    count_m = 0
    count_1 = 0
    count_2 = 0
    count_3 = 0
    count_4 = 0
    count_5 = 0
    count_6 = 0
    count_7 = 0
    count_8 = 0
    count_9 = 0
    count_10 = 0
    
    #Finds time in minutes
    tm = time.strptime(time_data[(i-29)], '%H:%M:%S.%f')
    tm = datetime.timedelta(hours=tm.tm_hour,minutes=tm.tm_min,seconds=tm.tm_sec).total_seconds()/60

    #iterates over all stars that were found using sexractor
    for j in range (0, last_value):
        
        #pulls all relevante data values at that star
        ra = data[j][3]
        dec = data[j][4]
        flux = data[j][5]
        err = data[j][6]

        #checks if the star applies to any of the 10 that we want or our main star
        #If it does it willwrite the time, flux, and error to the relevant text file
        #It will also iterate the count variables to make sure we are extracting all stars 
        if abs(ra-9.4589)<e_ra and abs(dec-51.2886)<e_dec:
            f = open('Flux_Values_Main.txt', 'a')
            data_1 = str([tm, flux, err]).strip('[]')
            f.write('\n' + data_1)
            f.close()
            count=count+1
            count_m = 1
        elif abs(ra-9.5378)<e_ra and abs(dec-51.2962)<e_dec:
            f = open('Flux_Values_1.txt', 'a')
            data_1 = str([tm, flux, err]).strip('[]')
            f.write('\n' + data_1)
            f.close()
            count=count+1
            count_1 = 1
        elif abs(ra-9.5881)<e_ra and abs(dec-51.3410)<e_dec:
            f = open('Flux_Values_2.txt', 'a')
            data_1 = str([tm, flux, err]).strip('[]')
            f.write('\n' + data_1)
            f.close()
            count=count+1
            count_2 = 1
        elif abs(ra-9.3692)<e_ra and abs(dec-51.2261)<e_dec:
            f = open('Flux_Values_3.txt', 'a')
            data_1 = str([tm, flux, err]).strip('[]')
            f.write('\n' + data_1)
            f.close()
            count=count+1
            count_3=1
        elif abs(ra-9.4864)<e_ra and abs(dec-51.1881)<e_dec:
            f = open('Flux_Values_4.txt', 'a')
            data_1 = str([tm, flux, err]).strip('[]')
            f.write('\n' + data_1)
            f.close()
            count=count+1
            count_4=1
        elif abs(ra-9.6204)<e_ra and abs(dec-51.1769)<e_dec:
            f = open('Flux_Values_5.txt', 'a')
            data_1 = str([tm, flux, err]).strip('[]')
            f.write('\n' + data_1)
            f.close()
            count=count+1
            count_5=1
        elif abs(ra-9.7185)<e_ra and abs(dec-51.2497)<e_dec:
            f = open('Flux_Values_6.txt', 'a')
            data_1 = str([tm, flux, err]).strip('[]')
            f.write('\n' + data_1)
            f.close()
            count=count+1
            count_6=1
        elif abs(ra-9.2291)<e_ra and abs(dec-51.3652)<e_dec:
            f = open('Flux_Values_7.txt', 'a')
            data_1 = str([tm, flux, err]).strip('[]')
            f.write('\n' + data_1)
            f.close()
            count=count+1
            count_7=1
        elif abs(ra-9.3169)<e_ra and abs(dec-51.2162)<e_dec:
            f = open('Flux_Values_8.txt', 'a')
            data_1 = str([tm, flux, err]).strip('[]')
            f.write('\n' + data_1)
            f.close()
            count=count+1
            count_8=1
        elif abs(ra-9.4093)<e_ra and abs(dec-51.2294)<e_dec:
            f = open('Flux_Values_9.txt', 'a')
            data_1 = str([tm, flux, err]).strip('[]')
            f.write('\n' + data_1)
            f.close()
            count=count+1
            count_9=1
        elif abs(ra-9.2540)<e_ra and abs(dec-51.3289)<e_dec:
            f = open('Flux_Values_10.txt', 'a')
            data_1 = str([tm, flux, err]).strip('[]')
            f.write('\n' + data_1)
            f.close()
            count=count+1
            count_10=1
    #Check is we extracted 11 parameters if not warn the user which one was not extracted
    if count != 11:
        if count_m !=1:
            print('main')
        elif count_1 !=1:
           print('1')
        elif count_2 !=1:
            print('2')

        elif count_3 !=1:
            print('3')

        elif count_4 !=1:
            print('4')

        elif count_5 !=1:
            print('5')

        elif count_6 !=1:
            print('6')

        elif count_7 !=1:
            print('7')

        elif count_8 !=1:
            print('8')

        elif count_9 !=1:
            print('9')

        elif count_10 !=1:
            print('10')


