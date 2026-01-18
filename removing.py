import pandas as pd
data ={
    "Name":['Prince','Aman','Aashu','Prince2'],
    "Age":[20,19,18,32],
    "City":['Bihar','Bhopal','Chhapra','Bihar'],
    "salary":[25000,15000,22000,30000]
}

df=pd.DataFrame(data)
print(df)

print("After Removing")

##df.drop(column=["column_name"],inplace=True)

#df.drop(columns=["Age"],inplace=True)
#print(df)

#multiple Row remove
df.drop(columns=["Age","salary"],inplace=True)
print(df)