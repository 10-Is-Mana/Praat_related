#!/usr/bin/env python3
# created by Mana ASHIDA, 12-09-2020, ver.1.2
import sys
import os
import glob
import csv
import pathlib
from tqdm import tqdm
import textgrids

print("What is the path to the folder containing target TextGrids?")
path_in = input()

if os.path.isfile(path_in+"/0_durations.csv"):
    print("Are you sure to override 0_0_durations.csv in the "+path_in+"? (yes/no)")
    if input() != "yes":
        sys.exit()

p_temp = pathlib.Path(path_in)
dirs = [p.name for p in p_temp.iterdir() if p.is_dir()]
dirs.append(path_in)

paths = []
for dire in dirs:
    paths.extend(glob.glob(path_in+"/"+dire+"/*.TextGrid"))

if len(paths) == 0:
    print("No TextGrids in the folders "+path_in)
    sys.exit()

f = open(path_in+"/0_durations.csv", "w")
writer = csv.writer(f)

paths.sort()
# print(paths)
for path in tqdm(paths):
    f_in = textgrids.TextGrid(path)
    writer.writerow([path.split("/")[-2], path.split("/")[-1], f_in.xmax])

f.close()
print("0_duration.csv is generated in "+path_in)
