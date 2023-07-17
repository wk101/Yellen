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
                print(f"Trailing stop loss adjusted for LONG position. New level: {new_stop_loss:.2f}")
            else:
                new_stop_loss = 0
                print("RSI is not above 65. No change in stop loss for LONG position.")
        else:
            if rsi < 35:
                # Set the stop loss level for short position as 0.1% above the entry price
                new_stop_loss = entry_price + (entry_price * 0.001)
                print(f"Trailing stop loss adjusted for SHORT position. New level: {new_stop_loss:.2f}")
            else:
                new_stop_loss = 0
                print("RSI is not below 35. No change in stop loss for SHORT position.")

        return new_stop_loss
