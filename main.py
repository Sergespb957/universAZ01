import pandas as pd

df = pd.read_csv('mobile_sales.csv')

print(df.head())

print(df.info())

print(df.describe())

df2 = pd.read_csv('dz.csv')
group = df2.groupby('City')['Salary'].mean()

print(group)
