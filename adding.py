import pandas as pd
data ={
    "Name":['Prince','Aman','Aashu','Prince2'],
    "Age":[20,19,18,32],
    "City":['Bihar','Bhopal','Chhapra','Bihar'],
    "salary":[25000,15000,22000,30000]
}
df=pd.DataFrame(data)
print(df)
  
#adding new column to dataframe 
#syntax is - df['new_column_name']=values

df["Department"]=['CSE','ECE','MECH','CIVIL']
print(df)
df["Bonus"]=df["salary"]*0.10
print(df)

##Using insert()
#df.insert(location,"column_name","data")
df.insert(0,"Emoloyee_id",["E101","E102","E103","E104"])
print(df)