import pandas as pd

#DataFrame
df = pd.DataFrame(
    {"a" : [4, 5, 6],
     "b" : [7, 8, 9],
     "c" : [10, 11, 12]},
    index = [1, 2, 3])

print(df)
print(df["a"])
print(df[["a"]])
print()
'''result
  a  b   c
1  4  7  10
2  5  8  11
3  6  9  12
1    4
2    5
3    6
Name: a, dtype: int64
   a
1  4
2  5
3  6
'''

#Subset (일부 값만 불러오기)

print(df[["a", "b"]])
print()
'''result
 a  b
1  4  7
2  5  8
3  6  9
'''

#Reshaping

print(df["a"].sort_values())
print(df.sort_values("a"))
print(df.sort_values("a", ascending=False))

df = df.drop(["c"], axis=1)
print(df)
print()
'''result
1    4
2    5
3    6
Name: a, dtype: int64
   a  b   c
1  4  7  10
2  5  8  11
3  6  9  12
   a  b   c
3  6  9  12
2  5  8  11
1  4  7  10
   a  b
1  4  7
2  5  8
3  6  9
'''

#Group Data

print(df.groupby(["a"])["b"].mean())
print(pd.pivot_table(df, index="a"))
'''result
a
4    7
5    8
6    9
Name: b, dtype: int64
   b
a   
4  7
5  8
6  9
'''

#Plotting

df.plot()
df.plot.bar()
df.plot.density()