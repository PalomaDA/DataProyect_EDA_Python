# Import Libraries
from pathlib import Path
import pandas as pd
import csv


# FUNCTIONS

# Open file
def detectFileExt(file_name, sheet=None):
    path = Path( '../../files/input')
    final_path = path / file_name
    file_ext = file_name.split('.')[1]
    try:
        if file_ext =='csv':
            return pd.read_csv(final_path)
        if file_ext == 'xlsx':
            return  pd.read_excel(final_path,sheet)
        else:
            return print("File extension not supported")
    except FileNotFoundError:
        print('No file found')


# Testing
test_file = 'customer-details.xlsx'
test_sheet = 2012
df = detectFileExt(test_file, test_sheet)
print(df.head())




