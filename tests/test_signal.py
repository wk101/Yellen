import os

# Get the parent directory of the current script (assuming both files are in the same parent directory)
parent_dir = os.path.dirname(os.path.abspath(__file__))

# Add the parent directory to the Python path
sys.path.append(parent_dir)

import pytest
from signal_rules import SignalRules


@pytest.fixture
def signal_rules_instance():
    # Create an instance of SignalRules for testing
    return SignalRules()

@pytest.mark.parametrize("adx_green, adx_red, rsi, expected_result", [
    # Test cases for check_long_signal method
    (20, 15, 35, False),  # Signal rules not satisfied
    (25, 20, 25, True),   # Signal rules satisfied
    # Add more test cases as needed
])
def test_check_long_signal(signal_rules_instance, adx_green, adx_red, rsi, expected_result):
    assert signal_rules_instance.check_long_signal(adx_green, adx_red, rsi) == expected_result

@pytest.mark.parametrize("adx_green, adx_red, rsi, expected_result", [
    # Test cases for check_short_signal method
    (20, 25, 60, False),  # Signal rules not satisfied
    (30, 35, 75, True),   # Signal rules satisfied
    # Add more test cases as needed
])
def test_check_short_signal(signal_rules_instance, adx_green, adx_red, rsi, expected_result):
    assert signal_rules_instance.check_short_signal(adx_green, adx_red, rsi) == expected_result

def test_reset(signal_rules_instance):
    # Test the reset method

    # Set some initial values to True
    signal_rules_instance.adx_green_over_red = True
    signal_rules_instance.adx_red_over_green = True
    signal_rules_instance.rsi_below_30 = True
    signal_rules_instance.rsi_above_30 = True
    signal_rules_instance.rsi_above_70 = True
    signal_rules_instance.rsi_below_70 = True

    # Call the reset method
    signal_rules_instance.reset()

    # Check if all values are reset to False
    assert not signal_rules_instance.adx_green_over_red
    assert not signal_rules_instance.adx_red_over_green
    assert not signal_rules_instance.rsi_below_30
    assert not signal_rules_instance.rsi_above_30
    assert not signal_rules_instance.rsi_above_70
    assert not signal_rules_instance.rsi_below_70

    # Add more reset test cases as needed

