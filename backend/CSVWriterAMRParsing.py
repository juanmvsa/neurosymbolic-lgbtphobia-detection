import csv

class CSVWriterAMRParsing:
    def __init__(self, tokens, nodes, edges, roots):
        self.tokens = tokens
        self.nodes = nodes
        self.edges = edges
        self.roots = roots

    def write(self):
        with open('tokens.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(self.tokens)

        with open('nodes.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(self.nodes)

        with open('edges.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(self.edges)

        with open('roots.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(self.roots)