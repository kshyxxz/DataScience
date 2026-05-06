import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# sample skewed data
df = pd.DataFrame({
    'income': [1000, 2000, 3000, 10000, 50000]
})



# check skewness
print(df['income'].skew())

# log transformation
df['income_log'] = np.log(df['income'])

print(df)
df['income'].hist()
plt.title("Before Transformation")
plt.show()

df['income_log'].hist()
plt.title("After Log Transformation")
plt.show()