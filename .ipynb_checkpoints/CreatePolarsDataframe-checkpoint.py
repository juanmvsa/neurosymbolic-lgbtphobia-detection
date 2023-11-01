import polars as pl


class CSVImporter:
    def __init__(self, path_to_csv):
        self.df = pl.read_csv(path_to_csv)

    def get_dataframe(self):
        # this line replaces all the NaN values with 0.
        columns = self.df.columns
        
        for column in columns:
            if column == "label":
                self.df = self.df.with_columns(pl.col("label").fill_null("NR"))
        
        return self.df