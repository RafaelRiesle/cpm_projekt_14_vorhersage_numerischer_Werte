from pathlib import Path

import pandas as pd


class SetLoader:
    def __init__(
        self, trainset_path: Path, testset_path: Path, valset_path: Path
    ) -> None:
        self.trainset_path = trainset_path
        self.testset_path = testset_path
        self.valset_path = valset_path

    def load_sets(self) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
        trainset = pd.read_parquet(self.trainset_path)
        testset = pd.read_parquet(self.testset_path)
        valset = pd.read_parquet(self.valset_path)

        print("Trainset:", trainset.shape)
        print("Testset:", testset.shape)
        print("Valset:", valset.shape)
        return trainset, testset, valset
