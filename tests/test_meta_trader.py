import asyncio
import pandas as pd
import pytest
from client.meta_trader import MetaTraderClient


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
