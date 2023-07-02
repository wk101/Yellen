import pytest
from strategy.calculators.take_profit import TakeProfit

@pytest.fixture(scope="module")
def tp():
    return TakeProfit()

@pytest.mark.parametrize("trade_num, price, trade_type, expected", [
    # Test short trade
    (1, 100, "short", 80),  # 20% below
    (2, 110, "short", 103),  # 70% between 100 and 110
    (3, 115, "short", 106),  # 60% between 100 and 115
    (4, 114, "short", 107.0),  # 50% between 100 and 114
    (5, 120, "short", 111),  # 45% between 100 and 120
    # Test long trade
    (1, 100, "long", 120),  # 20% above
    (2, 90, "long", 97),  # 70% between 100 and 90 83 87 93
    (3, 80, "long", 92)  # 60% between 100 and 80 68 72
])
def test_take_profit(tp, trade_num, price, trade_type, expected):
    assert tp.calculate_tp(trade_num, price, trade_type) == expected


@pytest.mark.parametrize(
    "trades, new_trade, error_message", [
        ([(1, 100, "short"), (2, 110, "short")], (3, 102, "short"),
         "The given price crosses a previous take profit level"),
    ]
)
def test_price_crosses_previous_tp(trades, new_trade, error_message):
    tp = TakeProfit()
    for trade in trades:
        tp.add_trade(*trade)

    # Now attempt to add a trade that crosses the previous TP.
    with pytest.raises(ValueError, match=error_message):
        tp.add_trade(*new_trade)
