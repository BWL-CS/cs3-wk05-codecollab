from numpy import divide
import pandas as pd

# PART A
df = pd.DataFrame({
    "Name": [
        "Braund, Mr. Owen Harris",
        "Allen, Mr. William Henry",
        "Bonnell, Miss. Elizabeth",
    ],
    "Age": [22, 35, 58],
    "Sex": ["male", "male", "female"],
})

# Divider to help organize terminal output
DIV = "〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️"

print(df)
print(DIV)

print(df.describe())
print(DIV)

print(df["Age"])
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
