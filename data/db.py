import sqlite3
import pandas as pd

class OHLCVDataLoader:

    def __init__(self, db_path: str):
        self.db_path = db_path
        self.connection = None

    def __enter__(self) -> 'OHLCVDataLoader':
        self.connection = sqlite3.connect(self.db_path)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection is not None:
            self.connection.close()

    def create_ohlcv_table(self) -> None:
        """
        Create the OHLCV data table in the database if it doesn't exist.
        """
        create_table_query = '''
            CREATE TABLE IF NOT EXISTS ohlcv_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp DATETIME,
                symbol TEXT,
                open REAL,
                high REAL,
                low REAL,
                close REAL,
                volume REAL
            )
        '''

        # Execute the table creation query
        with self.connection:
            self.connection.execute(create_table_query)

    def get_ohlcv_data(self, symbol: str) -> pd.DataFrame:
        """
        Retrieve OHLCV data for a specific symbol from the database.
        Returns a pandas DataFrame containing the data.
        """
        query = f"SELECT * FROM ohlcv_data WHERE symbol = '{symbol}'"

        # Execute the query and fetch the results into a DataFrame
        with self.connection:
            df = pd.read_sql_query(query, self.connection)

        return df
