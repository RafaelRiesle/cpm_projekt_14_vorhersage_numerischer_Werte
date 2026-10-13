from sklearn.ensemble import RandomForestRegressor

from vnw.ml.base_model import BaseRegressionModel


class RandomForestModel(BaseRegressionModel):
    def __init__(self):
        super().__init__(
            RandomForestRegressor(
                random_state=42,
                n_jobs=1,
            ),
            {
                "n_estimators": [100, 300],
                "max_depth": [3, 5, 10, None],
                "min_samples_leaf": [2, 5, 10],
                "max_features": [0.7, 1.0],
            },
        )
