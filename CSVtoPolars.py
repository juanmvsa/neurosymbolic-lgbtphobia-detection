import csv
import polars as pl

class CSVtoPolars:
    def __init__(self, filename1, filename2, filename3, filename4):
        self.filename1 = filename1
        self.filename2 = filename2
        self.filename3 = filename3
        self.filename4 = filename4

    def convert(self):
        data = {}
        for i, filename in enumerate([self.filename1, self.filename2, self.filename3, self.filename4], start=1):
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                data[f'column{i}'] = list(reader)[0]  # Get the list at position 0
        df = pl.DataFrame(data)  # Convert dict to DataFrame
        return df