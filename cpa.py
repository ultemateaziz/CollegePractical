import pandas as pd
df = pd.read_excel('study.xlsl')
df
df.dropna(axis=0, inplace=True)
df
df.fillna(0)
df