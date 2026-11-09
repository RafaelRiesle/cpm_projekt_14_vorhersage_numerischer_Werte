import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor, export_text, plot_tree


class LinearRegressionTree:
    def __init__(
        self,
        max_depth=None,
        min_samples_split=2,
        min_samples_leaf=1,
        max_leaf_nodes=None,
        min_impurity_decrease=0.0,
        ccp_alpha=0.0,
    ):

        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.min_samples_leaf = min_samples_leaf
        self.max_leaf_nodes = max_leaf_nodes
        self.min_impurity_decrease = min_impurity_decrease
        self.ccp_alpha = ccp_alpha

    def _get_tree_parameters(self):

        return {
            "max_depth": (None if self.max_depth is None else int(self.max_depth)),
            "min_samples_split": int(self.min_samples_split),
            "min_samples_leaf": int(self.min_samples_leaf),
            "max_leaf_nodes": (
                None if self.max_leaf_nodes is None else int(self.max_leaf_nodes)
            ),
            "min_impurity_decrease": float(self.min_impurity_decrease),
            "ccp_alpha": float(self.ccp_alpha),
            "random_state": 42,
        }

    def fit(self, X, y):

        if isinstance(X, pd.DataFrame):
            self.feature_names_ = list(X.columns)
            X_array = X.to_numpy()
        else:
            X_array = np.asarray(X)
            self.feature_names_ = [f"x{i}" for i in range(X_array.shape[1])]

        y_array = np.asarray(y).ravel()

        self._X_fit_ = X_array.copy()
        self._y_fit_ = y_array.copy()

        self.tree_model_ = DecisionTreeRegressor(**self._get_tree_parameters())

        self.tree_model_.fit(X_array, y_array)

        # Blätter identifizieren
        leaf_ids = self.tree_model_.apply(X_array)

        self.leaf_models_ = {}

        # Für jedes Blatt ein lineares Regressionsmodell trainieren
        for leaf_id in np.unique(leaf_ids):
            mask = leaf_ids == leaf_id

            X_leaf = X_array[mask]
            y_leaf = y_array[mask]

            linear_model = LinearRegression()
            linear_model.fit(X_leaf, y_leaf)

            self.leaf_models_[leaf_id] = linear_model

        return self

    def predict(self, X):

        if isinstance(X, pd.DataFrame):
            X_array = X.to_numpy()
        else:
            X_array = np.asarray(X)

        leaf_ids = self.tree_model_.apply(X_array)

        predictions = np.zeros(len(X_array))

        for leaf_id in np.unique(leaf_ids):
            mask = leaf_ids == leaf_id

            linear_model = self.leaf_models_[leaf_id]

            predictions[mask] = linear_model.predict(X_array[mask])

        return predictions

    def get_coefficients(self):

        rows = []

        for leaf_id, model in self.leaf_models_.items():
            row = {"Leaf": leaf_id, "Intercept": model.intercept_}

            for feature, coefficient in zip(
                self.feature_names_, model.coef_, strict=False
            ):
                row[feature] = coefficient

            rows.append(row)

        return pd.DataFrame(rows)

    def get_leaf_models(self):

        leaf_ids = self.tree_model_.apply(self._X_fit_)

        rows = []

        for leaf_id, model in self.leaf_models_.items():
            mask = leaf_ids == leaf_id

            rows.append(
                {
                    "Leaf": leaf_id,
                    "Samples": int(mask.sum()),
                    "Intercept": model.intercept_,
                    "Coefficients": model.coef_,
                }
            )

        return pd.DataFrame(rows)

    def get_tree_structure(self):

        return export_text(self.tree_model_, feature_names=self.feature_names_)

    def get_tree_info(self):

        tree = self.tree_model_.tree_

        return {
            "Number of nodes": tree.node_count,
            "Number of leaves": tree.n_leaves,
            "Maximum depth": self.tree_model_.get_depth(),
        }

    def get_pruning_path(self, X, y):

        if isinstance(X, pd.DataFrame):
            X_array = X.to_numpy()
        else:
            X_array = np.asarray(X)

        y_array = np.asarray(y).ravel()

        base_tree = DecisionTreeRegressor(
            max_depth=(None if self.max_depth is None else int(self.max_depth)),
            min_samples_split=int(self.min_samples_split),
            min_samples_leaf=int(self.min_samples_leaf),
            max_leaf_nodes=(
                None if self.max_leaf_nodes is None else int(self.max_leaf_nodes)
            ),
            min_impurity_decrease=float(self.min_impurity_decrease),
            random_state=42,
        )

        base_tree.fit(X_array, y_array)

        return base_tree.cost_complexity_pruning_path(X_array, y_array)

    def plot_tree_structure(self, figsize=(20, 10)):

        plt.figure(figsize=figsize)

        plot_tree(
            self.tree_model_,
            feature_names=self.feature_names_,
            filled=True,
            rounded=True,
            impurity=True,
            proportion=False,
        )

        plt.title("Linear Regression Tree")
        plt.show()
