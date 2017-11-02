#! /bin/bash -u

for file in $(ls -1 wasp-93-b-r-band-data.00000***.fits)
do
    ftpixcalc $(basename " $file" .fits)"_dark.fits" a-b a=$file b=Master_Dark.fits
done

for file in $(ls -1 wasp-93-b-r-band-data.00000**_dark.fits)
do
    ftpixcalc $(basename " $file" _dark.fits)"_final.fits" a/b a=$file b=Master_Flat_1.fits
done
