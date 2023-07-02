class SignalCalculator:
    """
    Class to calculate trading signals based on the ADX and RSI indicators.
    """

    @staticmethod
    def generate_signal(adx_green: float, adx_red: float, rsi: float, rsi_threshold: float = 30) -> str:
        """
        Generate a trading signal based on the ADX green, ADX red, and RSI values.

        Args:
            adx_green: The ADX green line value.
            adx_red: The ADX red line value.
            rsi: The RSI value.
            rsi_threshold: The threshold value for RSI to generate a signal. Default is 30.

        Returns:
            str: The generated signal ("Long", "Short", or "No Signal").
        """
        if adx_green > adx_red and rsi < rsi_threshold:
            return "Long"
        elif adx_red > adx_green and rsi > 100 - rsi_threshold:
            return "Short"
        else:
            return "No Signal"
