Question:
Given a dataframe consisting of income details,Return the name of person having the highest income.
code:
import pandas as pd
data = {
    'name': ['Elon', 'Jeff', 'Bill', 'Falguni'],
    'gender': ['M', 'F', 'M', 'F'],
    'income': [53000, 28000, 25000, 44000]
}
df = pd.DataFrame(data)
result = df.iloc[df['income'].idxmax()]['name']
print(result)
