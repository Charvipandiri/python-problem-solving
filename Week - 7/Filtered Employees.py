Question:
Given a dictionary containing employee details, create a Pandas DataFrame. Filter the rows where the gender is 'male' 
and display only the profession, gender, and age columns.
code:
import pandas as pd
data = {
    'name': ["Sam", "Roma", "Mark"],
    'profession': ['dev', 'mle', 'Data scientist'],
    'gender': ['male', 'female', 'male'],
    'age': [21, 20, 25],
    'review': ['No comments', 'hardworker', 'need improvement'],
    'rating': [10, 5, 7]
}
df = pd.DataFrame(data)
result = df.loc[df['gender'] == 'male', ['profession', 'gender', 'age']]

print(result)
