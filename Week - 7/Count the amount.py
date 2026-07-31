Question:
Given two dataframes customer and orders also name is given which is a customer's name.
Perform the following operation:
1)merge the dataframe such that the resultant dataframe should contain records of all 
customer ids present in customer dataframe.
2)Calculate the total order amount for given customer name Return the merged dataframe and the sum amount.
  code:
import pandas as pd
df1 = pd.DataFrame({
    'cust_id': [101, 102, 103, 104],
    'name': ['rick', 'morty', 'pickle', 'jerry']
})

df2 = pd.DataFrame({
    'order_id': ['OR1', 'OR3', 'OR23', 'OR42'],
    'cust_id': [102, 105, 101, 102],
    'amount': [1200, 650, 120, 989]
})

name = 'morty'
result = pd.merge(df1, df2, on = 'cust_id', how = 'left')
sum_amt = result[result['name'] ==name]['amount'].sum()
print(result)
print(sum_amt)
