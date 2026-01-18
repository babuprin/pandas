import pandas as pd
data ={
    "Name":['Prince','Aman','Aashu','Prince2'],
    "Age":[20,19,18,32],
    "City":['Bihar','Bhopal','Chhapra','Bihar'],
    "salary":[25000,15000,22000,30000]
}
df=pd.DataFrame(data)
print(df)

## .loc[]
#df.loc[row_index,"column_name"]=new_value

df.loc[0,"Age"]=55
print(df)