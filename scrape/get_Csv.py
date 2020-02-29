from urllib.request import urlopen
import pandas as pd
import numpy as np
from io import StringIO
import csv

if __name__ == "__main__":
  csvPage = urlopen('http://www.pythonscraping.com/files/MontyPythonAlbums.csv').read().decode('utf-8', 'ignore')
  dataFile = StringIO(csvPage)
  
  #csvReader = csv.reader(datafile)
  csvReader = csv.DictReader(dataFile) # ordered dict を生成

  df = pd.DataFrame()
  for row in csvReader:
    df = pd.concat([df, pd.DataFrame([row['Name']], columns=['Name'], index=[row['Year']])])
  df.index.name = 'Year'
  print(df.sort_index(ascending=False))

  # pandas の場合. How simple is that!!
  # csvPage = urlopen('http://www.pythonscraping.com/files/MontyPythonAlbums.csv')
  # print(pd.read_csv(csvPage))