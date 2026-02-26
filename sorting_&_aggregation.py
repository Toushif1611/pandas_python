#sorting data
#SORTING DATA IN 1 COLUMN sort_values()
# df.sort_values(by="column_name", ascending=True/False, inplace=True)
# df.sort_values(by=["Age", "Salary"], ascending=[True, False], inplace=True)

import pandas as pd

data ={
    "Name":['Arun', 'Varun', 'Karun','Narun','Maru'],
    "Age":[28,34,22,34,28],
    "Salary":[50000,60000,45000,52000,40000]
}

df = pd.DataFrame(data)
print(df)

df.sort_values(by="Age", ascending=True, inplace=True)
print("Sorting age by Descending order")
print(df)


df.sort_values(by=["Age", "Salary"], ascending=[True, False], inplace=True)
print("Age and Salary")
print(df)


"""
df["column Name"].sum()
df["column Name"].min()
df["column Name"].max()
df["column Name"].mean()
"""

avg_salary = df['Salary'].mean()
print("Average Salary:", avg_salary)


grouped = df.groupby("Age")["Salary"].sum()
print(grouped)

"""df.groupby("Age")
age = 22 > [45000]
age = 28 [50000, 40000]
age = 34 [60000, 52000]

["Salary"].sum()
age = 22 > 45000
age = 28 [50000 + 40000 = 90000]
age = 34 [60000 + 52000 = 112000]"""

grouped = df.groupby(["Age","Name"])["Salary"].sum()
print(grouped)

"""1- sum()
2- mean()
3- count()
4- min()
5- max()
6- std()
7- var()
8- median()
9- agg()""" #custom aggregation


