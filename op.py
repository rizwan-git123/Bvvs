import pandas as pd

df=pd.read_csv("../average.csv")
print(df.head())
print(df.info())
print(df.describe())
