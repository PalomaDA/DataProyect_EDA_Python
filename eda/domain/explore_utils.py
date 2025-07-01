#Import libraries
import logging
import pandas as pd

logger = logging.getLogger(__name__)

# Funtions
def info_dataframe(df):
    '''
    Generates a summary dataframe with basic info od the dataframe: count not null and null values in columns, perfect of null values and types.

    Args:
    - df: dataframe

    Returns
    - Summary dataframe
    '''
    column_info = []
    total_rows = len(df)
    
    for col in df.columns:
        non_null_count = int(df[col].notnull().sum())
        null_count = total_rows - non_null_count
        null_percent = round( null_count / total_rows * 100, 2)
        dtype = df[col].dtype

        column_info.append(
            {
                "column_name" : col,
                "non_null_count" : non_null_count,
                "null_count" : null_count,
                "null_percent" : null_percent,
                "dtype" : dtype
            }
        )
    
    info_df = pd.DataFrame(column_info)

    return info_df