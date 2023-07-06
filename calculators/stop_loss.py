class StopLoss:
    def __init__(self, account_drawdown: float, pair_drawdown: float):
        self.account_drawdown = account_drawdown
        self.pair_drawdown = pair_drawdown

    def adjust_level(self, position_id: int, current_stop_loss: float, new_stop_loss: float):
        """
        Adjust the stop loss level for a specific position.

        Args:
            position_id (int): The ID of the position.
            current_stop_loss (float): The current stop loss level.
            new_stop_loss (float): The new stop loss level.
        """
        try:
            # Check if the new stop loss level is lower than the current stop loss level
            if new_stop_loss < current_stop_loss:
                # Check if the new stop loss level is within the allowed account drawdown
                if new_stop_loss <= self.account_drawdown:
                    # Check if the new stop loss level is within the allowed pair drawdown
                    if new_stop_loss <= self.pair_drawdown:
                        print(f"Stop loss adjusted for position {position_id}. New level: {new_stop_loss}")
                    else:
                        raise ValueError(f"New stop loss {new_stop_loss} exceeds the allowed pair drawdown {self.pair_drawdown}")
                else:
                    raise ValueError(f"New stop loss {new_stop_loss} exceeds the allowed account drawdown {self.account_drawdown}")
            else:
                raise ValueError(f"New stop loss {new_stop_loss} is higher than the current stop loss level {current_stop_loss}")
        except ValueError as e:
            print(f"Error adjusting stop loss for position {position_id}: {str(e)}")
