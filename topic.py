'''
1 how big is your dataset
2 what are the names of column

shape is a method to find the number of rows and column in dataset
column is find the all name of column
'''

import pandas as pd
data ={
    "Name":['Prince','Aman','Monu','Aashu','Ansh','Aditya','Tejas','Rohit'],
    "Age":[12,13,14,15,16,17,18,19],
    "Salary":[100,200,300,400,500,600,700,800],
    "Performance":[90,80,40,56,98,78,59,43]
}

df=pd.DataFrame(data)
print("Simple Data Frame")
print(df)

print("After applyong method")
print(f'Shape: {df.shape}')
print(f'Column Names: {df.columns}')