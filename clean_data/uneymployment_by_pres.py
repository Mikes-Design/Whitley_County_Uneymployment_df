import pandas as pd
import matplotlib.pyplot as plt
# This script reads a CSV file containing unemployment data for Whitley County, Kentucky,
df = pd.read_csv('whitley_county_uneymployment.csv')
# It renames the columns for better readability and converts the 'observation_date' column to datetime format.
df = df.rename(columns={'KYWHIT5URN': 'Uneymployment_Rate', 'observation_date': 'Date'})
df['Date'] = pd.to_datetime(df['Date'])

#dictonaries of presidents and their terms
democrat_presidents = {'Bill Clinton' : '1993-2001', 'Barack Obama' : '2009-2017', 'Biden' : '2021-2025'}
republican_presidents = {'George Bush' : '1989-1993', 'George W Bush' : '2001-2009', 'Donald Trump' : '2017-2021'}

#current uneymployment rate
#uneymployment_2025 = df.loc[df['Date'] >= '2025-01-01']
#plots current uneymployment rate
#uneymployment_2025.plot(x='Date', y='Uneymployment_Rate', kind='bar', title='Current Uneymployment Rate in Whitley County', ylabel='Uneymployment Rate (%)', xlabel='Date')

fig, ax = plt.subplots(figsize=(15, 8))

dem_colors = {
    'Bill Clinton': 'royalblue',
    'Barack Obama': 'dodgerblue',
    'Biden': 'lightblue'
}

rep_colors = {
    'George Bush': 'darkred',
    'George W Bush': 'red',
    'Donald Trump': 'indianred'
}

# Create single figure and axis
fig, ax = plt.subplots(figsize=(15, 8))

# Plot Democratic presidents with different blues
for president, term in democrat_presidents.items():
    start_year, end_year = term.split('-')
    mask = df['Date'].between(f'{start_year}-01-01', f'{end_year}-12-31')
    df[mask].plot(
        x='Date', 
        y='Uneymployment_Rate',
        label=president,
        color=dem_colors[president],
        alpha=0.9,
        ax=ax
    )

# Plot Republican presidents with different reds
for president, term in republican_presidents.items():
    start_year, end_year = term.split('-')
    mask = df['Date'].between(f'{start_year}-01-01', f'{end_year}-12-31')
    df[mask].plot(
        x='Date', 
        y='Uneymployment_Rate',
        label=president,
        color=rep_colors[president],
        alpha=0.9,
        ax=ax
    )


# Add labels and styling
ax.set_title('Whitley County Unemployment Rate by President')
ax.set_ylabel('Unemployment Rate (%)')
ax.set_xlabel('Date')
ax.grid(True, linestyle='--', alpha=0.7)
ax.legend()

plt.tight_layout()
plt.show()




