from numpy import divide
import pandas as pd

# WARNING: Lots of print statements here!!! Sorry!
# Be careful to connect the code section to the correct output!
# Divider to help organize terminal output
DIV = "〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️"

# PART A: Series & DataFrames
dict = {'Braund, Mr. Owen Harris': 22,
        'Allen, Mr. William Henry': 35,
        "Bonnell, Miss. Elizabeth": 58}
series = pd.Series(dict)
dataframe = pd.DataFrame(series, columns=['age'])

print(dataframe) # how many dimensions is this DF?
print(DIV)

print(dataframe.describe()) 
print(DIV)

# PART B: DataFrame from a CSV file
titanic = pd.read_csv("titanic.csv")

print(titanic) # how does this DF differ from Part A?
print(DIV)

print(titanic.info())
print(DIV)

print(titanic.columns) 
print(DIV)

# PART C: Filtering
above_35 = titanic[titanic['Age'] > 35]

print(above_35.shape)
print(DIV)

adult_names = titanic.loc[titanic['Age'] > 35, 'Name']

print(adult_names.head())
print(DIV)

# PART D: Manipulating Text Content
print(titanic['Name'].str.lower())
print(DIV)

print(titanic['Name'].str.split(","))
print(DIV)

print(titanic[titanic['Name'].str.contains("Countess")])
