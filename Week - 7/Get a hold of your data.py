Question:
Given a dataframe, a list of rows in the format of list of lists, and a number,out . Perform the following operations:
1)Append the rows from the list of lists to the dataframe
2)After appending, remove the row at the out position
code:
import pandas as pd
df = pd.DataFrame({
    "Name": ["a", "b", "c"],
    "Age": [17, 18, 19]
})

print("Original DataFrame:")
print(df)
n = int(input("Enter number of new rows: "))

rows = []
for i in range(n):
    name = input(f"Enter Name for row {i+1}: ")
    age = int(input(f"Enter Age for row {i+1}: "))
    rows.append([name, age])

out = int(input("Enter index to remove: "))
new_df = pd.DataFrame(rows, columns=df.columns)
df = pd.concat([df, new_df], ignore_index=True)
df = df.drop(out)

print("\nFinal DataFrame:")
print(df)
