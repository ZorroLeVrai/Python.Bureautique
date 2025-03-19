import pandas as pd

df_page1 = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], columns=['a', 'b', 'c'])
print("DataFrame 1")
print(df_page1)

df_page2 = pd.DataFrame([[11, 12, 13], [14, 15, 16], [17, 18, 19]], columns=['a', 'b', 'c'])
print("DataFrame 2")
print(df_page2)

# Copie de la cellule (1,1) de df_page2 dans df_page1
df_page1.iloc[1,1] = df_page2.iloc[1,1]

print("DataFrame 1 après copie")
print(df_page1)
