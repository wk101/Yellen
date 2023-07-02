import random
import numpy as np
import pandas as pd
from decimal import Decimal
from datetime import datetime, timedelta


class CombinedDataGenerator:
    @staticmethod
    def generate_combined_data(start_timestamp, end_timestamp, time_bar):
        # Generate OHLC data with the specified time bar frequency
        ohlcv_data = CombinedDataGenerator.generate_dummy_fx_ohlcv(start_timestamp, end_timestamp, freq=time_bar)

        # Generate trade and position data
        trade_data = CombinedDataGenerator.generate_trade_data(ohlcv_data)
        position_data = CombinedDataGenerator.generate_position_data(trade_data)

        # Generate tp and sl values
        tp_values = generate_tp_values(len(ohlcv_data))
        sl_values = generate_sl_values(len(ohlcv_data))
        rt_values = generate_rt_values(len(ohlcv_data))

        # Merge OHLC, trade, and position data into a single DataFrame
        combined_data = pd.merge(ohlcv_data, trade_data, on='timestamp', how='left')
        combined_data = pd.merge(combined_data, position_data, on='timestamp', how='left')
        combined_data['tp'] = tp_values
        combined_data['sl'] = sl_values
        combined_data['return'] = rt_values

        return combined_data

    @staticmethod
    def generate_dummy_fx_ohlcv(start_timestamp, end_timestamp, freq):
        # Generate dummy OHLCV data with random values
        timestamps = pd.date_range(start=start_timestamp, end=end_timestamp, freq=freq)
        num_bars = len(timestamps)

        open_prices = np.random.uniform(low=1.0, high=1.2, size=num_bars)
        high_prices = np.random.uniform(low=1.2, high=1.4, size=num_bars)
        low_prices = np.random.uniform(low=0.8, high=1.0, size=num_bars)
        close_prices = np.random.uniform(low=1.0, high=1.2, size=num_bars)
        volumes = np.random.randint(low=1000, high=5000, size=num_bars)

        ohlcv_data = pd.DataFrame({
            'timestamp': timestamps,
            'open': open_prices,
            'high': high_prices,
            'low': low_prices,
            'close': close_prices,
            'volume': volumes
        })

        return ohlcv_data

    @staticmethod
    def generate_trade_data(ohlcv_data):
        # Generate dummy trade data based on OHLCV data
        timestamps = ohlcv_data['timestamp']
        trade_ids = np.arange(1, len(timestamps) + 1)
        trade_types = np.random.choice(['market', 'limit'], size=len(timestamps))

        trade_data = pd.DataFrame({
            'timestamp': timestamps,
            'trade_id': trade_ids,
            'trade_type': trade_types
        })

        return trade_data

    @staticmethod
    def generate_position_data(trade_data):
        # Generate dummy position data based on trade data
        timestamps = trade_data['timestamp']
        position_ids = np.arange(1, len(timestamps) + 1)
        position_types = np.random.choice(['long', 'short'], size=len(timestamps))
        position_amounts = np.random.uniform(low=100000, high=200000, size=len(timestamps))
        trade_quantities = np.random.randint(low=1, high=5, size=len(timestamps))
        position_amount_open = position_amounts.copy()

        position_data = pd.DataFrame({
            'timestamp': timestamps,
            'position_id': position_ids,
            'position_type': position_types,
            'position_amount': position_amounts,
            'trade_quantity': trade_quantities,
            'position_amount_open': position_amount_open
        })

        return position_data


def generate_tp_values(num_bars):
    # Generate random tp values between 0.95 and 1.05
    tp_values = np.random.uniform(low=0.95, high=1.05, size=num_bars)
    return tp_values


def generate_sl_values(num_bars):
    # Generate random sl values between 0.9 and 0.95
    sl_values = np.random.uniform(low=0.9, high=0.95, size=num_bars)
    return sl_values


def generate_rt_values(num_bars):
    sl_values = np.random.uniform(low=-0.001, high=0.001, size=num_bars)
    return sl_values
