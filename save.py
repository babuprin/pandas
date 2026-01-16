import pandas as pd

data ={
    "Name":['Prince','Aman','Aashu'],
    "Age":[20,19,18],
    "City":['Bihar','Bhopal','Chhapra']
}
df=pd.DataFrame(data)
print(df)

#df.to_csv("output.csv",index=False)
#df.to_json("output.json",index=False)
