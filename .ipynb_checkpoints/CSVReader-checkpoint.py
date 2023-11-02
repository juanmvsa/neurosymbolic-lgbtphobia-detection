import csv

class CSVReader:
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with open(self.filename, 'r') as file:
            reader = csv.reader(file)
            return list(reader)