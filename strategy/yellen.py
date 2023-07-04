from typing import List
from strategy.calculators.indicator_rsi import RSICalculator
from strategy.calculators.indicator_adx import ADXCalculator
from strategy.calculators.signal_calculator import SignalCalculator
from strategy.calculators.stop_loss import StopLoss
from strategy.calculators.take_profit import TakeProfit
from strategy.processor.signal_processor import SignalProcessor
from strategy.processor.position_processor import PositionProcessor
from strategy.processor.order_processor import ProcessOrder

from client.meta_trader import MetaTraderClient


class YellenStrategy:
    def __init__(self) -> None:
        pass

    def calculate_indicators(self) -> None:
        """
        Calculate the necessary indicators for the strategy.
        """
        # Retrieve OHLC data from MetaTrader client
        ohlc: List[float] = MetaTraderClient.get_ohlc()

        # Calculate ADX
        self.adx.calculate(ohlc)

        # Calculate RSI
        self.rsi_red.calculate(ohlc)
        self.rsi_green.calculate(ohlc)

    def calculate_signals(self) -> None:
        """
        Calculate trading signals based on the indicators.
        """
        self.signal_calculator.calculate_signals(
            self.adx.green_line, self.adx.red_line,
            self.rsi_green.value, self.rsi_red.value
        )

    def process_signals(self) -> None:
        """
        Process the trading signals.
        """
        if not self.signal_calculator.signals:
            return

        self.position_processor.process_positions(self.signal_calculator.signals)
        self.position_processor.process_order(self.signal_calculator.signals, self.stop_loss)

    def on_new_bar(self) -> None:
        """
        Perform necessary actions when a new bar is formed.
        """
        self.calculate_indicators()
        self.calculate_signals()
        self.process_signals()

    def setup(self) -> None:
        """
        Perform initial setup, adjusting take profit and stop loss for open positions.
        """

        MetaTraderClient.get_ohlcv()
        self.rsi_red = RSICalculator(period=7)
        self.rsi_green = RSICalculator(period=14)
        self.adx = ADXCalculator()
        self.signal_calculator = SignalCalculator()
        self.signal_calculator = SignalProcessor()
        self.position_processor = PositionProcessor()
        self.stop_loss: StopLoss = StopLoss()
        self.take_profit: TakeProfit = TakeProfit()

        self.position_processor.adjust_open_positions(self.take_profit, self.stop_loss)

    def run_strategy(self) -> None:
        """
        Run the Yellen strategy.
        """
        # Perform initial setup
        self.calculate_indicators()
        self.calculate_signals()
        self.process_signals()
        self.setup()

        # Start monitoring for new bars
        while True:
            # Wait for a new bar formation
            MetaTraderClient.wait_for_new_bar()

            # Perform actions on new bar
            self.on_new_bar()


class ProcessOrder:
    def __init__(self, trading_client: TradingClient):
        self.trading_client = trading_client
        self.signal_processor = SignalProcess()
        self.stop_loss = StopLoss()
        self.take_profit = TakeProfit()

    def execute_trades(self, adx_green: float, adx_red: float, rsi: float):
        """
        Execute trades based on the ADX green, ADX red, and RSI values.

        Args:
            adx_green (float): The ADX green line value.
            adx_red (float): The ADX red line value.
            rsi (float): The RSI value.
        """
        processed_signal = self.signal_processor.process_indicator(adx_green, adx_red, rsi)
        if processed_signal == "Long":
            sl_level = self.stop_loss.calculate_sl("long")
            tp_level = self.take_profit.calculate_tp(1, self.trading_client.get_current_price(), "long")
            self.trading_client.create_long_trade(sl_level, tp_level)
        elif processed_signal == "Short":
            sl_level = self.stop_loss.calculate_sl("short")
            tp_level = self.take_profit.calculate_tp(1, self.trading_client.get_current_price(), "short")
            self.trading_client.create_short_trade(sl_level, tp_level)
        else:
            self.trading_client.close_all_trades()

    def execute_trades_batch(self, adx_green_list: List[float], adx_red_list: List[float], rsi_list: List[float]):
        """
        Execute trades in batch based on lists of ADX green, ADX red, and RSI values.

        Args:
            adx_green_list (List[float]): The list of ADX green line values.
            adx_red_list (List[float]): The list of ADX red line values.
            rsi_list (List[float]): The list of RSI values.
        """
        for adx_green, adx_red, rsi in zip(adx_green_list, adx_red_list, rsi_list):
            self.execute_trades(adx_green, adx_red, rsi)


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



@pytest.fixture
def sample_ohlcv_data():
    return pd.DataFrame({'Returns': [0.01, -0.02, 0.03, 0.01, -0.02]})


def test_sharpe_ratio_calculator(sample_ohlcv_data):
    # Create sample OHLCV data
    ohlcv_data = sample_ohlcv_data
    risk_free_rate = 0.02

    # Create an instance of SharpeRatioCalculator
    sharpe_calculator = SharpeRatioCalculator(ohlcv_data)

    # Calculate Sharpe Ratio
    result = sharpe_calculator.calculate_sharpe_ratio(risk_free_rate)

    # Check if the 'Sharpe Ratio' column is added to the DataFrame
    assert 'Sharpe Ratio' in result.columns

    # Check if the calculated Sharpe Ratio value is correct
    expected_sharpe_ratio = (np.mean(ohlcv_data['Returns']) - risk_free_rate) / np.std(ohlcv_data['Returns'])
    assert result['Sharpe Ratio'].iloc[-1] == expected_sharpe_ratio


@pytest.mark.asyncio
async def test_metatrader_client():
    symbol = "EURUSD"
    timeframe = MetaTraderClient.TIMEFRAME_M5
    start_time = pd.Timestamp("2022-01-01")
    end_time = pd.Timestamp("2022-01-02")
    access_token = "YOUR_TEST_NET_ACCESS_TOKEN"  # Replace with your access token for the test net
    secret_key = "YOUR_TEST_NET_SECRET_KEY"  # Replace with your secret key for the test net

    # Set the access token and secret key for the MetaTrader client
    MetaTraderClient.set_credentials(access_token, secret_key)

    # Test create_order
    assert await MetaTraderClient.create_order(symbol, "buy", 0.1)

    # Test close_position
    assert await MetaTraderClient.close_position(12345)

    # Test get_positions
    positions = await MetaTraderClient.get_positions()
    assert isinstance(positions, list)

    # Test get_ohlcv
    df = await MetaTraderClient.get_ohlcv(symbol, timeframe, start_time, end_time)
    assert isinstance(df, pd.DataFrame)
    assert len(df) > 0


# Run the test
asyncio.get_event_loop().run_until_complete(test_metatrader_client())



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


