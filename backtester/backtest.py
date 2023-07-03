import random
from typing import List, Tuple
from strategy.position import Position
from strategy.yellen_strategy import YellenStrategy
from strategy.sharpe_ratio_calculator import SharpeRatioCalculator
from strategy.drawdown_calculator import DrawdownCalculator

class Backtester:
    def __init__(self, strategy: YellenStrategy):
        self.strategy = strategy
        self.positions = []
        self.trades = []
        self.pnl = 0.0
        self.sharpe_ratio = 0.0
        self.drawdown = 0.0
        self.winning_trades = 0
        self.total_trades = 0

    def update_positions(self):
        """
        Update the positions based on the strategy's open positions.
        """
        self.positions = self.strategy.get_open_positions()

    def calculate_profit_loss(self):
        """
        Calculate the profit/loss for each position based on price movement.
        """
        for position in self.positions:
            # Get the current price from the position
            current_price = position.get_current_price()

            # Generate random slippage
            slippage = random.uniform(-0.005, 0.005)

            # Calculate the entry price with slippage
            entry_price = position.entry_price + slippage

            # Calculate the price movement
            price_movement = current_price - entry_price

            # Calculate the profit/loss based on price movement
            position.calculate_profit_loss(price_movement)
            self.pnl += position.pnl

            # Track winning trades
            if position.pnl > 0:
                self.winning_trades += 1

            # Track total trades
            self.total_trades += 1

            # Append trade details to trades list
            trade_details = {
                'entry_price': entry_price,
                'exit_price': current_price,
                'profit_loss': position.pnl
            }
            self.trades.append(trade_details)

    def calculate_sharpe_ratio(self):
        """
        Calculate the Sharpe ratio based on the profit/loss of the positions.
        """
        pnl_values = [position.pnl for position in self.positions]

        sharpe_calculator = SharpeRatioCalculator(pnl_values)
        self.sharpe_ratio = sharpe_calculator.calculate_sharpe_ratio()

    def calculate_drawdown(self):
        """
        Calculate the maximum drawdown based on the profit/loss of the positions.
        """
        pnl_values = [position.pnl for position in self.positions]

        drawdown_calculator = DrawdownCalculator(pnl_values)
        self.drawdown = drawdown_calculator.calculate_drawdown()

    def execute_trades(self):
        """
        Execute trades based on the strategy's trading signals.
        """
        self.strategy.execute_trades()

    def run_backtest(self):
        """
        Run the backtest by updating positions, calculating profit/loss, executing trades,
        calculating the Sharpe ratio and drawdown, and returning the backtest results.
        """
        self.update_positions()
        self.calculate_profit_loss()
        self.execute_trades()
        self.calculate_sharpe_ratio()
        self.calculate_drawdown()

        backtest_results = {
            'trades': self.trades,
            'pnl': self.pnl,
            'sharpe_ratio': self.sharpe_ratio,
            'drawdown': self.drawdown,
            'winning_trades': self.winning_trades,
            'total_trades': self.total_trades
        }

        return backtest_results
