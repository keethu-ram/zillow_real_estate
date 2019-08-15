import pandas as pd
from pandas import DataFrame
import csv
import sys

df = pd.read_csv('Search.csv')

#PRICE
maxPrice = 0 #set maximum price
indexPrice = df[ df['price'] >= maxPrice ].index
df.drop(indexPrice , inplace=True)

#LOCATION (comment out if not required)
myCity = "Ithaca" #set city
indexCity = df[ df['city'] != myCity ].index
df.drop(indexCity , inplace=True)



