# openstereo_addon
A simple Python module for reading data from FieldMove CLINO with OpenStereo.

## Table of contents
- [Introduction](#introduction)
- [Functions](#functions)
  - [clino_to_txt](#clino_to_txt) 

## Introduction
`openstereo_addon` is a __Python module__ made to __facilitate data processing__ of [FieldMove CLINO](https://www.petex.com/products/move-suite/digital-field-mapping/) files (in CSV format) to view data on [OpenStereo](https://openstereo.readthedocs.io/en/latest/) opensource software.
`openstereo_addon` relies on __Pandas__, __NumPy__ and __os__ libraries to select files directory, gather data from CSV files and export them according to the user's choices.  
_Versions currently used in `openstereo_addon` :_
- _[Python](https://www.python.org/) : 3.9.16_
- _[NumPy](https://numpy.org/doc/stable/) : 1.23.5_
- _[Pandas](https://pandas.pydata.org/) : 1.5.3_

If you want to import the module into a Python file, __be sure to move `openstereo_addon.py` to the same folder as your Python file__. You can now import `openstereo_addon` :
```python
import openstereo_addon
```
To initiate `openstereo_addon` on a specific folder, enter in the class parameter the folder path :
```python
import openstereo_addon
opa = openstereo_addon('D:\\path\\to\\a\\folder')
```

## Functions
This section lists the `openstereo_addon` __functions__, their __description__ and __related examples__. Input parameters and their format can be found in each __function documentation__.    

### clino_to_txt
`clino_to_txt` allows to convert a list of FieldMove CLINO CSV files in TXT format compatible with OpenStereo. Input parameters allow to filter over data and select specific types of geological planes or lines. `clino_to_txt` selects __dipAzimuth__ and __dip__ for __planes__ files and __plungeAzimuth__ and __plunge__ for __lines__ files.  
_Example_ :
```python
import openstereo_addon
opa = openstereo_addon('D:\\path\\to\\a\\folder')

opa.clino_to_txt(['file1','file2','file3'], locality='Locality 1', unit='Carbonate', data_type='Bedding')
# the output will be 'Locality1_Carbonate_Bedding.txt'

opa.clino_to_txt(['file4'], locality='Locality 1', data_type='Fault',output_name='FaultCarbonate')
# the output will be 'FaultCarbonate.txt'
```
