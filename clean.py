import pandas as pd
from pandas import DataFrame
import csv
import sys

df = pd.read_csv('Search.csv')

indexNames = dfObj[ dfObj['Age'] == 30 ].index
dfObj.drop(indexNames , inplace=True)
