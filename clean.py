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

#FEATURES 
myFeatures = "3 bds , 2 ba" #edit number of bathrooms and bedrooms
indexFeatures = df[ myFeatures is not in df['facts and features']].index
df.drop(indexFeatures , inplace=True)



