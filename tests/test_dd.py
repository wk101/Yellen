import pytest
from backtester.draw_down import MaxDrawdown
from data.generator import CombinedDataGenerator

@pytest.fixture
def fx_data():
    """
    Generate a OHLC DataFrame with a 'Return' column for FX data with 5-minute bars.
    """
    # Define the start and end timestamps
    start_timestamp = '2023-06-01 00:00:00'
    end_timestamp = '2023-06-01 02:30:00'
    cdg = CombinedDataGenerator

    # Generate OHLC data with a 5-minute frequency
    ohlc_data = cdg.generate_combined_data(start_timestamp, end_timestamp, time_bar='5min')

    return ohlc_data


def test_calculate(fx_data):
    """
    Test the calculate method of MaxDrawdown class.
    """
    max_drawdown = MaxDrawdown(fx_data)

    result = max_drawdown.calculate()

    assert 'max_drawdown' in result
    assert 'peak_date' in result
    assert 'trough_date' in result
