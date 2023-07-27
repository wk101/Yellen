import pytest
from yellen.stop_loss import StopLoss

@pytest.fixture
def stop_loss_instance():
    # Create an instance of StopLoss for testing
    return StopLoss()

@pytest.mark.parametrize("entry_price, rsi, is_long, expected_result", [
    # Test cases for long positions
    (100, 70, True, 99.9),  # RSI > 65, new stop loss 0.1% below entry price
    (100, 60, True, 0),     # RSI <= 65, new stop loss should be 0 (no adjustment)
    # Test cases for short positions
    (100, 30, False, 100.1),  # RSI < 35, new stop loss 0.1% above entry price
    (100, 40, False, 0),      # RSI >= 35, new stop loss should be 0 (no adjustment)
    # Add more test cases as needed
])
def test_adjust_level(stop_loss_instance, entry_price, rsi, is_long, expected_result):
    assert stop_loss_instance.adjust_level(entry_price, rsi, is_long) == expected_result
