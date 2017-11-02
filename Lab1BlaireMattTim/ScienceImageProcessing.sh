#! /bin/bash -u

for file in $(ls -1 wasp-93-b-r-band-data.00000***.fits)
do
    ftpixcalc $(basename " $file" .fits)"_dark.fits" a-b a=$file b=Master_Dark.fits
done

for file in $(ls -1 wasp-93-b-r-band-data.00000**_dark.fits)
do
    ftpixcale $((basename " $file" _dark.fits)"_corrected.fits" a-b a=$file b=bad_pixel_map.fits
done

for file in $(ls -1 wasp-93-b-r-band-data.00000**_dark.fits)
do
    ftpixcalc $(basename " $file" _corrected.fits)"_final.fits" a/b a=$file b=Master_Flat_1.fits
done
