import pandas as pd
df = pd.read_csv("diabetes.csv")
print(df.shape) # shape is a method not a fun whithout ()
print(df.head())
print(df["Age"].describe())
df.info()
print("#" * 50)
df_1 = df[["Pregnancies", "Age" , "Outcome"]]
print(df_1.head())
print("#" * 50)
df_1["new_age"] = df_1["Age"] *2
print(df_1.head())
print("#" * 50)

# to print one cell in the data we use iloc fun
print(df.iloc[1, 1]) # 2nd row and 2nd column
df.iloc[2, 4] = -1
df.iloc[3, 1]= None
df.iloc[4, 1] = None
df.info
print(df["Age"].head())
print("#" * 50)
df2 = pd.DataFrame(df)
df2.dropna()
print(df2.head())
