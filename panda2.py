import pandas as pd

#adding columns
data = {
    "Name": ["Alice","Charlie", "David", "Eve", "Frank", "Grace", "Hannah", "Ian"],
    "Age": [24, None,29,35, 28, 40, 32, 29],
    "Salary": [50000, None, 55000,70000, 80000, 75000, 68000, 62000],
    "Performance Score": [85, None, 92, 87, 95, 89, 91, 88],
    "City": ["New York", None, "Phoenix", "Seattle", "Boston", "Miami", "Chicago", "Houston"]
}
df = pd.DataFrame(data)
print("Sample DataFrame:")
print(df)

"""
#square brackets [] df["new_column"] = values
df["Bonus"] = df["Salary"] * 0.1
print("DataFrame after adding Bonus column:")
print(df)

#using insert() method
# df.insert(loc, "column_name", values)
df.insert(0, "Employee ID", [10,20,30,40,50,60,70,80])
print(df)

# .loc[] 
# df.loc[row_index, "column_name"] = new_value
df.loc[0, 'Salary'] = 55000
print(df)

"""

#increasing salary by 5%
df['Salary'] = df['Salary'] * 1.05
print(df)


# df.drop(columns=["column_name1", "column_name2", ...], inplace=True)
print("Modified data:")
df.drop(columns=["City"], inplace=True)
print(df)


"""
NaN (not a number)
None (for object data type)

isnull()
True - NaN is missing
False - value is present
"""

print("Checking for missing values:")
print(df.isnull().sum())

"""
# dropna() method
"""

df.dropna(inplace=True)
print(df)


"""
#fillna() method
#fillna(value, inplace= True/False)
"""

df.fillna(0, inplace=True)
print(df)