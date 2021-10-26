# When I Work Code Challenge

When I Work Code Challenge - Erik Hendrickson

## Getting Started

These instructions provide a guide to installing and executing a program that meets the requirements defined in the file "Software_Engineer_Data_-_Code_Challenge.pdf"

## Requirements

This software requires [Python 3](https://www.python.org/), [pip](https://pypi.org/project/pip/), and the [pandas](https://pandas.pydata.org/) python library.
## Installing

To install pandas:
```
pip install pandas
```

Alternatively, a "requirements.txt" file is also provided. Requirements can be automatically installed in this way:
```
pip install -r requirements.txt
```
## Execution
The application can be executed by entering

```
python web_traffic_transformation.py
```
## Output
The application will output a file named "web_traffic_pivoted.csv" containing data transformed per the requirements in CSV format.

The raw data file can also be output using the "save_raw_files" flag described below.

## Execution Options

Certain items can be modified to change the execution of the application. These are done in-code in the "Variables" section of the main function.

These options are:

### Filenames
Filenames are initially set to a list of lowercase characters from a to z, in this way:
```
filenames = list(string.ascii_lowercase)
```
They can also be set manually
```
filenames = ['a','b']
```

### File Extension
The file extension can be modified, but the default is set to ".csv" here:
```
extension = '.csv'
```

### Base URL
The base URL location of the files can be modified manually as well. The default is set as:
```
base_url = 'https://public.wiwdata.com/engineering-challenge/data/'
```

### Saving of Raw Data Files
The raw data files (named "a.csv", "b.csv", ... "z.csv" in the default example) can be saved for debugging purposes. Simply set the below flag to 1:
```
save_raw_files = 0
```