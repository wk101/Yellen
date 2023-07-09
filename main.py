# region imports
from AlgorithmImports import *
from QuantConnect.DataSource import *
from typing import List
from processor.position_processor import PositionProcessor
from calculators.stop_loss import StopLoss
from calculators.take_profit import TakeProfit
from QuantConnect import Position


# endregion

class Yellen(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2022, 1, 4)  # Set Start Date
        self.SetCash(100000)  # Set Strategy Cash
        self.symbol = self.AddForex("EURUSD", Resolution.Minute, Market.Oanda).Symbol
        self.SetBenchmark(self.symbol)

        # Add RSI indicator
        self.rsi = self.RSI(self.symbol, 9, Resolution.Minute)

        # Initialize ADX values
        self.green_adx_value = 30.0  # Manually set the green ADX value
        self.red_adx_value = 20.0  # Manually set the red ADX value

        # Initialize StopLoss and TakeProfit calculators
        account_drawdown = 0.0  # Initialize account drawdown
        pair_drawdown = 0.0  # Initialize pair drawdown

        # Initialize PositionProcessor
        self.position_processor = PositionProcessor(stop_loss, take_profit)

    def OnData(self, slice: Slice):
        if self.symbol in slice.Bars:
            bar = slice.Bars[self.symbol]
            self.Log(
                f"{self.symbol} at {bar.Time}: Close: {bar.Close}, Open: {bar.Open}, High: {bar.High}, Low: {bar.Low}")

            # Calculate price movement percentage from the last bar
            previous_bar = self.History(self.symbol, 2, Resolution.Minute)[-2]
            price_movement = (bar.Close - previous_bar.Close) / previous_bar.Close * 100.0

            # Update RSI with current bar
            self.rsi.Update(bar.EndTime, bar.Close)

            # Retrieve RSI value
            rsi_value = self.rsi.Current.Value
            self.Log(f"RSI: {rsi_value:.2f}")

            # Retrieve open positions
            open_positions = self.Portfolio.GetOpenPositions()

            # Calculate trade count dynamically
            trade_count = self.CalculateTradeCount(open_positions)

            # Calculate drawdown dynamically
            account_drawdown = self.CalculateAccountDrawdown()
            pair_drawdown = self.CalculatePairDrawdown(open_positions)

            # Update StopLoss with new drawdown values
            self.position_processor.stop_loss.account_drawdown = account_drawdown
            self.position_processor.stop_loss.pair_drawdown = pair_drawdown

            # Adjust stop loss and take profit levels for open positions
            self.position_processor.adjust_open_positions(open_positions, trade_count)

    def CalculateAccountDrawdown(self) -> float:
        total_portfolio_value = self.Portfolio.TotalPortfolioValue
        unrealized_profit = self.Portfolio.UnrealizedProfit
        account_drawdown = unrealized_profit / total_portfolio_value
        return account_drawdown

    def CalculatePairDrawdown(self, open_positions: List[Position]) -> float:
        # Calculate pair drawdown dynamically based on custom logic
        pair_drawdown = 0.0  # Initialize pair drawdown with 0.0

        if open_positions:
            max_drawdown = max(position.ProfitLossPercentage for position in open_positions)
            pair_drawdown = max(max_drawdown, 0.0)  # Ensure pair drawdown is not negative

        return pair_drawdown

    def CalculateTradeCount(self, open_positions: List[Position]) -> int:
        trade_count = sum(position.TradeCount for position in open_positions)
        return trade_count
