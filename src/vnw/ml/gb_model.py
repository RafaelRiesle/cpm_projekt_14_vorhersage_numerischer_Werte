from sklearn.ensemble import GradientBoostingRegressor

from vnw.ml.base_model import BaseRegressionModel


class GradientBoostingModel(BaseRegressionModel):
    def __init__(self):
        super().__init__(
            GradientBoostingRegressor(random_state=42),
            {
                "n_estimators": [100, 200],
                "learning_rate": [0.03, 0.1],
                "max_depth": [3, 5, 10, None],
                "min_samples_leaf": [2, 5],
                "subsample": [0.8, 1.0],
            },
        )
