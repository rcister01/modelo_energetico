from sklearn.preprocessing import StandardScaler , RobustScaler, MinMaxScaler
from sklearn.base import TransformerMixin, BaseEstimator


class MultiScaler(TransformerMixin, BaseEstimator):
    def __init__(self, scaler = RobustScaler()):
        self.scaler = scaler

    def fit(self, X, y=0):
        self.scaler.fit(X)
        return self

    def transform(self, X, y = 0):
        return self.scaler.transform(X)
