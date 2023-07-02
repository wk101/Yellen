import pytest
import numpy as np
import pandas as pd
from backtester.sharpe_ratio import SharpeRatioCalculator


@pytest.fixture
def sample_ohlcv_data():
    return pd.DataFrame({'Returns': [0.01, -0.02, 0.03, 0.01, -0.02]})


def test_sharpe_ratio_calculator(sample_ohlcv_data):
    # Create sample OHLCV data
    ohlcv_data = sample_ohlcv_data
    risk_free_rate = 0.02

    # Create an instance of SharpeRatioCalculator
    sharpe_calculator = SharpeRatioCalculator(ohlcv_data)

    # Calculate Sharpe Ratio
    result = sharpe_calculator.calculate_sharpe_ratio(risk_free_rate)

    # Check if the 'Sharpe Ratio' column is added to the DataFrame
    assert 'Sharpe Ratio' in result.columns

    # Check if the calculated Sharpe Ratio value is correct
    expected_sharpe_ratio = (np.mean(ohlcv_data['Returns']) - risk_free_rate) / np.std(ohlcv_data['Returns'])
    assert result['Sharpe Ratio'].iloc[-1] == expected_sharpe_ratio

