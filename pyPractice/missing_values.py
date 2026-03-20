import pandas as pd
import numpy as np

# sample data
df = pd.DataFrame({
    'age': [20, 25, np.nan, 30, np.nan],
    'salary': [20000, 25000, 30000, np.nan, 40000]
})

# check missing values
# print(df.isnull().sum())

# 1. Drop missing values
df_drop = df.dropna()
print(df_drop)

# # 2. Fill with mean
# df['age'] = df['age'].fillna(df['age'].mean())

# # 3. Fill with median
# df['salary'] = df['salary'].fillna(df['salary'].median())

# print(df)