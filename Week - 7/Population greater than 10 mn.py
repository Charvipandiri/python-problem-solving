Question:
Given a dataset containing information about different countries, including their Country Name, 
Population, Year, and Continent, create a Pandas DataFrame and perform the following operations:
Filter the DataFrame to include only the countries with a population greater than 10 million.
Sort the filtered DataFrame in ascending order, first by the Year column and then by the Population column.
Return the resulting DataFrame.
code:
import pandas as pd
data = [
    ["India", 1400000000, 2023, "Asia"],
    ["Nepal", 30000000, 2022, "Asia"],
    ["Bhutan", 800000, 2023, "Asia"],
    ["Australia", 26000000, 2022, "Australia"],
    ["Canada", 39000000, 2023, "North America"]
]

df = pd.DataFrame(data, columns=["Country", "Population", "Year", "Continent"])
df = df[df["Population"] > 10000000]
df = df.sort_values(by=["Year", "Population"], ascending=True)
print(df)
