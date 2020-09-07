# Praat_related
1. Praat_edit.py


## Expected Use Case
This script is useful for the situation that you want to edit the existing TextGrids Tier information (tier name, tier text). The pre-edit version of the TextGrids are saved into the folder you indicated via the dialog with Python. Editing Tier includes deleting/adding Tiers as well. 


## Requirements
Csv file should follow this format.
|  A  |  B  |  C  |  D  |  E  |
| ---- | ---- | ---- | ---- | ---- | 
|  ID  |  soundfile name  |  target  |  gloss |  folder name |

The directly is nested, for example, in this format
main --- speaker A - .wav and .textgrids
      |- speaker B - .wav and .textgrids
      |- speaker C - .wav and .textgrids
    

## How to Use the program
- prepare csv file as required
- download & save the program in the preferred location
- change direclty to the saved location via command `cd`
- install praat-textgrids package via `pip install praat-textgrids` or `pip3 install praat-textgrids`
- type `python3 praat_edit.py`

      python will ask : `What is the path of the csv file?`
      
      python will ask : `Where are the files that need reprocessing?`
      
      python will ask : `Where do you want to save the existing TextGrid files?`
      

## Copyright
created by Mana ASHIDA, 10suism.ashida@gmail.com

`praat-textgrids` package[https://github.com/Legisign/Praat-textgrids] is a free software.

## Support
This script is supported by the project at ReNeLDA, "Establishment of a Research Network for Exploring the Linguistic Diversity and Linguistic Dynamism in Africa."
