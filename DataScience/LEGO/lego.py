import pandas as pd
from matplotlib import pyplot as plt


def blank_lines():
    print('\n\n\n')


col_df = pd.read_csv('colors.csv')
col_df['name'].nunique()
col_df.groupby('is_trans').count()

sets_df = pd.read_csv('sets.csv')
print(sets_df.columns)

themes_df = pd.read_csv('themes.csv')
print(themes_df.columns)

# blank_lines()
# print(sets_df[sets_df['year'] == 1949])
# blank_lines()
# print(sets_df.sort_values('num_parts', ascending=False).head())
# blank_lines()

years = tuple(range(1950, 2018))

sets_per_year = sets_df.groupby('year').count()['name'][:-2]
themes_by_year = sets_df.groupby('year').agg({'theme_id': pd.Series.nunique})
themes_by_year.rename(columns={'theme_id': 'nr_themes'}, inplace=True)

# ax1 = plt.gca()
# ax2 = ax1.twinx()
#
# ax1.plot(sets_per_year.index[:-2], sets_per_year[:-2], color='green')
# ax2.plot(themes_by_year.index[:-2], themes_by_year.nr_themes[:-2], color='blue')
#
# ax1.set_xlabel('Year')
# ax1.set_ylabel('Number of sets', color='green')
# ax2.set_ylabel('Number of themes', color='blue')


# parts_per_set = sets_df.groupby('year').agg({'num_parts': pd.Series.mean})
# plt.scatter(parts_per_set.index[:-2], parts_per_set[:-2])
# plt.show()

set_theme_count = sets_df['theme_id'].value_counts()
print(set_theme_count.head())
blank_lines()
star_wars_ids = themes_df[themes_df['name'] == 'Star Wars']['id']
print(star_wars_ids)
blank_lines()
print(sets_df[sets_df['theme_id'] == 158].sort_values('year'))
blank_lines()
set_theme_count = pd.DataFrame({
    'id': set_theme_count.index,
    'set_count': set_theme_count.values
})
print(set_theme_count.head())
blank_lines()

merged_df = pd.merge(set_theme_count, themes_df, on='id')
print(merged_df)

plt.figure(figsize=(14, 8))
plt.xticks(fontsize=14, rotation=45)
plt.yticks(fontsize=14)
plt.ylabel('Number of sets', fontsize=14)
plt.xlabel('Theme name', fontsize=14)

plt.bar(merged_df.name[:10], merged_df.set_count[:10])

plt.tight_layout()
plt.show()
