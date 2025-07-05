# Import Libraries
from eda.domain.formatting_utils import (
    column_names_formatting
)
import pytest
import pandas as pd

# Creation of test dataframe
@pytest.fixture
def test_dataframe():
    return pd.DataFrame({'Column.1':[1,2], 
                                            'column.DOs':[3,4],
                                            'COlumn_3':[5,6]})


# Tests for function column_names_formatting
def test_column_names_formatting(test_dataframe):
    df = column_names_formatting(test_dataframe)
    assert df.columns[0] == 'COLUMN_1'
    assert df.columns[1] == 'COLUMN_DOS'
    assert df.columns[2] == 'COLUMN_3'