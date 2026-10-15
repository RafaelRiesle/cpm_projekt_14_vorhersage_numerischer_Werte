from sklearn.tree import DecisionTreeRegressor

from vnw.ml.base_model import BaseRegressionModel


class DecisionTreeModel(BaseRegressionModel):
    def __init__(self):
        super().__init__(
            DecisionTreeRegressor(random_state=42),
            {
                "max_depth": [3, 5, 10, None],
                "min_samples_leaf": [2, 5, 10],
                "ccp_alpha": [0.0, 0.001, 0.01],
            },
        )
