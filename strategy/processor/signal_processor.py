from strategy.calculators.signal_calculator import SignalCalculator


class SignalProcessor:
    def __init__(self):
        self.signal_calculator = SignalCalculator()
        self.trade_number = 1

    def process_signal(self, price_movement: float, adx_green: float, adx_red: float, rsi: float) -> str:
        """
        Process a signal based on the price movement, ADX green, ADX red, and RSI values.

        Args:
            price_movement: The price movement in percentage.
            adx_green: The ADX green line value.
            adx_red: The ADX red line value.
            rsi: The RSI value.

        Returns:
            str: The signal ("Long", "Short", or "No Signal").
        """
        if self.trade_number <= 30:
            signal = self.signal_calculator.generate_signal(adx_green, adx_red, rsi)
            self.trade_number += 1

            # Check for additional conditions based on trade number and price movement
            if self.trade_number <= 5 and price_movement >= 0.5:
                return signal
            elif self.trade_number <= 8 and price_movement >= 0.4:
                return signal
            elif self.trade_number <= 11 and price_movement >= 0.35:
                return signal
            elif self.trade_number <= 15 and price_movement >= 0.3:
                return signal
            elif self.trade_number <= 19 and price_movement >= 0.25:
                return signal
            elif self.trade_number <= 23 and price_movement >= 0.2:
                return signal
            elif self.trade_number <= 27 and price_movement >= 0.18:
                return signal
            elif self.trade_number <= 30 and price_movement >= 0.15:
                return signal
            else:
                return "No Signal"
        else:
            return "No Signal"
