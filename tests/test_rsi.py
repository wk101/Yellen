import pytest
from strategy.calculators.indicator_rsi import RSICalculator
from data.generator import CombinedDataGenerator


@pytest.fixture
def ohlc_data():
    """
    Generate and return the OHLC data for testing.
    """
    # Define the start and end timestamps
    start_timestamp = '2023-06-01 00:00:00'
    end_timestamp = '2023-06-01 02:30:00'

    # Generate OHLC data with a 5-minute frequency
    cdg = CombinedDataGenerator()
    ohlc_data = cdg.generate_combined_data(start_timestamp, end_timestamp, time_bar='5min')

    return ohlc_data


def test_rsi_calculator(ohlc_data):
    """
    Test the functionality of the RSICalculator class.
    """
    # Create an instance of the RSICalculator class
    rsi_calculator = RSICalculator(ohlc_data=ohlc_data, period=14)

    # Calculate RSI
    rsi_calculator.calculate_rsi()

    # Get OHLC data with RSI column
    ohlc_data_with_rsi = rsi_calculator.get_ohlc_data()

    # Assert that RSI column is present in the OHLC data
    assert 'rsi' in ohlc_data_with_rsi.columns
    ohlc_data_with_rsi.fillna(0, inplace=True)
    # Assert that the RSI values are within the expected range (0 to 100)
    assert (ohlc_data_with_rsi['rsi'] >= 0).all() and (ohlc_data_with_rsi['rsi'] <= 100).all()
