
import pandas as pd
import numpy as np

from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.impute import SimpleImputer


# Transfomers
class BinaryNullTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        return X.assign(**{col: X[col].notnull() for col in self.columns})


class IntervalCategorizer(BaseEstimator, TransformerMixin):
    def __init__(self, column, rng=(2, 4)):
        self.column = column
        self.rng = rng

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        return X.assign(
            **{self.column: np.where((X[self.column] >= self.rng[0]) & (X[self.column] <= self.rng[1]), True, False)})


class Normalizer(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        self.means = X[self.columns].mean()
        self.std = X[self.columns].std()

        return self

    def transform(self, X):
        return X.assign(**{col: (X[col] - self.means[col]) / self.std[col] for col in self.columns})


class FeatureSelector(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        return X[self.columns]


# New transformer to just do simple imput on each column
class DataframeImputer(SimpleImputer):
    def transform(self, X):
        return pd.DataFrame(super().transform(X), columns=X.columns)