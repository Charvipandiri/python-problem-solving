Question:
 Select Specific Rows and Columns Using Pandas.Given the following DataFrame containing transaction records:

|  date	    |  name	  | amt |
|2020-01-01	|Himanshu	| 100 |
|2020-07-01 |Robert	  | 200 |
|2020-08-01	|Karie	  | 400 |
|2020-03-02	|Rohan	  | 150 |
|2020-01-03	|John	    | 300 |
Write a Pandas program to:
Extract only the rows with index 1 and 2.Select only the name and amt columns.
Code:
import pandas as pd
df = pd.DataFrame(
    [
        ['2020-01-01', 'Himanshu', 100],
        ['2020-07-01', 'Robert', 200],
        ['2020-08-01', 'Karie', 400],
        ['2020-03-02', 'Rohan', 150],
        ['2020-01-03', 'John', 300]
    ],
    columns=['date', 'name', 'amt']
)
result = df.loc[1:2, ['name', 'amt']]
print(result)
