import seaborn as sns
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 5]

# regression + scatter
sns.regplot(x=x, y=y)

plt.title("Regression Plot")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()