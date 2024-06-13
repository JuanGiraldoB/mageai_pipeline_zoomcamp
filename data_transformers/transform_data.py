if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


import pandas as pd


@transformer
def transform(data, *args, **kwargs):
    data = data[(data['passenger_count'] != 0) & (data['trip_distance'] != 0)]
    data.columns = (data.columns.str.replace(' ', '_').str.lower())
    data.rename(columns={'vendorid': 'vendor_id'}, inplace=True)
    data['lpep_pickup_datetime'] = pd.to_datetime(data['lpep_pickup_datetime'])
    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date
    # del data['lpep_pickup_datetime']
    data.dropna(subset=['vendor_id'], inplace=True)
    print("Q2", data.shape[0])
    unique_values = data['vendor_id'].unique()
    print("Q4", unique_values)
    print("Q5", 4)
    return data


@test
def test_vendor_id(output, *args) -> None:
    assert 'vendor_id' in output.columns, 'The output is undefined'


@test
def test_passenger_count(output, *args) -> None:
    assert output['passenger_count'].sum() > 0, 'The output is undefined'


@test
def test_trip_distance(output, *args) -> None:
    assert output['trip_distance'].sum() > 0, 'The output is undefined'
