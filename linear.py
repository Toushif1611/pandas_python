import pandas as pd

data = {
    "Time":[1, 2, 3, 4, 5, 6, 7, 8],
    "Value":[10, None, 30, None, 50, 60, None, 80]
}

df = pd.DataFrame(data)
print('before interpolation:')
print(df)

df['Value'] = df['Value'].interpolate(method='linear')
print('after interpolation:')
print(df)

"""
1- timer series data
2- numeric data with trends
3- avoid droping rows
"""