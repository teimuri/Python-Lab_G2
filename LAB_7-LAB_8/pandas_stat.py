#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 31 13:45:15 2021

@author: hamimehrabi
"""


import numpy as np
import pandas as pd

indexes = [1, 2, 3, 4, 5, 6]

df = pd.DataFrame(np.random.randint(0,100,size=(6, 4)), columns=list('ABCD'), index=indexes)
print("***1***")
print(df)

print("***2***")
new_df = df.tail(2)
new_df = new_df.append(df.head(2))
print(new_df)

print("***3***")
print(df.values)
print(df.columns) 
print(df.index) 
print(df.describe)

print("***4***")
df = df.sort_values(by=['B', 'C'], ascending=[True, False])
print(df)


print("***5***")
d = {1:1, 2:2, 3:3, 4:4, 5:5, 6:6}
S = pd.Series(data=d, index=indexes)
df['F'] = S
print(df)


print("***6***")
df.iat[2, 4] = np.nan
print(df)
print(df.iloc[[0, 1, 2], [0, 4]])


print("***7***")
df1 = df.dropna()
print(df1)


print("***8***")
df2 = df.fillna(np.mean(df['F']))
print(df2)