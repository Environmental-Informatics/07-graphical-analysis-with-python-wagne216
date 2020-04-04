#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 17:08:51 2020
10 minute tut (several hours: )
https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html

import data: 
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_table.html
@author: wagne216
"""

# modules:
import numpy as np
import pandas as pd

# create objects
# series- numbers a set in an array
s = pd.Series([1, 3, 5, np.nan, 6, 8])

# dataframe - numpy aray + datetime idx + #'d col's
dates = pd.date_range('20130101', periods=6) # datetime array
df = pd.DataFrame(np.random.randn(6, 4), index=dates,\
                  columns=list('ABCD')) # labels col's, creates shaped data
# another dataframe - dictionary of objects -> series-like - note input style
df2 = pd.DataFrame({'A': 1.,\
                    'B': pd.Timestamp('20130102'),\
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),\
                    'D': np.array([3] * 4, dtype='int32'),\
                    'E': pd.Categorical(["test", "train", "test", "train"]),\
                    'F': 'foo'})
print('df2 datatypes:')
print(df2.dtypes)

# viewing data
print() # empty line
print('view top rows:')
print(df.head())
print()
print('view bottom 3 rows:')
print(df.tail(3))
print()
print('view index,cols:')
print(df.index)
print(df.columns)

# convert pandas datas to numpy types
# note- this searches for a waythat all datatypes can be handled thus everything
# may become objects
#df.np.to_numpy() #doesn't work?
print()
print('describe:')
print(df.describe()) #- quick stats! mean, quartiles...
print()
print('transpose:')
print(df.T)
print()
print('sort by axis:')
print(df.sort_index(axis=0, ascending=False)) # 0-x; 1- y
print()
print('sort by B')
print(df.sort_values(by='B'))

#%%
# selecting datas:
# with labels
print()
print("show col A: via df['A'] or df.A")
print(df['A'])

print()
print("slices rows with []")
print(df[0:3])
print('or')
print(df['20130102':'20130104'])

print()
print("slect by label df.loc[xlabel,ylabel]")
print(df.loc[dates[0]])

print()
print("select multiple axes with label")
print(df.loc[:, ['A', 'B']])

print()
print("can also us .at to get scalar")
print(df.at[dates[0], 'A'])
# with positions
print()
print("iloc")
print(df.iloc[3])

print()
print("lists of positiosn")
print(df.iloc[[1, 2, 4], [0, 2]])

print()
print("slice rows")
print(df.iloc[1:3, :])

print()
print("slice cols")
print(df.iloc[:, 1:3])

#%% boolean
print()
print("find data when vals in B larger than 0")
print(df[df['B'] > 0])
print()
print("vals when all vals >0")
print(df[df > 0])
print()
print("filter with isin")
df2 = df.copy()
df2['E'] = ['one', 'one', 'two', 'three', 'four', 'three']
print(df2)
print(df2[df2['E'].isin(['two', 'four'])])

# %% setting? - can set vals by label, positin, array #
print()
print("")
s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range('20131005', periods=6))
print(s1)

# missing datas
print("re-index at specified axis")
df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ['E'])
print(df1)
print("drop rows with missing data")
drop =df1.dropna(how='any')
print(drop)
print()
print("fill rows with missing data")
fill =df1.fillna(value=50)
print(fill)
# %% basic operations pretty standard- see tut on how to apply them to certain axes
# if need alignment: 
s = pd.Series([1, 3, 5, np.nan, 6, 8], index=dates).shift(2)
sub = df.sub(s, axis='index')
print(s)
print(sub)








