Question:
Given a dataframe df having the income details for different individuals
Return a Dataframe that contains the gender-wise average income.
Code:
import pandas as pd
data = {
    'name': ['Elon', 'Jeff', 'Bill', 'Falguni'],
    'gender': ['M', 'F', 'M', 'F'],
    'income': [53000.0, 28000.0, 25000.0, 44000.0]
}
df = pd.DataFrame(data)
result = df.groupby('gender')[['income']].mean()
print(result)
