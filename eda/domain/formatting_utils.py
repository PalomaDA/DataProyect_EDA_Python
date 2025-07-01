#Import libraries
import logging
import pandas

logger = logging.getLogger(__name__)

# Funtions
def column_names_formatting(df):
    '''
    Format dataframe column names to lower, underscore for separation between words and start and end spaces striped.

    Args:
    - df: dataframe to format

    Returns:
    - Dataframe with the column names in the desired format.
    '''
    col_names = df.columns
    col_name_map = {}
    for col in col_names:
        new_name = col.strip().replace("_","").replace(".","_").lower()
        col_name_map[col] = new_name
    try:
        df = df.rename(columns=col_name_map)
        return df
    except:
        logger.error('Error formatting dataframe column names')