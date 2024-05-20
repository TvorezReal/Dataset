import pandas as pd

# df = pd.read_csv("heart_statlog_cleveland_hungary_final.csv")
#
# print(df.head(5))
# print(df.info())
# print(df.describe())

df = pd.read_csv("dz.csv")
print(df.info())
df.dropna(inplace=True)
print(df.head(5))
group = df.groupby('City')['Salary'].mean()
print(group)


