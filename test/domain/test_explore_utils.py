# Import Libraries
from eda.domain.explore_utils import (
    info_dataframe
)
import pytest
import pandas as pd

@pytest.fixture
def test_dataframe():
    return pd.DataFrame({ "COL_1":["uno", "dos", None],
                                              "COL_2":[1,2,3]
                                            })

# Tests for function info_dataframe
def test_info_dataframe_non_null_count(test_dataframe):
    df_info = info_dataframe(test_dataframe)
    assert int(df_info["non_null_count"][0]) == 2
    assert int(df_info["non_null_count"][1]) == 3

def test_info_dataframe_null_count(test_dataframe):
    df_info = info_dataframe(test_dataframe)
    assert int(df_info["null_count"][0]) == 1
    assert int(df_info["null_count"][1]) == 0

def test_info_dataframe_null_percent(test_dataframe):
    df_info = info_dataframe(test_dataframe)
    assert float(df_info["null_percent"][0]) == 33.33
    assert float(df_info["null_percent"][1]) == 0.00

def test_info_dataframe_non_dtype(test_dataframe):
    df_info = info_dataframe(test_dataframe)
    assert str(df_info["dtype"][0]) == "object"
    assert str(df_info["dtype"][1]) == "int64"