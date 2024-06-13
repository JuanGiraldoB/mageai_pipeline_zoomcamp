import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    months = [10, 11, 12]
    dataframes = []

    for month in months:
        url = f"""https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-{month}.csv.gz"""

        try:
            df = pd.read_csv(url, sep=",", compression="gzip")
            num_rows = df.shape[0]
            print(f"Month {month} has {num_rows} rows")
            dataframes.append(df)
        except Exception as e:
            print(f"Error loading data for month {month}: {e}")

    df = pd.concat(dataframes, ignore_index=True)
    print("Q1", df.shape)
    return df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
