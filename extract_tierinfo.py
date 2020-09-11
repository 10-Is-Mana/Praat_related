#!/usr/bin/env python3
# created by Mana ASHIDA, 11-09-2020, ver.1.0

import glob
import csv
import textgrids
from tqdm import tqdm

print("What is the path to the folder containing target TextGrids?")
path_in = input()
paths = glob.glob(path_in+"/*.TextGrid")

f = open(path_in+"/TierInfos.csv", "w")
writer = csv.writer(f)

for path in tqdm(sorted(paths)):
    f_in = textgrids.TextGrid(path)
    info = []
    info.append(path.split("/")[-1])
    for elem in f_in:
        interval = []
        for seg in f_in[elem]:
            interval.append(seg.text)
        info.append(" ".join(interval))
    writer.writerow(info)

f.close()
print("TierInfos.csv is generated in "+path_in)
