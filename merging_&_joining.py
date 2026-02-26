#pd.merge(df1, df2, on="COlumn_Name", how="type_of_join")
import pandas as pd

#customer dataframe
df_customers = pd.DataFrame({
    'CustomerID':[1,2,3],
    'Name':['Ramesh', 'Suresh', 'Kalpesh']
})

#order dataframe
df_orders = pd.DataFrame({
    'CustomerID':[1,2,4],
    'OrderAmount':[250, 450, 350]
})

#merge
df_merged = pd.merge(df_customers, df_orders, on='CustomerID', how='cross')
print("Cross Join:")
print(df_merged)

"""
#cross join
1df = m rows
2df =n rows
m*n rows
"""

#concatination
"""
vertically (row-wise) 
horizontally (column-wise)

pd.concate([df1, dff2], axis=0/1, ignore_index=True/False)

[df1, df2]= list of dataframes
axis=0 (row-wise)
axis=1 (column-wise)
ignore_index=True/False

"""
#region1
df_Region1 = pd.DataFrame({
    'CustomerID':[1,2],
    'Name':['Gopal','Rju']
})

#region2
df_Region2 = pd.DataFrame({
    'CustomerID':[3,4],
    'Name':['Mohan','Sohan']
})

#vertical concatination
df_concat = pd.concat([df_Region1, df_Region2], axis=0, ignore_index=True)
print("Vertical Concatenation:")
print(df_concat)

#horizontal concatination
df_concat_horiz = pd.concat([df_Region1, df_Region2], axis=1)
print("Horizontal Concatenation:")
print(df_concat_horiz)