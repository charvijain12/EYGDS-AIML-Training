import pandas as pd
import numpy as np
data={
    "Name":["Rahul","Priya","Arjun","Neha","Vikram"],
    "Age":[21,22,20,23,21],
    "Course" : ["AI","ML","Data Science","AI","ML"],
    "Marks":[85,90,78,88,95]
}
df=pd.DataFrame(data)
print(df)
print("\n")

# selecting data
print(df["Name"],"\n") #single column
print(df[["Name","Marks"]]) #multiple column
print("\n",df.iloc[0],"\n") #first row - row navigation
print(df.loc[2,"Marks"]) #value at row 2, column navigation
print("\n")

#data filter
high_scores = df[df["Marks"]>85] #students with marks > 85 will be returned
print("Scores above 85 are:")
print(high_scores,"\n")

#adding pass/fail column
df["Result"] = np.where(df["Marks"]>=80, "Pass","Fail")
#updating neha's marks
df.loc[df["Name"]=="Neha","Marks"] = 92
print(df)