import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df=sns.load_dataset("titanic")
print(df.describe(include="all"))
print(df.head())

sns.boxplot(y='age',x='sex',data=df)
plt.title("age and sex")
plt.show()

sns.countplot(x='pclass',data=df)
plt.title("passanger class disbrution")
plt.show()

sns.countplot(x='survived',data=df)
plt.title("Passanger Survived")
plt.show()

num_cols=df[['age','fare','pclass']].dropna()

cov_matrix=num_cols.cov()

cor_matrix=num_cols.corr()
print("Covariance:\n", cov_matrix)
print("\nCorrelation:\n", cor_matrix)

sns.heatmap(cor_matrix,annot=True,cmap='coolwarm')
plt.title("Correlation Matrix")
plt.show()

import seaborn as sns
sns.pairplot(data=df)
plt.show()
