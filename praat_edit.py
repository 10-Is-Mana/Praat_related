#!/usr/bin/env python3
# created by Mana ASHIDA, 03-09-2020, ver.1.1

import textgrids
import csv

"""
This program reprocess the existing TextGrids and generate TextGrids which have the following tiers:
1 segment (leave empty)
2 target (column C) = [2]
3 gloss (column D) = [3]
4 sentence (column E) = [1]
5 archive id (column A) = [0]
"""

# functions for editing TextGrid
# adding tiers
def add_tiers(tiername, f_in, max, text):
    f_in.update({tiername:textgrids.Tier()})
    f_in[tiername].xmax = max
    f_in[tiername].append(textgrids.Interval())
    f_in[tiername][0].xmax = max
    f_in[tiername][0].text = text

# initialize - delete all the existing tiers
def pop(f_in):
    f_in.popitem()
    return f_in

# main function, input : one column of csv file
def main(csv_col, path_in, path_out):
    filename = csv_col[1].replace(".wav", ".TextGrid")
    filepath = f'{path_in}/{csv_col[4]}/{filename}'

    f_in = textgrids.TextGrid(filepath)
    f_in.write(f'{path_out}/{filename}')

    max = f_in.xmax

    for _ in range(len(f_in)):
        pop(f_in)

    add_tiers("segment", f_in, max, "")
    add_tiers("target", f_in, max, csv_col[2])
    add_tiers("gloss", f_in, max, csv_col[3])
    add_tiers("sentence", f_in, max, csv_col[1])
    add_tiers("archive id", f_in, max, csv_col[0])

    f_in.write(filepath)

# reading csv file (from excel, par sheet)
print("What is the path of the csv file?")
path = input()

with open(path) as f:
    csv_in = [line for line in csv.reader(f)]

print("Where are the files that need reprocessing?")
f_in = input()

if f_in == "":
    print("Error: required path not provided")
    sys.exit()

print("Where do you want to save the existing TextGrid files?")
f_out = input()

if f_out == "":
    print("Error: required path not provided")    
    sys.exit()

for line in csv_in[1:]:
    try:
        main(line, f_in, f_out)
    except FileNotFoundError:
        print(f'{line[7]} is not in the folder')
