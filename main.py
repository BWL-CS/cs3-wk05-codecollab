from numpy import divide
import pandas as pd

# PART A
dict = {'Braund, Mr. Owen Harris': 22,
        'Allen, Mr. William Henry': 35,
        "Bonnell, Miss. Elizabeth": 58}
series = pd.Series(dict)
dataframe = pd.DataFrame(series, columns=['age'])

# Divider to help organize terminal output
DIV = "〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️"

print(df)
print(DIV)

print(df.describe())
print(DIV)

print(df['age'])
print(DIV)

# PART B
titanic = pd.read_csv("titanic.csv")

print(titanic)
print(DIV)

print(titanic.info())
print(DIV)

# PART C
above_35 = titanic[titanic["Age"] > 35]

print(above_35.shape)
print(DIV)

adult_names = titanic.loc[titanic["Age"] > 35, "Name"]

print(adult_names.head())
print(DIV)

# PART D
print(titanic["Name"].str.lower())
print(DIV)

print(titanic["Name"].str.split(","))
print(DIV)

print(titanic[titanic["Name"].str.contains("Countess")])
