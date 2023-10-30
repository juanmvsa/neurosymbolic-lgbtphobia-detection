import polars as pl


class CSVImporter:
    def __init__(self, path_to_csv):
        self.df = pl.read_csv(path_to_csv)

    def get_dataframe(self):
        return self.df