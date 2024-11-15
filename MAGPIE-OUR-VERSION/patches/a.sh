#!/bin/bash

# cd /home/me/myfolder2tocleanup/

# Exit if the directory isn't found.
if (($?>0)); then
    echo "Can't find work dir... exiting"
    exit
fi

for i in *; do
    if ! grep -qxFe "$i" ../filelist.txt; then
        echo "Deleting: $i"
        # the next line is commented out.  Test it.  Then uncomment to removed the files
        rm "$i"
    fi
done