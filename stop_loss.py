#region imports
from AlgorithmImports import *
#endregion
from AlgorithmImports import *
from QuantConnect import *
class StopLoss:
    def __init__(self):
        pass

    def adjust_level(self, entry_price: float, rsi: float, is_long: bool) -> float:
        """
        Adjust the stop loss level based on RSI and position type (long or short).

        Args:
            entry_price (float): The entry price of the position.
            rsi (float): The current RSI value.
            is_long (bool): True if the position is long, False if it is short.

        Returns:
            float: The new stop loss level.
        """
        if is_long:
            if rsi > 65:
                # Set the stop loss level for long position as 0.1% below the entry price
                new_stop_loss = entry_price - (entry_price * 0.001)
            else:
                new_stop_loss = 0
        else:
            if rsi< 35:
                # Set the stop loss level for short position as 0.1% above the entry price
                new_stop_loss = entry_price + (entry_price * 0.001)
            else:
                new_stop_loss = 0

        return new_stop_loss
