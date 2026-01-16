#head(),tail()

import pandas as pd
df=pd.read_json("products.json")

print('Display 10 rows of first')
print(df.head())

print('Display 10 rows of lasr')
print(df.tail())
