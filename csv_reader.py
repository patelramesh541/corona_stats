import numpy as np
import csv
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('/home/rameshlpatel/Downloads/novel-corona-virus-2019-dataset/covid_19_data.csv', sep=',', quotechar='"',parse_dates=True)
#print(df.iloc[0])
#print(df.head(20))
#print(df.values)
#df.sort(['Confirmed'], ascending=[1])
df1 = df.groupby('Country/Region').sum().sort_values(by=['Confirmed'], ascending=False).head(5) 
df1['Confirmed'].plot(x ='Country/Region', y='Confirmed', kind = 'bar')
plt.savefig('graph.png')
