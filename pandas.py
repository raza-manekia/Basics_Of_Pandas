# -*- coding: utf-8 -*-
"""Pandas.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EXr5ObZusFb4_AKbhQuC9IjyrQPXPX8k

#INTRODUCTION AND SOME USEFUL COMMANDS OF PANDAS
"""

import pandas as pd

data = pd.read_csv('/content/sample_data/california_housing_test.csv')
data

"""Print starting and ending Values using **.head(n)** and **.tail(n)**"""

data.head(2)

data.tail(2)

"""Basic Info using **.info** and **.shape**"""

data.info()

data.shape

"""Working On **Columns**"""

data.columns

data.rename(columns={'longitude':'length','latitude':'width', 'housing_median_age':'median', 'total_rooms':'Total'})

"""Statistical Analysis (**sum,mean,describe**)"""

data.sum()

"""**.sum(n)** where *n=0,1* 
n = 0: Coloumn wise sum
n = 1: Row wise sum


"""

data.sum(0)

data.mean()

data.describe()

"""locating your desired Item (**.loc(item)**)"""

data.loc[5]