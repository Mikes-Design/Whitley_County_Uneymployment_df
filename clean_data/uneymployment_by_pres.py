import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('whitley_county_uneymployment.csv')

df = df.rename(columns={'KYWHIT5URN': 'Uneymployment_Rate', 'observation_date': 'Date'})


democrat_presidents = {'Bill Clinton' : '1993-2001', 'Barack Obama' : '2009-2017', 'Biden' : '2021-2025'}
republican_presidents = {'George Bush' : '1989-1993', 'George W Bush' : '2001-2009', 'Donald Trump' : '2017-2021'}

uneymployment_2025 = df.tail(2)

uneymployment_2025.plot(x='Date', y='Uneymployment_Rate', kind='bar', title='Current Uneymployment Rate in Whitley County', ylabel='Uneymployment Rate (%)', xlabel='Date')
plt.show() 
