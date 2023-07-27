import os
import sys

# Get the parent directory of the current script (assuming both files are in the same parent directory)
parent_dir = os.path.dirname(os.path.abspath(__file__))

# Add the parent directory to the Python path
sys.path.append(parent_dir)

import pytest
from signal_rules import SignalRules


import pytest
from signal_rules import SignalRules

@pytest.fixture
def signal_rules_instance():
    return SignalRules()

def test_check_long_signal():
    # Create an instance of SignalRules for testing
    signal_rules = SignalRules()

    # Test case 1: Signal rules not satisfied for a long position
    adx_green = 20
    adx_red = 25
    rsi = 25
    assert signal_rules.check_long_signal(adx_green, adx_red, rsi) is False

    # Test case 2: Signal rules satisfied for a long position
    adx_green = 25
    adx_red = 20
    rsi = 25
    assert signal_rules.check_long_signal(adx_green, adx_red, rsi) is True

    # Test case 3: Signal rules satisfied for a long position
    adx_green = 25
    adx_red = 20
    rsi = 35
    assert signal_rules.check_long_signal(adx_green, adx_red, rsi) is True

def test_check_short_signal():
    # Create an instance of SignalRules for testing
    signal_rules = SignalRules()

    # Test case 1: Signal rules not satisfied for a short position
    adx_green = 30
    adx_red = 35
    rsi = 60
    assert signal_rules.check_short_signal(adx_green, adx_red, rsi) is False

    # Test case 2: Signal rules not satisfied for a short position
    adx_green = 20
    adx_red = 25
    rsi = 70
    assert signal_rules.check_short_signal(adx_green, adx_red, rsi) is False

    # Test case 3: Signal rules satisfied for a short position
    adx_green = 30
    adx_red = 35
    rsi = 75
    assert signal_rules.check_short_signal(adx_green, adx_red, rsi) is True
