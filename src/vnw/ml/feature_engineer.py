import pandas as pd
from sklearn.preprocessing import OneHotEncoder


class FeatureEngineer:
    def __init__(self, categorical_features):
        self.categorical_features = categorical_features

        self.encoder = OneHotEncoder(handle_unknown="ignore", sparse_output=False)

        self.feature_names = None

    def fit_transform(self, X):
        encoded = self.encoder.fit_transform(X[self.categorical_features])

        self.feature_names = self.encoder.get_feature_names_out(
            self.categorical_features
        )

        return pd.DataFrame(encoded, columns=self.feature_names, index=X.index)

    def transform(self, X):
        encoded = self.encoder.transform(X[self.categorical_features])

        return pd.DataFrame(encoded, columns=self.feature_names, index=X.index)
