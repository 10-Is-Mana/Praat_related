# Praat_related

## List of scripts

### (1) extract_tierinfo.py
-> This script extracts information from all the tiers in textgrids in a folder.
   A csv file is generated as a result.
   
### (2-1) get_duration_subf.py
-> This script extracts duration from textgrids of files that are embedded in subfolders.
   This script is a specific version of script get_duration.py
   A csv file is generated as a result.
   
### (2-2)get_duration.py
-> This script extract duration from textgrids of files in a folder
   A csv file is generated as a result.
   
### (3-1) praat_reprocess_v1_1.py
-> This script creates textgrids of a series of sound files in subfolders using information provided in a csv files. Sounds files must have textgrids. See below for details. Old textrids will be saved into a preassigned folder by the user.

### (3-2) praat_reprocess_v1.py
-> Superseded by v1_1


## How to Use the program
- prepare required files, folders, csv files
- download & save the program in the preferred location
- change direclty to the location where saved scripts via command `cd`
- install packages via `pip install [package name]` or `pip3 install [package name]`
- type `python3 [program name]`
- interact with Python (a.k.a, Python will ask for things, and you answer.)
      
      
## Copyright
created by Mana ASHIDA, contact : 10suism.ashida@gmail.com

## Acknowledgement
Thank you for the creator of [`praat-textgrids` package](https://github.com/Legisign/Praat-textgrids), and for the fact he makes this publically available!

## Support
This script is supported by the project at ReNeLDA, "Establishment of a Research Network for Exploring the Linguistic Diversity and Linguistic Dynamism in Africa."
