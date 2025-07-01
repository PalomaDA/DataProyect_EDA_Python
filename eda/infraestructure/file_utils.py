# Import Libraries
from pathlib import Path
import pandas as pd
import csv
import logging

logger = logging.getLogger(__name__)

# FUNCTIONS

# Open file
def detectFileExt(file_name, sheet=None):
    base_path = Path(__file__).resolve().parents[2]
    final_path = base_path / 'files' / 'input' / file_name
    file_ext = file_name.split('.')[1]

    try:
        if file_ext =='csv':
            return pd.read_csv(final_path)
        if file_ext == 'xlsx':
            print(f'Path: {final_path}')
            return  pd.read_excel(final_path,sheet)
        else:
            logger.info("File extension not supported")
            return None 
    except FileNotFoundError:
        print(f'Path: {final_path}')
        logger.error('No file found')


# Testing
# test_file = 'customer-details.xlsx'
# test_sheet = '2012'
# df = detectFileExt(test_file,test_sheet)
# print(df)




