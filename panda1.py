import pandas as pd

data = {
    "name": ["Alice", "Bob", "Charlie", "David"],
    "age": [24, 30, 22, 35],
    "city": ["New York", "Los Angeles", "Chicago", "Houston"]

}

df = pd.DataFrame(data)
print(df)

#df.to_csv("people.csv", index=False)

#df.to_excel("people.xlsx", index=False)
#df.to_json("people.json", orient="records")

"""
1- understand the data set
2- identify the problems
3- plan next steps
"""

#head(n) first 5 rows by default
# tail(n) last 5 rows by default
df = pd.read_csv("people.csv")
print(df.head())
print(df.tail())


"""
1- column, rows
2- what type of data
3- missing values

info() method

1- number of rows and columns
2- column names
3- int64, float64, object (string)
4- not null counts
5- memory usage of the DataFrame
"""

df = pd.read_csv("people.csv")
print("displaying info")
print(df.info())


data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hannah"],
    "Age": [24, 30, 22, 35, 28, 40, 32, 29],
    "Salary": [50000, 60000, 55000, 70000, 65000, 80000, 75000, 68000],
    "Performance Score": [85, 90, 88, 92, 87, 95, 89, 91],
    "City": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Seattle", "Boston", "Miami"]
}


df = pd.DataFrame(data)
print("Sample DataFrame:")
print(df)

print("Descriptive statistics:")
print(df.describe())

"""
1- how big id your data set
2- what are the names of columns

shape and columns attributes
"""

df = pd.DataFrame(data)
print(df)
print(f'shape : {df.shape}')
print(f'columns : {df.columns}')


"""
1- select specific columns
2- filter rows based on conditions
3- combine multiple conditions

1- square brackets []
2- boolean condition

selection columns
1- a series
2- dataframe multiple columns of data

column = df["column_name"]
subset = df[["col1", "col2", ...]]

filtering rows
1- boolean indexing

#based on a single condition
filtered_df = df[df["column_name"] > value]

#combining multiple conditions
filtered_df = df[(df["col1"] > value1) & (df["col2"] < value2)]
"""

df = pd.DataFrame(data)
print("Sample DataFrame:")
print(df)   
name = df["Name"]
print("Selected 'Name' column:")
print(name)

#selecting multiple columns
subset = df[["Name", "Salary", "Age"]]
print("Selected 'Name', 'Salary' and 'Age' columns:")
print(subset)


df = pd.DataFrame(data)
print("Sample DataFrame:")
print(df)
#filtering rows based on a single condition
high_salary = df[df["Salary"] > 60000]
print("Employees with Salary greater than 60000:")
print(high_salary)

#combining multiple conditions
filltered = df[(df["Salary"] > 60000) & (df['Salary'] < 80000)]
print("Employees with Salary between 60000 and 80000:")
print(filltered)

# using | for OR condition
filtered_or = df[(df["Age"] > 25) | (df["Performance Score"] > 90)]
print("Employees with Age greater than 25 or Performance Score greater than 90:")
print(filtered_or)