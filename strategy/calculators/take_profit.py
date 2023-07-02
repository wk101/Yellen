from typing import List, Optional


class TakeProfit:
    """
    A class to represent a take profit adjustment mechanism.

    Attributes
    ----------
    tp_values : List[float]
        A list containing percentage values for take profit adjustments.
    first_trade_price: Optional[float]
        The price of the first trade. None if no trades have been executed.
    last_tp_level: Optional[float]
        The last calculated take profit level. None if no trades have been executed.

    Methods
    -------
    calculate_tp(trade_count:int, price:float, trade_type:str):
        Returns the calculated take profit level based on the number of trades, the latest price, and the trade type.
    """

    def __init__(self):
        """
        Constructs the necessary attributes for the TakeProfit object.
        """

        self.tp_values = [0.7, 0.6, 0.5, 0.45, 0.4, 0.35, 0.3, 0.28, 0.26, 0.24, 0.22, 0.2,
                          0.18, 0.16, 0.15, 0.14, 0.13, 0.12, 0.11, 0.1, 0.08, 0.07, 0.065,
                          0.06, 0.055, 0.05, 0.047, 0.044, 0.04]
        self.first_trade_price = None
        self.last_tp_level = None

    def calculate_tp(self, trade_count: int, price: float, trade_type: str) -> float:
        """
        Returns the calculated take profit level based on the number of trades, the latest price, and the trade type.

        Raises ValueError if the given price crosses the previous take profit level.
        """

        # If it's the first trade, store the price and set TP at 20% below (for short) or above (for long)
        if trade_count == 1:
            self.first_trade_price = price

            if trade_type == "long":
                tp_level = price * 1.2
            elif trade_type == "short":
                tp_level = price * 0.8
        # For subsequent trades
        else:
            # Check if self.first_trade_price is not None before performing subtraction
            if self.first_trade_price is None:
                raise ValueError("No first trade price set yet. Cannot calculate price difference.")

            price_diff = price - self.first_trade_price
            tp_percent = self.tp_values[min(trade_count - 2, len(self.tp_values) - 1)]

            # Additional check for self.last_tp_level being not None
            if self.last_tp_level is not None:
                if trade_type == "long" and price > self.last_tp_level:
                    raise ValueError(
                        f"The given price {price} crosses the previous take profit level {self.last_tp_level}")
                elif trade_type == "short" and price < self.last_tp_level:
                    raise ValueError(
                        f"The given price {price} crosses the previous take profit level {self.last_tp_level}")

            if trade_type == "long":
                tp_level = price + abs(price_diff) * tp_percent
            elif trade_type == "short":
                tp_level = price - price_diff * tp_percent

        self.last_tp_level = tp_level
        return tp_level
