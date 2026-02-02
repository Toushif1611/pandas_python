import pandas as pd

data = {
    "Name": ["Alice","David", "Eve", "Frank", "Grace", "Hannah", "Ian", "Jack"],
    "Age": [24, None,29,35, 28, 40, 32, 29],
    "Salary": [50000, None, 55000,70000, 80000, 75000, 68000, 62000],
    "Performance Score": [85, None, 92, 87, 95, 89, 91, 88],
    "City": ["New York", "Phoenix", "Seattle", "Boston", "Miami", "Chicago", "Houston", "Dallas"]
}
df = pd.DataFrame(data)
print("Sample DataFrame:")
print(df)
'''
#df.fillna(value, inplace=True
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Salary'].fillna(df['Salary'].mean(), inplace=True)
print(df)
'''
#linear, polynamial, time
df.interpolate(method="linear", axis=1, inplace=True)
print(df)

"""
1- timer series data
2- numeric data with trend
3- avoid dropping rows/columns
"""