import pandas as pd
import matplotlib.pyplot as plt

# data = {'value':[1, 2, 3, 3, 3, 4, 4, 4, 5, 6, 7, 8, 9, 10, 55]}
# df = pd.DataFrame(data)
#
# df.boxplot(column='value')
# plt.show()
#
# Q1 = df['value'].quantile(0.25)
# Q3 = df['value'].quantile(0.75)
# IQR = Q3 - Q1
#
# downside = Q1 - 1.5 * IQR
# upside = Q3 + 1.5 * IQR
#
# df_new = df[(df['value'] >= downside) & (df['value'] <= upside)]
#
# df_new.boxplot(column='value')
# plt.show()

data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'gender': ['female', 'male', 'male', 'male', 'female'],
    'department': ['HR', 'Engineering', 'Marketing', 'Engineering', 'HR']
}

df = pd.DataFrame(data)
df['gender'] = df['gender'].astype('category')
df['department'] = df['department'].astype('category')

df['department'] = df['department'].cat.add_categories(['Finance'])
print(df['department'].cat.categories)

df['department'] = df['department'].cat.remove_categories(['HR'])
print(df['department'].cat.categories)

print(df)