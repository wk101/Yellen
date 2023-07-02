import pandas as pd


class RSICalculator:
    """
    Class to calculate the Relative Strength Index (RSI) based on OHLC (Open-High-Low-Close) data.
    """

    def __init__(self, ohlc_data: pd.DataFrame, period: int = 14) -> None:
        """
        Initialize the RSICalculator instance.

        Args:
            ohlc_data: DataFrame containing the OHLC data.
            period: Period for RSI calculation. Default is 14.
        """
        self.ohlc_data = ohlc_data
        self.period = period

    def calculate_rsi(self) -> None:
        """
        Calculate the RSI using the OHLC data.
        """
        price_change = self.ohlc_data['close'].diff()
        self.ohlc_data['upward_change'] = price_change.where(price_change > 0, 0)
        self.ohlc_data['downward_change'] = -price_change.where(price_change < 0, 0)

        avg_gain = self.ohlc_data['upward_change'].rolling(window=self.period).mean()
        avg_loss = self.ohlc_data['downward_change'].rolling(window=self.period).mean()

        self.ohlc_data['rs'] = avg_gain / avg_loss
        self.ohlc_data['rsi'] = 100 - (100 / (1 + self.ohlc_data['rs']))

    def get_ohlc_data(self) -> pd.DataFrame:
        """
        Get the OHLC data with added RSI column.

        Returns:
            DataFrame: DataFrame containing the OHLC data with RSI column.
        """
        return self.ohlc_data


