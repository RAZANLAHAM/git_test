import pandas as pd
# creat dataframe --> excel sheet(rows,columns)
columns= ["A", "b"]
row = [
    [1, 2],
    [2, 4],
    [5, 6]
    ]
df = pd.DataFrame(columns=columns,data=row)
print(df.head())


print("#" * 50)
# DataFrame as a list (rows and columns)
people = {
    "first" : ["razan" , "Aseel"],
    "last":["laham", "adel"] ,
    "email":["rzanlaham@","aseeladel@"]
}
df_list = pd.DataFrame(people)
print(df_list.head())
print(df_list["first"].head())
# df_list.info()
# print(df_list.descibe())
print("#" * 50)
# Access the values :
print(df_list["email"]) # access a single col
# df_list.email : another methode


