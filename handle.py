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

#df.fillna(value, inplace=True)
# avoid chained-assignment warnings by assigning back to the column
# or operate on the whole DataFrame
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Salary'] = df['Salary'].fillna(df['Salary'].mean())
print("Age and Salary:")
print(df)

# interpolate only numeric columns (axis=0 is the default) –
# axis=1 tries to treat each row as a series and fails because
# non-numeric columns are present and dtype becomes object
# the original DataFrame has no NaNs left in numeric cols anyway
num = df.select_dtypes(include='number')
num = num.interpolate(method="linear")
# put the results back if you need them:
df[num.columns] = num
print(df)

"""
1- timer series data
2- numeric data with trend
3- avoid dropping rows/columns
"""