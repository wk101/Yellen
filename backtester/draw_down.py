import pandas as pd
import numpy as np


class MaxDrawdown:
    """
    Class to calculate the maximum drawdown of a time series based on 'Return' column in the OHLC DataFrame.
    """

    def __init__(self, ohlc_data: pd.DataFrame):
        """
        Initialize the MaxDrawdown with OHLC DataFrame.

        :param ohlc_data: pandas.DataFrame containing OHLC and Return data
        """
        self.ohlc_data = ohlc_data

    def calculate(self) -> dict:
        """
        Calculate the maximum drawdown of a time series.

        :return: a dictionary contains 'max_drawdown', 'peak_date', 'trough_date'
        """
        # Use Return for drawdown calculation
        time_series = self.ohlc_data['return']

        # Running max
        cummax = np.maximum.accumulate(time_series)

        # Drawdown as a percentage
        drawdown = (cummax - time_series) / cummax

        # Max drawdown
        max_drawdown = np.max(drawdown)

        # Date at max drawdown
        peak_date = time_series[drawdown == max_drawdown].index[0]

        # Series from peak to end
        peak_to_trough = time_series[peak_date:]

        # Index at which recovery from max drawdown begins
        recovery = np.argmax(peak_to_trough - peak_to_trough.iloc[0])

        # Date of recovery
        trough_date = time_series.index[recovery]

        return {
            'max_drawdown': max_drawdown,
            'peak_date': peak_date,
            'trough_date': trough_date
        }
