#region imports
#endregion
class OrderSize:
    def __init__(self, initial_size: float, _lot_size: float = 100000 ) -> None:
        self.initial_size: float = initial_size
        self.current_size: float = initial_size
        self.scale_factor: float = 1.3
        self.lot_size: int =  _lot_size # Base lot size

    def reset_size(self) -> None:
        self.current_size = self.initial_size

    def calculate_size(self, trade_number: int) -> float:
        """
        Calculate the order size for a given trade number.

        Args:
            trade_number (int): The trade number.

        Returns:
            float: The calculated order size in lots.
        """

        if trade_number > 30:
            self.reset_size()
            trade_number = 1  # Reset to initial order size after 30 trades

        # Compute size in lots
        # Apply the scaling factor to the initial size for each trade
        # Subtracting 1 from trade_number is necessary because trade_number is used as an exponent for the scaling factor.
        # Since trade_number starts from 1, we subtract 1 to ensure that the first trade (trade_number = 1) applies the scaling factor once.
        # If we don't subtract 1, the first trade will be multiplied by self.scale_factor ** 1 instead of self.scale_factor ** 0,
        # resulting in an incorrect scaling factor for subsequent trades.
        # By subtracting 1, we ensure that the scaling factor is correctly applied for each trade.

        self.current_size = self.initial_size * self.scale_factor ** (trade_number - 1)
        return round(self.current_size/self.lot_size)*self.lot_size   # Convert to units of base currency
