import pandas as pd
data ={'marks':[88,98,100,75,91,65,75,61]}
df = pd.DataFrame(data)
print(df.describe())

import matplotlib.pyplot as plt
import seaborn as sns
sns.histplot(df['marks'],kde="true")
plt.title("Marks Distrubution")
plt.show()

df2=pd.DataFrame({'Gender':["M","F","M","F","M","F","M","F",],
                'marks':[78,99,63,54,98,78,69,47]
                  })
sns.boxplot(x='Gender',y='marks',data=df2)
plt.title("Boxplot for Marks and Gender")
plt.show()

df3=pd.DataFrame({'Grade':['A','B','C','B','D','E','C','A']
                   })
sns.countplot(x='Grade',data=df3)
plt.title("Count Plot for Grade")
plt.show()
