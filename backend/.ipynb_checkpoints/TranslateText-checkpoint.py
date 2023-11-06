from googletrans import Translator
import polars as pl
import time


class TranslateText:
    def __init__(
        self, source_lang: str, target_lang: str, df: pl.DataFrame, column: str
    ):
        self.source_lang = source_lang
        self.target_lang = target_lang
        self.df = df
        self.column = column

    def translate_text(self) -> pl.DataFrame:
        translator = Translator()
        translated_text = []
        cont = 0

        for row in self.df[self.column][0:100]:
            cont = cont + 1

            if cont < 1000:
                t = translator.translate(row, dest=self.target_lang)
                translated_text.append(t.text)

            else:
                time.sleep(3600)
                t = translator.translate(row, dest=self.target_lang)
                translated_text.append(t.text)
                cont = 0

        # create a new Series with the translated text.
        translated_column = pl.Series("content", translated_text)

        # this Dataframe contains the translated text.
        df = pl.DataFrame()
        df = df.with_columns(translated_column)

        return df