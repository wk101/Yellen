import os
import sys
# Get the parent directory of the current script (assuming both files are in the same parent directory)
parent_dir = os.path.dirname(os.path.abspath(__file__))

# Add the parent directory to the Python path
sys.path.append(parent_dir)

import pytest
from take_profit import TakeProfit

@pytest.fixture(scope="module")
def tp():
    return TakeProfit()

@pytest.mark.parametrize("trade_num, price, trade_type, expected", [
    # Test short trade
    (1, 100, "short", 80),    # 20% below
    (2, 110, "short", 103),   # 70% between 100 and 110
    (3, 115, "short", 106),   # 60% between 100 and 115
    (4, 114, "short", 107.0), # 50% between 100 and 114
    (5, 120, "short", 111),   # 45% between 100 and 120
    # Test long trade
    (1, 100, "long", 120),    # 20% above
    (2, 90, "long", 97),      # 70% between 100 and 90 83 87 93
    (3, 80, "long", 92)       # 60% between 100 and 80 68 72
])
def test_calculate_tp(tp, trade_num, price, trade_type, expected):
    assert tp.calculate_tp(trade_num, price, trade_type) == expected

def test_price_crosses_previous_tp():
    tp = TakeProfit()

    # Add a trade that sets the first trade price (price=100, trade_type="short")
    tp.calculate_tp(1, 100, "short")

    # Add a second trade (price=110, trade_type="short")
    tp.calculate_tp(2, 110, "short")

    
    # Error taken out - Now attempt to add a third trade with price=102, which will cross the previous TP (103).
    # with pytest.raises(ValueError, match="The given price crosses a previous take profit level"):
    #    tp.calculate_tp(3, 102, "short")
