#! /bin/bash -u

for file in $(ls -1 wasp-93-b-r-band-data.*_final.new)
do 
    sex ${file} -c default.se -CATALOG_NAME $(basename " $file" .new)".cat"

done
