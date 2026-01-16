'''
Describe method

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

print("Descriptive Statistics")
print(df.head())