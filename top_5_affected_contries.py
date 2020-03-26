import numpy as np
import csv
import pandas as pd
import matplotlib.pyplot as plt
fig = plt.gcf()
fig.set_size_inches(18.5, 10.5)
df=pd.read_csv('/home/rameshlpatel/Downloads/novel-corona-virus-2019-dataset/covid_19_data.csv', sep=',', quotechar='"',parse_dates=True)
df1 = df.groupby('Country/Region').sum().sort_values(by=['Confirmed'], ascending=False).head(5) 
df1['Confirmed'].plot(x ='Country/Region', y='Confirmed', kind = 'bar')
plt.savefig('top_5_affected_countries.png')

