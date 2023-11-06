from createPath import *
from CreatePolarsDataframe import *
from Labels import *
from TranslateText import *
from AMR import *
import csv

# this program calls the csv with the training csv, translates it into english and saves the translated text into a new csv.
# it also parses the translated data using the AMR parser and saves the resulting tokens, nodes, edges and roots into four csvs.
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
    
    # instantiate the AMRParser.
    amr = AMR("AMR3-structbart-L")
    
    tokens, nodes, edges, roots = amr.createAMR(polars_dataframe_en['content'])
    
    csv_amr_writer = CSVWriterAMRParsing(tokens, nodes, edges, roots)
    
    parse_amr_to_dataframe = CSVtoPolars("tokens.csv", "nodes.csv", "edges.csv", "roots.csv")
    
    parse_amr_to_dataframe.write_csv("parsed_corpus.csv")