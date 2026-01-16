'''
info() is a method to give me a information about data 
like - no. of row and column
     - data type
     - missing data
     - column name
     - non null count
     - memory usage of data frame

'''
import pandas as pd
df=pd.read_json("products.json")
print("Displaying the info of data set")

print(df.info())
