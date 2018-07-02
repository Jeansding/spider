import pandas as pd
dd=pd.read_csv('movies.csv')
dd.to_csv('movies1.csv')
print(dd)