import polars as pl
import numpy as np
import torch


class CreateEmbeddings:
    def __init__(self, df, path_to_embeddings):
        self.df = df
        self.embeddings = {}
        with open(
            path_to_embeddings, "r", encoding="utf-8", newline="\n", errors="ignore"
        ) as f:
            for line in f:
                values = line.rstrip().split(" ")
                word = values[0]
                vector = np.asarray(values[1:], dtype="float32")
                self.embeddings[word] = vector

    def get_embeddings(self):
        final_embeddings = []

        for row in self.df["content"]:
            text = row
            words = text.split()
            embedding = np.zeros(len(self.embeddings[next(iter(self.embeddings))]))

            count = 0

            for word in words:
                if word in self.embeddings:
                    embedding = embedding + self.embeddings[word]
                    count += 1

                else:
                    embedding = np.zeros(100)

                if count != 0:
                    embedding /= count
            final_embeddings.append(embedding)

        return final_embeddings