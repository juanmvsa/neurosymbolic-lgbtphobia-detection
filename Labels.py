import polars as pl
from sklearn.preprocessing import LabelEncoder


class Labels:
    def __init__(self, df, column_name):
        self.df = df
        self.column_name = column_name
        self.encoded_labels = []

        # self.encoders = {}

    # TODO: fix this method.
    def fit_transform(self):
        encoder = LabelEncoder()
        encoded_column_name = f"{self.column_name}_encoded"
        encoded_labels = encoder.fit_transform(self.df[self.column_name])
        # return encoded_column
        self.df = self.df.with_columns([(encoded_column_name, self.encoded_labels)])

        return encoded_labels

    def transform(self):
        # encoder = self.encoders[column_name]
        encoded_column_name = f"{self.column_name}_encoded"
        encoded_column = self.encoder.transform(self.df[self.column_name]).ravel()
        # self.df.with_columns([(encoded_column_name, encoded_column)])