import numpy as np
import pandas as pd


class SharpeRatioCalculator:
    def __init__(self, ohlcv_data: pd.DataFrame) -> None:
        """
        Initialize the SharpeRatioCalculator.

        Args:
            ohlcv_data (pd.DataFrame): DataFrame with OHLCV data including a 'Returns' column.
        """
        self.ohlcv_data = ohlcv_data

    def calculate_sharpe_ratio(self, risk_free_rate: float) -> pd.DataFrame:
        """
        Calculate the Sharpe Ratio and return the DataFrame with 'Sharpe Ratio' column.

        Args:
            risk_free_rate (float): Risk-free rate for calculating excess returns.

        Returns:
            pd.DataFrame: DataFrame with 'Sharpe Ratio' column.
        """
        returns = self.get_returns_data()
        excess_returns = returns - risk_free_rate
        mean_excess_return = np.mean(excess_returns)
        std_excess_return = np.std(excess_returns)
        sharpe_ratio = mean_excess_return / std_excess_return

        self.ohlcv_data['Sharpe Ratio'] = sharpe_ratio
        return self.ohlcv_data

    def get_returns_data(self) -> pd.Series:
        """
        Get the 'Returns' data from the OHLCV data.

        Returns:
            pd.Series: Series of 'Returns' data.
        """
        return self.ohlcv_data['Returns']

    def get_ohlc_data(self) -> pd.DataFrame:
        """
        Get the 'Returns' data from the OHLCV data.

        Returns:
            pd.Series: Series of 'Returns' data.
        """
        return self.ohlcv_data

