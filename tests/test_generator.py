import pandas as pd
import pytest
from data.generator import CombinedDataGenerator


@pytest.fixture(scope="module")
def combined_data():
    start_timestamp = '2023-06-01 00:00:00'
    end_timestamp = '2023-06-01 02:30:00'
    time_bar = '5min'

    # Generate the combined data using the CombinedDataGenerator
    combined_data = CombinedDataGenerator.generate_combined_data(start_timestamp, end_timestamp, time_bar)

    return combined_data


def test_combined_data(combined_data):
    assert isinstance(combined_data, pd.DataFrame)
    assert len(combined_data) > 0
    assert 'timestamp' in combined_data.columns
    assert 'open' in combined_data.columns
    assert 'high' in combined_data.columns
    assert 'low' in combined_data.columns
    assert 'close' in combined_data.columns
    assert 'volume' in combined_data.columns
    assert 'trade_id' in combined_data.columns
    assert 'trade_type' in combined_data.columns
    assert 'tp' in combined_data.columns
    assert 'sl' in combined_data.columns
    assert 'position_id' in combined_data.columns
    assert 'position_type' in combined_data.columns
    assert 'position_amount' in combined_data.columns
    assert 'trade_quantity' in combined_data.columns
    assert 'position_amount_open' in combined_data.columns
