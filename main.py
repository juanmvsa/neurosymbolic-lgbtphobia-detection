from createPath import *
from CreatePytorchDataset import *
from Visualization import *
from CreateEmbeddings import *
from CreatePolarsDataframe import *
from Labels import *
from TranslateText import *

# from AMR import *

import torch
import sys
from googletrans import Translator


if __name__ == "__main__":
    print(sys.version)

    # object that creates a Path object with the route to the csv file that contains the training csv file.
    cvs_importer = CSVImporter(path_object_training_csv)

    # object that creates a polars dataframe from the csv file.
    polars_dataframe_es = cvs_importer.get_dataframe()

    # object that gets the (encoded) labels in original the polars dataframe.
    labels = Labels(polars_dataframe_es, ["label"])

    # object that translates the text in the polars Dataframe.
    translator = TranslateText("es", "en", polars_dataframe_es, "content")

    # uncomment to translate your text.
    # this new Dataframe contains the translated text.
    polars_dataframe_en = translator.translate_text()

    # uncomment to save your translated text in a csv.
    polars_dataframe_en.write_csv("translated_csv.csv")

    # variable that stores the encoded labels in a list.
    encoded_labels = labels.fit_transform()

    # object that creates the embeddings from the polars dataframe.
    embeddings_object = CreateEmbeddings(polars_dataframe_en, path_object_embeddings)

    # list with the feature embeddings that will be used for training.
    embeddings = embeddings_object.get_embeddings()

    # this variable stores the Pytorch dataset with the embeddings and the labels.
    dataset = CreatePytorchDataset(embeddings, encoded_labels)

    # the dataloader is used to iterate over the dataset.
    dataloader = torch.utils.data.DataLoader(dataset, batch_size=32, shuffle=True)

    # instantiate the AMRParser.
    # amr = AMRParser("AMR3-structbart-L")

    # amr_parser = amr.createAMR(t)
    # print(amr_parser)

    for batch in dataloader:
        embeddings, labels = batch
        print(embeddings, labels)

    # print(f"Number of features: {dataset.num_features}")
    # print(f"Number of classes: {labels.fit_transform()}")

    visualization = Visualization()