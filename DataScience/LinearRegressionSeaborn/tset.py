import pandas as pd

df = pd.read_csv('cost_revenue_dirty.csv')
df['USD_Production_Budget'] = pd.to_numeric(df['USD_Production_Budget'].str.replace('$', '').str.replace(',', ''))
