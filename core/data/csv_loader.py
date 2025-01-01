import pandas as pd


def loader(csv_path)->pd.DataFrame:
    df = pd.read_csv(csv_path)
    return df