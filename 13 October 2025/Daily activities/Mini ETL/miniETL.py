import pandas as pd

#1. extracting
df=pd.read_csv("students.csv")

#2. transform
df.dropna(inplace=True) #removing rows with missing values
df["Marks"] = df["Marks"].astype(int)
df["Result"] = df["Marks"].apply(lambda x: "Pass" if x>=50 else "Fail")

#3. load
df.to_csv("cleaned_students.csv",index=False)

print("Data pipeline completed. cleaned data saved to cleaned_students.csv.")
print("ETL IS DONE")