#!/usr/bin/env python3
# created by Mana ASHIDA, 11-09-2020, ver.1.1

import glob
import csv
import textgrids

print("What is the path to the folder containing target TextGrids?")
path_in = input()
paths = glob.glob(path_in+"/*.TextGrid")

f = open(path_in+"/durations.csv", "w")
writer = csv.writer(f)

for path in sorted(paths):
    f_in = textgrids.TextGrid(path)
    writer.writerow([path.split("/")[-1], f_in.xmax])

f.close()
print("duration.csv is generated in "+path_in)
