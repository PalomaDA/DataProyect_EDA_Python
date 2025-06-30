# Import Libraries
from pathlib import Path
import pandas as pd
import csv
import logging
import os

logger = logging.getLogger(__name__)

def main():
    base_path = Path(__file__).resolve().parents[1]
    path_bank =base_path.joinpath('files/input/bank-additional.csv')
    
    df_bank = pd.read_csv(path_bank)
    return df_bank.head()



execute = main()
print(execute)

