# Import Libraries
from pathlib import Path
import pandas as pd
import csv
import logging
from infraestructure.file_utils import file_to_dataframe
from domain.formatting_utils import column_names_formatting
from domain.explore_utils import info_dataframe

logger = logging.getLogger(__name__)

def main(file_name,sheet_name = None):
    df_bank = file_to_dataframe(file_name,sheet_name)
    df_bank= column_names_formatting(df_bank)
    df_bank_info = info_dataframe(df_bank)

    return df_bank_info


test_file = 'customer-details.xlsx'
test_sheet = '2012'
execute = main(test_file,test_sheet)
print(execute)

