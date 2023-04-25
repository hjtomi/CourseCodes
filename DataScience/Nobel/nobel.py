import pandas as pd
from sklearn.linear_model import LinearRegression
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('nobel_prize_data.csv')

# prizes_by_country = pd.DataFrame({'country': sorted(df['birth_country_current'].dropna().unique().tolist()),
#                                   'prizes': df['birth_country_current'].value_counts().reset_index().sort_values('index')['birth_country_current'].values})
#
# prizes_by_country = df.groupby('birth_country_current', as_index=False).aggregate({'prize': pd.Series.count})
#
# print(prizes_by_country)

# print(df[df['organization_name'] == 'Columbia University'])
# df = df.dropna(subset=['organization_country', 'organization_city', 'organization_name'])
# fig = px.sunburst(df, path=['organization_country', 'organization_city', 'organization_name'])
# fig.show()

df['birth_date'] = pd.to_datetime(df['birth_date'])
df['winning_age'] = df['year'] - df['birth_date'].dt.year
print(df.head().to_string())
print(df.columns)
fig = sns.lmplot(data=df, x='year', y='winning_age', hue='category', lowess=True)
plt.show()

# plt.figure(figsize=(8, 4), dpi=200)
# sns.regplot(data=df, x='year', y='winning_age', lowess=True, scatter_kws={'alpha': 0.4}, line_kws={'color': 'black'})
# plt.show()
# sns.boxplot(df, x='category', y='winning_age')
# plt.show()
