import pandas as pd
# sample data
df = pd.DataFrame({
	'class': ['A', 'A', 'B', 'B', 'C'],
	'marks': [85, 90, 78, 82, 88]
})

print(df.groupby('class')['marks'].agg(['mean', 'sum', 'max', 'min']))