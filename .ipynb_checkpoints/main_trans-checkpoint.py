from createPath import *
from CreatePolarsDataframe import *
from Labels import *
from TranslateText import *


if __name__ == "__main__":

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
    polars_dataframe_en.write_csv("translated.csv")

    # variable that stores the encoded labels in a list.
    encoded_labels = labels.fit_transform()
    
    # DataFrame that storres the encoded labels.
    df_labels = pl.DataFrame(encoded_labels)
    
    # save the encoded labels in a csv.
    df_labels.write_csv("labels.csv")