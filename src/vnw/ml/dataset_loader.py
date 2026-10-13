import pandas as pd
from sklearn.model_selection import train_test_split

from vnw.defines.defines import TESTSET_PATH, TRAINSET_PATH, VALSET_PATH


class TrainTestValSplitter:
    def __init__(
        self, df: pd.DataFrame, test_size: float = 0.15, val_size: float = 0.15
    ) -> None:
        self.df = df
        self.test_size = test_size
        self.val_size = val_size
        self.random_state = 42

        self.train_path = TRAINSET_PATH
        self.test_path = TESTSET_PATH
        self.val_path = VALSET_PATH

    def get_splits_save_as_parquet(self) -> None:
        (
            train_df,
            test_df,
            val_df,
        ) = self._split()
        train_df.to_parquet(self.train_path, index=False)
        test_df.to_parquet(self.test_path, index=False)
        val_df.to_parquet(self.val_path, index=False)

    def _split(self) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
        train_df, test_df = train_test_split(
            self.df, test_size=self.test_size, random_state=self.random_state
        )
        train_df, val_df = train_test_split(
            train_df,
            test_size=self.val_size / (1 - self.test_size),
            random_state=self.random_state,
        )
        return train_df, test_df, val_df
