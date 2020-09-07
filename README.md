# Praat_related

## Expected Use case
This script is useful for the situation that you want to edit the existing TextGrids Tier information (tier name, tier text). The pre-edit version of the TextGrids are saved into the folder you indicated via the dialog with Python. Editing Tier includes deleting/adding Tiers as well. 


## Requirements
Csv file should follow this format.
|  A  |  B  |  C  |  D  |  E  |  F  |
| ---- | ---- | ---- | ---- | ---- | ---- |
|  ID  |  filename  |  text  |  gloss |  foldername |

the directly is nested, for example, in this format
main --- speaker A - .wav and .textgrids
      |- speaker B - .wav and .textgrids
      |- speaker C - .wav and .textgrids
    

context, 
re-create praat textgrids according to the information from csv file

how to use,
prepare csv file
install praat-textgrids package via pip install
type python3 [] 
then python will ask : 
then python will ask : 
then python will ask : 

copyright
created by Mana ASHIDA
note: the praat-textgrids package is in XXX licensce.

support
This script is a part of the project at Asia-africa institute, which helps automatize re-formatting existing files for publishing.

