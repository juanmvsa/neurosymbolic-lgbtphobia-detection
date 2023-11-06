from pathlib import Path

path_training_csv: str = (
    "/001/usuarios/juanmvs/2023/iberlef2023/friday14/track1_training"
    ".csv"
)
path_embeddings: str = (
    "/001/usuarios/juanmvs/2023/amr/sunday22_october_2023/glove.twitter.27B.100d.txt"
)

path_object_training_csv: Path = Path(path_training_csv)
path_object_embeddings: Path = Path(path_embeddings)