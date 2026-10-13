import pandas as pd

from vnw.defines.defines import QUERY_DATA_FILE


class LoadPrepareData:
    def __init__(self, query_data_file: str = QUERY_DATA_FILE) -> None:
        self.query_data_file = query_data_file

    def load_and_prepare_data(self) -> pd.DataFrame:
        df = self._load_parquet_file()
        df = self._prepare_data(df)
        return df

    def _load_parquet_file(self) -> pd.DataFrame:
        # Load data from Parquet file
        df = pd.read_parquet(self.query_data_file)
        return df

    def _prepare_data(self, df: pd.DataFrame) -> pd.DataFrame:
        df["ProductLine"] = df["ProductLine"].str.strip()
        # Extract Year, Month, and Week from 'OrderDate'
        df["Year"] = df["OrderDate"].dt.year
        df["Month"] = df["OrderDate"].dt.month
        df["Week"] = df["OrderDate"].dt.isocalendar().week
        df["YearWeek"] = (
            df["Year"].astype(str) + "-" + df["Week"].astype(str).str.zfill(2)
        )
        return df
