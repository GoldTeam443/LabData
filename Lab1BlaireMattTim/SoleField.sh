#! /bin/bash -u

for file in $(ls -1 wasp-93-b-r-band-data.*_final.fits)
do 
    solve-field --ra 9.4583 --dec 51.2889 --radius 1 ${file}
done
