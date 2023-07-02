import pytest
from strategy.calculators.signal_calculator import SignalCalculator


@pytest.mark.parametrize("adx_green, adx_red, rsi, expected_signal", [
    (1.5, 1.2, 25, "Long"),
    (0.8, 1.2, 75, "Short"),
    (1.3, 1.1, 40, "No Signal"),
    (1.2, 1.3, 70, "No Signal"),
])
def test_generate_signal(adx_green, adx_red, rsi, expected_signal):
    signal = SignalCalculator.generate_signal(adx_green, adx_red, rsi)
    assert signal == expected_signal
