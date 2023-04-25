import pandas as pd
import seaborn as sns
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

df = pd.read_csv('cost_revenue_dirty.csv')
df['USD_Production_Budget'] = pd.to_numeric(df['USD_Production_Budget'].str.replace('$', '').str.replace(',', ''))
df['USD_Worldwide_Gross'] = pd.to_numeric(df['USD_Worldwide_Gross'].str.replace('$', '').str.replace(',', ''))
df['USD_Domestic_Gross'] = pd.to_numeric(df['USD_Domestic_Gross'].str.replace('$', '').str.replace(',', ''))
df['Release_Date'] = pd.to_datetime(df['Release_Date'])

# sns.regplot(df, x='USD_Production_Budget', y='USD_Worldwide_Gross', line_kws={'color': 'red'})
# plt.show()
print(df['USD_Production_Budget'])
reg = LinearRegression()
reg.fit(X=df[['USD_Production_Budget']], y=df[['USD_Worldwide_Gross']])
print(reg.coef_)
print(reg.intercept_)
print(reg.score(df[['USD_Production_Budget']], df[['USD_Worldwide_Gross']]))

