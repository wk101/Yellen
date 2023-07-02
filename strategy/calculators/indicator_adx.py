import pandas as pd


class ADXCalculator:
    """
    Class to calculate the Average Directional Index (ADX) based on OHLC data.
    """

    def __init__(self, ohlc_data: pd.DataFrame, period: int = 14) -> None:
        """
        Initialize the ADXCalculator instance.

        Args:
            ohlc_data: DataFrame containing the OHLC data.
            period: Period for ADX calculation. Default is 14.
        """
        self.ohlc_data = ohlc_data
        self.period = period

    def calculate_adx(self) -> None:
        """
        Calculate the Average Directional Index (ADX) using the OHLC data.
        """
        self.ohlc_data['high-low'] = self.ohlc_data['high'] - self.ohlc_data['low']
        self.ohlc_data['high-prevclose'] = abs(self.ohlc_data['high'] - self.ohlc_data['close'].shift())
        self.ohlc_data['low-prevclose'] = abs(self.ohlc_data['low'] - self.ohlc_data['close'].shift())
        self.ohlc_data['tr'] = self.ohlc_data[['high-low', 'high-prevclose', 'low-prevclose']].max(axis=1)

        self.ohlc_data['upmove'] = self.ohlc_data['high'] - self.ohlc_data['high'].shift()
        self.ohlc_data['downmove'] = self.ohlc_data['low'].shift() - self.ohlc_data['low']
        self.ohlc_data['pdm'] = self.ohlc_data['upmove'].where(
            (self.ohlc_data['upmove'] > self.ohlc_data['downmove']) & (self.ohlc_data['upmove'] > 0),
            0
        )
        self.ohlc_data['ndm'] = self.ohlc_data['downmove'].where(
            (self.ohlc_data['downmove'] > self.ohlc_data['upmove']) & (self.ohlc_data['downmove'] > 0),
            0
        )

        self.ohlc_data['tr_avg'] = self.ohlc_data['tr'].rolling(window=self.period).mean()
        self.ohlc_data['pdm_avg'] = self.ohlc_data['pdm'].rolling(window=self.period).mean()
        self.ohlc_data['ndm_avg'] = self.ohlc_data['ndm'].rolling(window=self.period).mean()
        self.ohlc_data['pdi'] = (self.ohlc_data['pdm_avg'] / self.ohlc_data['tr_avg']) * 100
        self.ohlc_data['ndi'] = (self.ohlc_data['ndm_avg'] / self.ohlc_data['tr_avg']) * 100
        self.ohlc_data['dx'] = abs(self.ohlc_data['pdi'] - self.ohlc_data['ndi']) / (
                self.ohlc_data['pdi'] + self.ohlc_data['ndi']) * 100

        self.ohlc_data['adx'] = self.ohlc_data['dx'].rolling(window=self.period).mean()

    def get_adx_values(self) -> pd.DataFrame:
        """
        Get the ADX values.

        Returns:
             DataFrame: DataFrame containing the OHLC data with RSI column.

        """

        return self.ohlc_data
