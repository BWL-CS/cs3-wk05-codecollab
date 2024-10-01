import pandas as pd

# WARNING: Lots of print statements here!!! Sorry!
# Be careful to connect the code section to the correct output!
# Divider to help organize terminal output
DIV = "〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️"

# PART A: Series & DataFrames
print("***** PART A *****")

dict = {'Kamala': 59,
        'Tim': 60,
        'Donald': 78,
        'JustDance Vance':40}
series = pd.Series(dict)
df1 = pd.DataFrame(series, columns=['age'])

print(df1)
print(DIV)

print(df1.describe()) 
print(DIV)

# PART B: Compare df2 to df1?
print("***** PART B *****")

area = pd.Series({'California': 423967, 'Texas': 695662,
                  'Florida': 170312, 'New York': 141297,
                  'Pennsylvania': 119280})
pop = pd.Series({'California': 39538223, 'Texas': 29145505,
                 'Florida': 21538187, 'New York': 20201249,
                 'Pennsylvania': 13002700})
df2 = pd.DataFrame({'area':area, 'pop':pop})

print(df2) 
print(DIV)

print(df2.describe()) 
print(DIV)

# PART C: DataFrame from CSV file
print("***** PART C *****")

titanic = pd.read_csv("titanic.csv")

print(titanic)
print(DIV)

print(titanic.info())
print(DIV)

print(titanic.columns) 
print(DIV)

# PART D: Manipulating Text Content
print("***** PART D *****")

print(titanic['Name'].str.lower())
print(DIV)

print(titanic['Name'].str.split(","))
print(DIV)

print(titanic[titanic['Name'].str.contains("Countess")])
