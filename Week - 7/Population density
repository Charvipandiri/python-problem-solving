Question:
Given a dataframe containing area and population data, calculate the Population Density for each state.
The function should return a Series of population densities sorted in ascending order.
Code:
import pandas as pd
data = {
    'country': ['India', 'USA', 'China', 'Australia'],
    'population': [1400000000, 333000000, 1412000000, 26000000],
    'area': [3287263, 9833517, 9596961, 7692024]
}

df = pd.DataFrame(data)
pop_den = df['population'] / df['area']
result = pop_den.sort_values()
print(result)
