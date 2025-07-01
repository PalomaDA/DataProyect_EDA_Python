#Import libraries
import logging
import pandas as pd

# Funtions
def info_dataframe(df):
    column_info = []
    

    for col in df.columns:
        non_null_count = int(df[col].notnull().sum())
        null_count = int(df[col].null().sum())
        dtype = df[col].dtype

        column_info.append(
            {
                "column_name" : col,
                "non_null_count" : non_null_count,
                "null_count" : null_count,
                "dtype" : dtype
            }
        )
    
    info_df = pd.DataFrame(column_info)

    return info_df