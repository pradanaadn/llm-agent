import pandas as pd
from core.data.metadata_extractor import extract_metadata

df =pd.read_csv('HRDataset_v14.csv')

print(extract_metadata(df))