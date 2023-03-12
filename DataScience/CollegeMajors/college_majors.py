import pandas as pd

pd.options.display.float_format = '{:,.2f}'.format

df = pd.read_csv('salaries_by_college_major.csv')
clean_df = df.dropna()
print(clean_df.columns)
print('\n')
# 1
print(clean_df.loc[clean_df['Mid-Career Median Salary'].idxmax()]['Undergraduate Major'])
print(clean_df['Mid-Career Median Salary'].max())
print('\n')
# 2
print(clean_df['Undergraduate Major'][clean_df['Starting Median Salary'].idxmin()])
print(clean_df['Starting Median Salary'].min())
print('\n')
# 3
print(clean_df['Undergraduate Major'][clean_df['Mid-Career Median Salary'].idxmin()])
print(clean_df['Mid-Career Median Salary'].min())

# Low-risk-majors
spread_col = clean_df['Mid-Career 90th Percentile Salary'] - clean_df['Mid-Career 10th Percentile Salary']
clean_df.insert(5, 'Spread', spread_col)
print(clean_df.head())

low_risk = clean_df.sort_values('Spread')
print(low_risk[['Undergraduate Major', 'Spread']].head())
print('\n')

# 4
highest_potential = clean_df.sort_values("Mid-Career 90th Percentile Salary", ascending=False)
print(highest_potential[['Undergraduate Major', 'Mid-Career 90th Percentile Salary']].head())
print('\n')

# 5
high_risk = clean_df.sort_values('Spread', ascending=False)
print(high_risk[['Undergraduate Major', 'Spread']].head())
print('\n')

# Grouping
print(clean_df.groupby('Group').mean())
