from calculators.stop_loss import StopLoss
from calculators.take_profit import TakeProfit
from typing import List


class PositionProcessor:
    def __init__(self, stop_loss: StopLoss, take_profit: TakeProfit):
        self.stop_loss = stop_loss
        self.take_profit = take_profit

    def adjust_stop_loss(self, position_id: int, new_stop_loss: float):
        """
        Adjust the stop loss level for an open position.

        Args:
            position_id (int): The ID of the position.
            new_stop_loss (float): The new stop loss level.
        """
        try:
            self.stop_loss.adjust_level(position_id, new_stop_loss)
            print(f"Stop loss adjusted for position {position_id}. New level: {new_stop_loss}")
        except ValueError as e:
            print(f"Error adjusting stop loss for position {position_id}: {str(e)}")

    def adjust_take_profit(self, position_id: int, new_take_profit: float):
        """
        Adjust the take profit level for an open position.

        Args:
            position_id (int): The ID of the position.
            new_take_profit (float): The new take profit level.
        """
        try:
            self.take_profit.adjust_level(position_id, new_take_profit)
            print(f"Take profit adjusted for position {position_id}. New level: {new_take_profit}")
        except ValueError as e:
            print(f"Error adjusting take profit for position {position_id}: {str(e)}")

    def adjust_open_positions(self, open_positions: List[Position]):
        """
        Adjust the stop loss and take profit levels for all open positions.

        Args:
            open_positions (List[Position]): A list of open positions.
        """
        for position in open_positions:
            position_id = position.id
            current_take_profit = position.take_profit

            try:
                new_take_profit = self.take_profit.calculate_tp(position.trade_count, position.price, position.trade_type)
                if new_take_profit != current_take_profit:
                    self.adjust_take_profit(position_id, new_take_profit)
            except ValueError as e:
                print(f"Error calculating take profit for position {position_id}: {str(e)}")
