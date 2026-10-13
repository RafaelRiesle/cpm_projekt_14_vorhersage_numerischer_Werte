from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score,
)
from sklearn.model_selection import GridSearchCV


class BaseRegressionModel:
    def __init__(self, estimator, param_grid):
        self.estimator = estimator
        self.param_grid = param_grid
        self.search = None
        self.best_model = None

    def fit(self, X_train, y_train):
        self.search = GridSearchCV(
            estimator=self.estimator,
            param_grid=self.param_grid,
            cv=5,
            scoring="neg_mean_absolute_error",
            n_jobs=-1,
            refit=True,
        )

        self.search.fit(X_train, y_train)
        self.best_model = self.search.best_estimator_

        print("Beste Parameter:", self.search.best_params_)
        print("Beste CV-MAE:", -self.search.best_score_)

        return self

    def predict(self, X):
        return self.best_model.predict(X)

    def evaluate(self, X, y):
        pred = self.predict(X)

        return {
            "MAE": mean_absolute_error(y, pred),
            "RMSE": mean_squared_error(y, pred) ** 0.5,
            "R2": r2_score(y, pred),
        }
