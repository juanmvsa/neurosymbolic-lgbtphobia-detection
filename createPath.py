from pathlib import Path

path_training_csv: str = (
    "/Users/juanvasquez/Library/Mobile Documents/com~apple~CloudDocs/nlp/iberlef2023/track1_training"
    ".csv"
)
path_embeddings: str = (
    "/Users/juanvasquez/Library/Mobile "
    "Documents/com~apple~CloudDocs/nlp/neurosym_lgbtqphobia_detection/glove.twitter.27B.100d.txt"
)

path_object_training_csv: Path = Path(path_training_csv)
path_object_embeddings: Path = Path(path_embeddings)