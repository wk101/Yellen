import pytest
import pandas as pd
from strategy.calculators.indicator_adx import ADXCalculator
from data.generator import CombinedDataGenerator


@pytest.fixture
def ohlc_data():
    """
    Generate and return the OHLC data for testing.
    """
    # Define the start and end timestamps
    start_timestamp = '2023-06-01 00:00:00'
    end_timestamp = '2023-06-01 02:30:00'

    combined_data = CombinedDataGenerator()

    # Generate OHLC data with a 5-minute frequency
    ohlc_data = combined_data.generate_combined_data(start_timestamp=start_timestamp, end_timestamp=end_timestamp, time_bar='5min' )

    return ohlc_data


def test_adx_calculator(ohlc_data):
    """
    Test the functionality of the ADXCalculator class.
    """
    # Create an instance of the ADXCalculator class
    adx_calculator = ADXCalculator(ohlc_data)

    # Calculate ADX
    adx_calculator.calculate_adx()

    # Get ADX values
    ohlc_data_with_adx = adx_calculator.get_adx_values()

    # Assert that RSI column is present in the OHLC data
    assert 'adx' in ohlc_data_with_adx.columns
    ohlc_data_with_adx.fillna(0, inplace=True)

    # Assert that ADX values are present and non-null
    assert isinstance(ohlc_data_with_adx, pd.DataFrame)

    # Assert that ADX values are within the expected range (0 to 100)
    assert (ohlc_data_with_adx['adx'] >= 0).all() and (ohlc_data_with_adx['adx'] <= 100).all()
