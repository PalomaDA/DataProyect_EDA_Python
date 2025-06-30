# Import Libraries
from pathlib import Path
import pandas as pd
import csv
import logging
from infraestructure.file_utils import detectFileExt

logger = logging.getLogger(__name__)

def main(file_name,sheet_name = None):
    df_bank = detectFileExt(file_name,sheet_name)
    return df_bank.head()


test_file = 'bank-additional.csv'
test_sheet = '2012'
execute = main(test_file)
print(execute)

